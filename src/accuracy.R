## this is necessary because I forgot to add nested effects for session/subject
library(ProjectTemplate)
load.project()

options(mc.cores=parallel::detectCores())
theme_set(theme_bw())
bname<-tools::file_path_sans_ext(basename(this.file.name()))
#stop()

d <- learn %>% ungroup %>%
  mutate(session=fct_relevel(session, "s_trng")) %>% 
  mutate(ztrial=(trial-mean(trial))/sd(trial),
         sorder=ordered(sorder),
         sorder_int=as.integer(sorder)-1,
         card_type=fct_relevel(card_type, "GoWin"))
#stop()
#===========================================================
## Function applied to every model for fitting and plotting
#===========================================================
fit_and_plot <- function(mod.name,frm,load.only=F,plot.only.new=T){
  is.new=TRUE
  
  if(!is.cached.var(mod.name,base=bname)){
    mod<-brm(frm,data=d,family=bernoulli())
    assign(mod.name,mod,envir=.GlobalEnv)
    cache.var(mod.name,bname)
  } else {
    mod<-load.cache.var(mod.name,bname)
    is.new=FALSE
  }

  if(!load.only & ((is.new & plot.only.new) | (!plot.only.new))  ){
      
    pdf(plot.filename(sprintf("diag_%s.pdf",mod.name),base=bname),width=5,height=10)
    mcmc_rhat(rhat(mod))%>%print
    mcmc_neff(neff_ratio(mod))%>%print
    dev.off()
    
    
     if(dim(attr(terms(frm),"factors"))[2]>1){
       ## needs to catch error because null model does not have effects
       pdf(plot.filename(sprintf("marginal_%s.pdf",mod.name),base=bname),width=4,height=3)
       map(plot(marginal_effects(mod),ask=F,plot=F),function(p) p+ylim(0,1)) %>% print
       plot(marginal_effects(mod, probs=c(0.05,0.95)),ask=F)
       dev.off()
     } else {
       message("Not plotting marginal effects for ", frm);
     }
  }  
  # pdf(plot.filename(sprintf("ppred_%s.pdf",mod.name),base=bname),width=15,height=10)
  # d %>% add_predicted_draws(mod,n=100) %>%
  #   group_by(conflict,session,learner,participant,.iteration) %>%
  #   summarize(pred=mean(pred),accuracy=mean(accuracy)) %>%
  #   ggplot(aes(x=conflict,y=accuracy,color=session))+
  #   stat_pointinterval(aes(y=pred),.width=c(.99,.95,.8,.5))+
  #   stat_summary(fun.y=mean,size=2,color="red",geom="point")+
  #   facet_grid(session~conflict~participant) +
  #   labs(title="Mean ACC per participant split by session/conflict")->p
  # print(p)

  return(mod)
}

#=====================================
## Model definitions
#=====================================
models<-list(
  formula(accuracy ~ (1|participant/session)),
  formula(accuracy ~ ztrial+(1|participant/session)),
  formula(accuracy ~ session+(1|participant/session)),
  formula(accuracy ~ sorder_int+(1|participant/session)),
  formula(accuracy ~ card_type+(1|participant/session)),
  formula(accuracy ~ ztrial+sorder_int+(1|participant/session)),
  formula(accuracy ~ ztrial+session+(1|participant/session)),
  formula(accuracy ~ ztrial+card_type+(1|participant/session)),
  formula(accuracy ~ ztrial+card_type+session+(1|participant/session)),
  formula(accuracy ~ ztrial+card_type+sorder_int+(1|participant/session)),  
  formula(accuracy ~ ztrial+card_type+sorder_int+session+(1|participant/session)),    
  formula(accuracy ~ ztrial*session+(1|participant/session)),
  formula(accuracy ~ sorder_int+session+(1|participant/session)),
  formula(accuracy ~ sorder_int*session+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial+sorder_int+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial+session+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial+sorder_int+session+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial+sorder_int*session+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial+session+session:ztrial+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial*session+(1|participant/session)),
  formula(accuracy ~ card_type*ztrial*session+sorder_int+(1|participant/session))
)
names(models)<-sprintf("mod%02i",1:length(models))

descriptions=c("Null", "Trial", "tACS", "order", "card", "trial+order", "trial+tACS", "trial+card", "trial+card+tACS",
                     "trial+card+order", "trial+card+order+tACS", "trial x tACS", "order + tACS", "order x tACS", 
                     "card x trial", "card x trial + order", "card x trial + tACS", "card x trial + tACS + order",
                     "card x trial + tACS x order", "card x trial + tACS x trial", "card x trial x tACS", "card x trial x tACS + order") 

#========================
## fit models
#========================
#library(parallel)
#library(furrr)
#plan(multiprocess, workers = 60)
library(pbapply)
models.wrap <- map2(names(models), models, ~ list(mod.name=.x, mod=.y))
models.fitted=pblapply(models.wrap, function(lmod){ fit_and_plot(lmod$mod.name, lmod$mod)}, cl=4)
#models.fitted=map2(names(models), models, fit_and_plot, load.only=F)
#models.fitted=future_map2(names(models), models, fit_and_plot, .progress = T)
names(models.fitted) <- names(models)


#models.fitted=map2(names(models),models,fit_and_plot)
#names(models.fitted) <- names(models)
#stop()
#========================
## model-selection
#========================
loos=if.cached.load("loos",{
  map(models.fitted, LOO, pointwise=F) 
},base=bname)
loos=map2(names(models),loos,function(mname,mod){mod$model_name=mname;mod})
names(models)
names(loos) <- names(models)

valid.models=as.logical(unlist(map(models.fitted, ~ tail(sort(brms::rhat(.x)),1)))<1.05)

sink(log.filename("models.log",base=bname))
tibble(
  model_num=names(models[valid.models]),
  model=paste(format(models[valid.models]),sep="")
) %>% print(n=Inf)
sink()
loo_compare(loos[valid.models])

#stop()
#expected log predictive density (ELPD)
loo_compare(loos[valid.models]) %>% as.data.frame %>%rownames_to_column(var="mod") %>%
  mutate(dlooic=-(looics-looics[mod=="mod01"])) %>%
  mutate(win=if_else(looics==min(looics), T,F)) %>%
  ggplot(aes(mod, dlooic, fill = win)) +
  geom_bar(stat = "identity", position =
             position_dodge()) + coord_flip() +
  scale_fill_manual(values=c("lightblue", "orange"))+
  geom_text(mapping=aes(fill=NULL, label=(descriptions[valid.models])), y=0, hjust="right")+
  labs(x="",y="LOOIC")+
  theme(axis.ticks.y = element_blank(),
        legend.position = "none",
        axis.text.y=element_blank(),
        panel.grid = element_blank(),
        strip.background = element_blank(),
        strip.text = element_text(size=12),
        strip.placement = "inside") #-> p.mod.prob

ggsave(plot.filename("looic.png", bname), width=6, height=8)
   
#r=loo::loo_model_weights(x=map(models.fitted, ~ .x$loo))
mod.weights = if.cached.load("mod.weights",
                             map_df(c("loo", "waic", "loo2"), function(strat) {
                               r = invoke(
                                 model_weights_wrapper,
                                 .x = models.fitted,
                                 weights = strat,
                                 model_names = names(models.fitted)
                               )
                               bind_cols(strategy = strat, data.frame(t(r)))
                             }), bname)


mod.desc=data.frame(mod=names(models.fitted),descriptions=descriptions)
map_df(c("loo","loo2","waic"), ~ cbind(strategy=.x,mod.desc)) %>%
  spread(strategy,descriptions) %>%
  #mutate(loo2="",waic="") %>%
  gather(strategy,descriptions,loo,loo2,waic) -> mod.desc

## model - weight plot
mod.weights %>%
  gather(mod, prob, starts_with("mod")) %>% 
  full_join(mod.desc) %>%
  mutate(
    strategy=ordered(strategy, c("loo", "waic","loo2")),
    strategy=ordered(case_when(strategy=="loo" ~ "LOO",
                               strategy=="waic" ~ "WAIC",
                               strategy=="loo2" ~ "pseudo-BMA"),
                     c("LOO","WAIC","pseudo-BMA"))) %>%
  filter(strategy!="WAIC") %>% droplevels %>%
  group_by(strategy) %>%
  mutate(win=if_else(prob==max(prob), T,F)) %>%
  ungroup %>%
  ggplot(aes(mod, prob, fill = win)) +
  geom_bar(stat = "identity", position =
             position_dodge()) + coord_flip() +
  scale_fill_manual(values=c("lightblue", "orange"))+
  geom_text(mapping=aes(fill=NULL, label=descriptions), y=0, hjust="left")+
  labs(x="",y="Posterior Probability")+
  facet_wrap(~strategy)+
  theme(axis.ticks.y = element_blank(),
        legend.position = "none",
        axis.text.y=element_blank(),
        panel.grid = element_blank(),
        strip.background = element_blank(),
        strip.text = element_text(size=12),
        strip.placement = "inside") -> p.mod.prob

p.mod.prob
ggsave(plot.filename("weights.png", bname), width=10, height=5)


## DETAILED MODEL SUMMARY
##=======================
mod.name="mod22"
mod<-models.fitted[[mod.name]]
session_labels=rev(c("trng", "amp", "cntrl", "peak", "trough"))

#marginal_effects(mod, effects=c("session"))
#brms::stanplot(mod)

samp=as.matrix(mod)

## MAIN EFFECT SESSION
##=======================
session.vars=str_subset(colnames(samp), "b_sessions", )
M=cbind(b_sessions_trng=0, samp[,session.vars])
colnames(M) <- map(str_split(colnames(M), "_"), tail, 1)
me=marginal_effects(mod, plot=F)
#stop()

map_df(as.data.frame(t(expand.grid(colnames(M), colnames(M)))), function(x){
  a=as.character(x[1])
  b=as.character(x[2])
  p=sum(M[,a]-M[,b]<0)/as.numeric(dim(M)[1])
  data.frame(a=a,b=b,p=p)
}) %>%
  mutate(a=factor(a, levels=colnames(M)),
         b=factor(b, levels=(colnames(M)))) %>%
  #filter(as.integer(a)<=as.integer(b)) %>%
  mutate(a=factor(a, levels=rev(colnames(M))),
         p=ifelse(a==b,NA, p)) -> r


me$session %>%data.frame %>% 
  mutate(session=map_chr(str_split(session,"_"), ~ .x[2]),
         session=factor(session, levels=rev(colnames(M)))) %>%
  ggplot(aes(y=estimate__,x=session,ymin=lower__, ymax=upper__))+
  geom_pointrange()+coord_flip()+
  labs(x="Accuracy", y="Session",title="Main-Effect Accuracy") -> p1

as.data.frame(M) %>%
  gather(session,val) %>% 
  mutate(session=factor(session, levels=rev(colnames(M)))) %>%
  ggplot(aes(x=val,y=session))+
  geom_halfeyeh(fun.data=mean_hdi)+
  stat_pointintervalh(.width = c(.66, .95))+
  geom_vline(xintercept = 0, color="red")+
  labs(x="Coefficient", y="Session")+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank())  -> p2

ggplot(r, aes(b,a,fill=p))+
  geom_tile(alpha=0.7, color="black", size=.6)+
  geom_text(aes(label=ifelse(is.na(p), "", sprintf("%.2f",p))))+
  scale_fill_gradientn(colors = jet.colors(7))+
  scale_x_discrete(position = "top") +
  labs(x="Session A", y="Session B",
       fill="P(A>B|M)", 
       caption=mod.name) +
  coord_fixed()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) -> p3


library(patchwork)
p=(p1+p2+p3)
ggsave(plot=p, filename = plot.filename("maineff_tacs.png", bname), height=5, width=10)

## IA SESSION x CARD
##=======================
me$`card_type:session`%>%data.frame %>% 
  mutate(session=map_chr(str_split(session,"_"), ~ .x[2]),
         session=factor(session, levels=session_labels)) %>%
  ggplot(aes(y=estimate__,x=session,ymin=lower__, ymax=upper__,color=card_type))+
  geom_pointrange(position = position_dodge(width=0.3))+coord_flip()+
  labs(x="Accuracy", y="Session",title="IA card x tACS Accuracy") -> p1

library(ggridges)
session.vars=str_subset(str_subset(str_subset(colnames(samp), "b_card_type"), "ztrial", negate = T), ":")
card.vars=str_subset(str_subset(colnames(samp), "b_card_type"), ":", negate = T)

M2=samp[,card.vars]
colnames(M2)<-sprintf("%s:session_trng", colnames(M2))
M=cbind(M2,samp[,session.vars])
data.frame(M) %>% mutate(ix=1:n()) %>% gather(var,val,-ix) %>%
  separate(var, c("card","session"), sep="\\.") %>%
  mutate(card=str_sub(map_chr(str_split(card, "_"), ~ .x[3]), 5),
         card=factor(card, levels=card_labels),
         session=map_chr(str_split(session,"_"), ~ .x[2]),
         session=factor(session, levels=session_labels)) %>%
  ggplot(aes(x=val,y=session,color=card, fill=card))+
  geom_density_ridges(alpha=0.4, position=position_dodge(width=0.3), rel_min_height=0.01,scale=0.7)+
  stat_pointintervalh(.width = c(.66, .95))+
  geom_vline(xintercept = 0, color="red")+
  labs(x="Coefficient", y="Session")+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) -> p2
  
  
p=(p1+p2)
p
ggsave(plot=p, filename = plot.filename("ia_tacs_card.png", bname), height=5, width=10)

### PAPER PLOT
card_to_label=c("GoWin"="Go-to-Win", "NoGoWin"="NoGo-to-Win", "GoAvo"="Go-to-Avoid", "NoGoAvo"="NoGo-to-Avoid")

me$`card_type:session`%>%data.frame %>% 
  mutate(session=map_chr(str_split(session,"_"), ~ .x[2]),
         session=factor(session, levels=session_labels)) %>%
  mutate(session=fct_recode(session, 
                            AM="amp", Peak="peak", Control="cntrl",Training="trng", Trough="trough"),
         session=fct_relevel(session, "Training", "Control", "AM", "Peak", "Trough")) %>%
  ggplot(aes(y=estimate__,x=session,ymin=lower__, ymax=upper__,color=card_type))+
  geom_pointrange(position = position_dodge(width=0.3))+
  labs(y="Accuracy", x="Session",title="",color="Card") 
sc=0.8
ggsave(plot.filename("paper_card_session.png",bname), width=sc*6,height=sc*4,dpi=300)

## stanplots

maineff.labs=str_subset(str_subset(colnames(samp), ":", negate = T), "b_")
brms::stanplot(mod, pars=maineff.labs, exact_match=T)+geom_vline(xintercept = 0, color="red")-> p1

twoay.ia=colnames(samp)[str_count(colnames(samp), ":")==1]
brms::stanplot(mod, pars=twoay.ia, exact_match=T)+geom_vline(xintercept = 0, color="red") -> p2

threeway.ia=colnames(samp)[str_count(colnames(samp), ":")==2]
brms::stanplot(mod, pars=threeway.ia, exact_match=T)+geom_vline(xintercept = 0, color="red")-> p3

p=p1+p2+p3
p
ggsave(plot=p, filename = plot.filename("stanplots.png", bname), height=5, width=15)


##  matrices
cards=card_labels #as.character(unique(d$card_type))
M=cbind(samp, b_sessions_trng=0, 
        `b_card_typeGoWin:sessions_trng`=0, `b_card_typeGoAvo:sessions_trng`=0, `b_card_typeNoGoAvo:sessions_trng`=0,`b_card_typeNoGoWin:sessions_trng`=0,
        `b_card_typeGoWin:sessions_amp`=0, `b_card_typeGoWin:sessions_peak`=0, `b_card_typeGoWin:sessions_trough`=0, `b_card_typeGoWin:sessions_cntrl`=0)

ps=map(cards, function(card){
  cat(card)
  map_df(as.data.frame(t(expand.grid(session_labels, session_labels))), function(x){
    a=as.character(x[1])
    b=as.character(x[2])
    alab=sprintf("b_sessions_%s",a)
    blab=sprintf("b_sessions_%s",b)
    cat(sprintf("a=b_card_type%s:sessions_%s\n",card,a))
    cat(sprintf("b=b_card_type%s:sessions_%s\n",card,b))
    
    aeff=M[,alab]+M[,sprintf("b_card_type%s:sessions_%s",card,a)]
    beff=M[,blab]+M[,sprintf("b_card_type%s:sessions_%s",card,b)]
    
    p=sum(aeff-beff<0)/as.numeric(dim(M)[1])
    data.frame(a=a,b=b,p=p)
  }) %>%
    mutate(a=factor(a, levels=session_labels),
           b=factor(b, levels=session_labels)) %>%
    #filter(as.integer(a)<=as.integer(b)) %>%
    mutate(b=factor(b, levels=rev(session_labels)),
           p=ifelse(a==b,NA, p)) -> r
  
  ggplot(r, aes(b,a,fill=p))+
    geom_tile(alpha=0.7, color="black", size=.6)+
    geom_text(aes(label=ifelse(is.na(p), "", sprintf("%.2f",p))))+
    scale_fill_gradientn(colors = jet.colors(7))+
    scale_x_discrete(position = "top") +
    labs(x="Session A", y="Session B",
         fill="P(A>B|M)", title=card,
         caption=mod.name) +
    coord_fixed()+
    theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.border = element_blank(),
          panel.background = element_blank()) -> p
  return(p)
})

p=(ps[[1]]+ps[[2]]+ps[[3]]+ps[[4]])+plot_layout(ncol=4)
p 
ggsave(plot.filename("ia_matrices.png", bname), plot=p, width=20, height=5)
###------------------------------------------------------------------------------
## IA tacs x trial


me$`ztrial:session` %>% data.frame %>%
  ggplot(aes(ztrial, estimate__,color=session))+geom_line()+
  labs(y="P(correct)",title="IA tACS x trial")+
  coord_fixed(ratio=10)-> p1

vars=str_subset(str_subset(colnames(samp)[str_count(colnames(samp), ":")==1], "ztrial"), "session")
M=cbind(samp[,vars],`b_ztrial:sessions_trng`=0)

as.data.frame(M) %>%
  gather(session,val) %>% 
  mutate(session=map_chr(str_split(session, "_"), ~ .x[3])) %>%
  mutate(session=factor(session, levels=session_labels)) %>%
  ggplot(aes(x=val,y=session))+
  geom_halfeyeh(fun.data=mean_hdi)+
  stat_pointintervalh(.width = c(.66, .95))+
  geom_vline(xintercept = 0, color="red")+
  labs(x="Coefficient", y="Session")+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) -> p2


map_df(as.data.frame(t(expand.grid(session_labels, session_labels))), function(x){
  a=as.character(x[1])
  b=as.character(x[2])
  alab=sprintf("b_ztrial:sessions_%s",a)
  blab=sprintf("b_ztrial:sessions_%s",b)

  aeff=M[,alab]#+M[,sprintf("b_card_type%s:sessions_%s",card,a)]
  beff=M[,blab]#+M[,sprintf("b_card_type%s:sessions_%s",card,b)]
  
  p=sum(aeff-beff<0)/as.numeric(dim(M)[1])
  data.frame(a=a,b=b,p=p)
}) %>%
  mutate(a=factor(a, levels=session_labels),
         b=factor(b, levels=session_labels)) %>%
  #filter(as.integer(a)<=as.integer(b)) %>%
  mutate(b=factor(b, levels=rev(session_labels)),
         p=ifelse(a==b,NA, p)) -> r

ggplot(r, aes(b,a,fill=p))+
  geom_tile(alpha=0.7, color="black", size=.6)+
  geom_text(aes(label=ifelse(is.na(p), "", sprintf("%.2f",p))))+
  scale_fill_gradientn(colors = jet.colors(7))+
  scale_x_discrete(position = "top") +
  labs(x="Session A", y="Session B",
       fill="P(A>B|M)",
       caption=mod.name) +
  coord_fixed()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) -> p3

p=(p1+p2+p3)
p
ggsave(plot=p, filename = plot.filename("ia_tacs_trial.png", bname), height=5, width=15)

###------------------------------------------------------------------------------
## IA card x trial


me$`ztrial:card_type` %>% data.frame %>%
  ggplot(aes(ztrial, estimate__,color=card_type))+geom_line()+
  labs(y="P(correct)",title="IA card x trial")+
  coord_fixed(ratio=10)-> p1

vars=str_subset(str_subset(colnames(samp)[str_count(colnames(samp), ":")==1], "ztrial"), "card_type")
M=cbind(samp[,vars],`b_card_typeGoWin:ztrial`=0)
card_labels=c("GoWin", "NoGoAvo", "GoAvo", "NoGoWin")#as.character(unique(d$card_type))

as.data.frame(M) %>%
  gather(card,val) %>% 
  mutate(card=str_sub(map_chr(str_split(card, "_"), ~ .x[3]), 5,-8)) %>%
  mutate(card=factor(card, levels=card_labels)) %>%
  ggplot(aes(x=val,y=card))+
  geom_halfeyeh(fun.data=mean_hdi)+
  stat_pointintervalh(.width = c(.66, .95))+
  geom_vline(xintercept = 0, color="red")+
  labs(x="Coefficient", y="card")+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) -> p2


map_df(as.data.frame(t(expand.grid(card_labels, card_labels))), function(x){
  a=as.character(x[1])
  b=as.character(x[2])
  alab=sprintf("b_card_type%s:ztrial",a)
  blab=sprintf("b_card_type%s:ztrial",b)
  
  aeff=M[,alab]
  beff=M[,blab]
  
  p=sum(aeff-beff<0)/as.numeric(dim(M)[1])
  data.frame(a=a,b=b,p=p)
}) %>%
  mutate(a=factor(a, levels=card_labels),
         b=factor(b, levels=card_labels)) %>%
  #filter(as.integer(a)<=as.integer(b)) %>%
  mutate(b=factor(b, levels=rev(card_labels)),
         p=ifelse(a==b,NA, p)) -> r

ggplot(r, aes(b,a,fill=p))+
  geom_tile(alpha=0.7, color="black", size=.6)+
  geom_text(aes(label=ifelse(is.na(p), "", sprintf("%.2f",p))))+
  scale_fill_gradientn(colors = jet.colors(7))+
  scale_x_discrete(position = "top") +
  labs(x="Card A", y="Card B",
       fill="P(A>B|M)",
       caption=mod.name) +
  coord_fixed()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) -> p3

library(patchwork)
p=(p1+p2+p3)
p
ggsave(plot=p, filename = plot.filename("ia_card_trial.png", bname), height=5, width=15)


## IA SESSION x TRIAL x CARD 
##===========================

conds=make_conditions(d, vars=c("session"))
me2=marginal_effects(mod, effects="ztrial:card_type", conditions=conds,  plot=F)
me2$`ztrial:card_type` %>%
  mutate(pgo=if_else(card_type %in% c("GoWin", "GoAvo"), estimate__, 1-estimate__)) %>%
  mutate(session=map_chr(str_split(session,"_"), ~ .x[2]),
         session=factor(session, levels=rev(session_labels))) %>%
  ggplot(aes(y=pgo,x=ztrial,color=card_type))+
  geom_line()+
  labs(x="Trial", y="P(Go)",title="Marginal effects: card x ztrial per tACS")+
  facet_wrap(~ session, ncol=5)#-> p1

sc=0.8
ggsave(filename=plot.filename("me_card_ztrial_sdssion.png", bname), height=4*sc, width=15*sc)


##  matrices
interc=samp[,"b_ztrial"]
data.frame(samp) %>%
  mutate(
    `a_trng:GoWin`  = b_ztrial,
    `a_trng:NoGoAvo`= b_ztrial+`b_card_typeNoGoAvo.ztrial`,
    `a_trng:GoAvo`  = b_ztrial+`b_card_typeGoAvo.ztrial`,
    `a_trng:NoGoWin`= b_ztrial+`b_card_typeNoGoWin.ztrial`,
    
    `a_amp:GoWin`  =  b_ztrial+`b_ztrial.sessions_amp`,
    `a_amp:NoGoAvo`=  b_ztrial+`b_ztrial.sessions_amp` + `b_card_typeNoGoAvo.ztrial` + `b_card_typeNoGoAvo.ztrial.sessions_amp`,
    `a_amp:GoAvo`  =  b_ztrial+`b_ztrial.sessions_amp` + `b_card_typeGoAvo.ztrial` + `b_card_typeGoAvo.ztrial.sessions_amp`,
    `a_amp:NoGoWin`=  b_ztrial+`b_ztrial.sessions_amp` + `b_card_typeNoGoWin.ztrial` + `b_card_typeNoGoWin.ztrial.sessions_amp`,

    `a_cntrl:GoWin`  =  b_ztrial+`b_ztrial.sessions_cntrl`,
    `a_cntrl:NoGoAvo`=  b_ztrial+`b_ztrial.sessions_cntrl` + `b_card_typeNoGoAvo.ztrial` + `b_card_typeNoGoAvo.ztrial.sessions_cntrl`,
    `a_cntrl:GoAvo`  =  b_ztrial+`b_ztrial.sessions_cntrl` + `b_card_typeGoAvo.ztrial` + `b_card_typeGoAvo.ztrial.sessions_cntrl`,
    `a_cntrl:NoGoWin`=  b_ztrial+`b_ztrial.sessions_cntrl` + `b_card_typeNoGoWin.ztrial` + `b_card_typeNoGoWin.ztrial.sessions_cntrl`,
    
    `a_peak:GoWin`  =  b_ztrial+`b_ztrial.sessions_peak`,
    `a_peak:NoGoAvo`=  b_ztrial+`b_ztrial.sessions_peak` + `b_card_typeNoGoAvo.ztrial` + `b_card_typeNoGoAvo.ztrial.sessions_peak`,
    `a_peak:GoAvo`  =  b_ztrial+`b_ztrial.sessions_peak` + `b_card_typeGoAvo.ztrial` + `b_card_typeGoAvo.ztrial.sessions_peak`,
    `a_peak:NoGoWin`=  b_ztrial+`b_ztrial.sessions_peak` + `b_card_typeNoGoWin.ztrial` + `b_card_typeNoGoWin.ztrial.sessions_peak`,

    `a_trough:GoWin`  =  b_ztrial+`b_ztrial.sessions_trough`,
    `a_trough:NoGoAvo`=  b_ztrial+`b_ztrial.sessions_trough` + `b_card_typeNoGoAvo.ztrial` + `b_card_typeNoGoAvo.ztrial.sessions_trough`,
    `a_trough:GoAvo`  =  b_ztrial+`b_ztrial.sessions_trough` + `b_card_typeGoAvo.ztrial` + `b_card_typeGoAvo.ztrial.sessions_trough`,
    `a_trough:NoGoWin`=  b_ztrial+`b_ztrial.sessions_trough` + `b_card_typeNoGoWin.ztrial` + `b_card_typeNoGoWin.ztrial.sessions_trough`,
  ) %>%
  mutate_at(vars(starts_with("a_")), ~ . - interc) %>% ## remove the ztrial-intercept again
  select(starts_with("a_")) %>% gather(var,val) %>%
  mutate(var=str_sub(var,3)) %>%
  separate(var, c("session", "card_type")) %>%
  mutate(session=factor(session, levels=session_labels),
         card_type=factor(card_type, levels=card_labels)) -> M.ia

M.ia %>%
  ggplot(aes(x=val,y=session))+
  geom_halfeyeh(fun.data=mean_hdi)+
  stat_pointintervalh(.width = c(.66, .95))+
  geom_vline(xintercept = 0, color="red")+
  labs(x="Coefficient", y="Session")+
  facet_wrap(~card_type,ncol=4)+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank()) #-> p2

sc=0.8
ggsave(filename=plot.filename("coeff_session_ztrial_card.png", bname), height=4*sc, width=15*sc)


##  matrices
cards=as.character(unique(d$card_type))

ps=map(card_labels, function(card){
  cat(card)
  map_df(as.data.frame(t(expand.grid(session_labels, session_labels))), function(x){
    a=as.character(x[1])
    b=as.character(x[2])
    
    aeff=M.ia %>% filter(session==a,card_type==card) %>% pull(val)
    beff=M.ia %>% filter(session==b,card_type==card) %>% pull(val)

    p=sum(aeff-beff<0)/as.numeric(length(aeff))
    data.frame(a=a,b=b,p=p)
  }) %>%
    mutate(a=factor(a, levels=session_labels),
           b=factor(b, levels=session_labels)) %>%
    #filter(as.integer(a)<=as.integer(b)) %>%
    mutate(b=factor(b, levels=rev(session_labels)),
           p=ifelse(a==b,NA, p)) -> r
  
  ggplot(r, aes(b,a,fill=p))+
    geom_tile(alpha=0.7, color="black", size=.6)+
    geom_text(aes(label=ifelse(is.na(p), "", sprintf("%.2f",p))))+
    scale_fill_gradientn(colors = jet.colors(7))+
    scale_x_discrete(position = "top") +
    labs(x="Session A", y="Session B",
         fill="P(A>B|M)", title=card,
         caption=mod.name) +
    coord_fixed()+
    theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.border = element_blank(),
          panel.background = element_blank()) -> p
  return(p)
})

p=(ps[[1]]+ps[[2]]+ps[[3]]+ps[[4]])+plot_layout(ncol=4)
p 
ggsave(plot.filename("ia_session_trial_matrices.png", bname), plot=p, width=20, height=5)

## paper-plot


sessions_labels_pretty=c("amp"="AM", "peak"="Peak", "cntrl"="Control", "trng"="Training", "trough"="Trough")
### mid-exp accuracy
cards=card_labels #as.character(unique(d$card_type))
M=cbind(samp, b_sessions_trng=0, 
        `b_card_typeGoWin:sessions_trng`=0, `b_card_typeGoAvo:sessions_trng`=0, `b_card_typeNoGoAvo:sessions_trng`=0,`b_card_typeNoGoWin:sessions_trng`=0,
        `b_card_typeGoWin:sessions_amp`=0, `b_card_typeGoWin:sessions_peak`=0, `b_card_typeGoWin:sessions_trough`=0, `b_card_typeGoWin:sessions_cntrl`=0)


card_to_label=c("GoWin"="Go-to-Win", "NoGoWin"="NoGo-to-Win", "GoAvo"="Go-to-Avoid", "NoGoAvo"="NoGo-to-Avoid")
ps1=map(cards, function(card){
  cat(card)
  map_df(as.data.frame(t(expand.grid(session_labels, session_labels))), function(x){
    a=as.character(x[1])
    b=as.character(x[2])
    alab=sprintf("b_sessions_%s",a)
    blab=sprintf("b_sessions_%s",b)
    cat(sprintf("a=b_card_type%s:sessions_%s\n",card,a))
    cat(sprintf("b=b_card_type%s:sessions_%s\n",card,b))
    
    aeff=M[,alab]+M[,sprintf("b_card_type%s:sessions_%s",card,a)]
    beff=M[,blab]+M[,sprintf("b_card_type%s:sessions_%s",card,b)]
    
    p=sum(aeff-beff<0)/as.numeric(dim(M)[1])
    data.frame(a=a,b=b,p=p)
  }) %>%
    mutate(a=factor(a, levels=session_labels),
           b=factor(b, levels=session_labels)) %>%
    #filter(as.integer(a)<=as.integer(b)) %>%
    mutate(p=ifelse(as.integer(a)<=as.integer(b),NA, p),
           b=factor(b, levels=rev(session_labels))) %>%
    filter(a!="trng", b!="trng", a!="trough", b!="amp") -> r
  
  r %>%
    mutate(a=fct_recode(a, AM="amp", Peak="peak", Control="cntrl",Training="trng", Trough="trough"),
           b=fct_recode(b, AM="amp", Peak="peak", Control="cntrl",Training="trng", Trough="trough")) %>%
  ggplot(aes(b,a,fill=p))+
    geom_tile(aes(color=is.na(p)), alpha=.8, size=.6)+
    geom_text(aes(label=ifelse(is.na(p), "", sprintf("%.2f",p))))+
    #scale_fill_gradient2(midpoint = 0.5, low = "blue", mid = "white", 
    #                      high = "red", space = "Lab", limits=c(0,1), na.value= "#EEEEEE", guide = "colourbar")+
    scale_fill_gradientn(colors = jet.colors.alpha(100), limits=c(0,1),na.value = "#FFFFFF")+
    scale_color_manual(values=c("#000000FF","#FFFFFF00"),guide = FALSE)+
    #scale_alpha_continuous(limits=c(0,1))+
    scale_x_discrete(position = "top") +
    scale_y_discrete(position = "right")+
    labs(x="Session A", y="Session B",
         fill="P(A>B)", title=card_to_label[card]) +
    coord_fixed()+
    theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          axis.text.y=element_text(size=12),
          axis.text.x=element_text(size=12),
          panel.border = element_blank(),
          panel.background = element_blank())+
    theme(plot.title=element_text(size=15, vjust=.5, hjust=0.5),
          plot.margin = unit(c(.1,.1,.1,.1), "cm")) -> p
  if(card!="NoGoWin"){
    p=p+guides(fill=FALSE)+labs(y="")+theme(axis.title.y=element_blank(),
                                            axis.text.y=element_blank(),
                                            axis.ticks.y=element_blank())
  }   
  if(card=="GoWin"){
    p=p+labs(y="Average Accuracy")+scale_y_discrete(position = "left")+
      theme(axis.title.y=element_text(size=17, angle = 90))
    
  }
  return(p)
})

### learning-rate plot
ps=map(card_labels, function(card){
  cat(card)
  map_df(as.data.frame(t(expand.grid(session_labels, session_labels))), function(x){
    a=as.character(x[1])
    b=as.character(x[2])
    
    aeff=M.ia %>% filter(session==a,card_type==card) %>% pull(val)
    beff=M.ia %>% filter(session==b,card_type==card) %>% pull(val)
    
    p=sum(aeff-beff<0)/as.numeric(length(aeff))
    data.frame(a=a,b=b,p=p)
  }) %>%
    mutate(a=factor(a, levels=session_labels),
           b=factor(b, levels=session_labels)) %>%
    #filter(as.integer(a)<=as.integer(b)) %>%
    mutate(p=ifelse(as.integer(a)<=as.integer(b),NA, p),
           b=factor(b, levels=rev(session_labels))) %>%
    filter(a!="trng", b!="trng", a!="trough", b!="amp")-> r
  
  r %>%
    mutate(a=fct_recode(a, AM="amp", Peak="peak", Control="cntrl",Training="trng", Trough="trough"),
           b=fct_recode(b, AM="amp", Peak="peak", Control="cntrl",Training="trng", Trough="trough")) %>%
  ggplot(aes(b,a,fill=p))+
    geom_tile(aes(color=is.na(p)), alpha=.8, size=.6)+
    geom_text(aes(label=ifelse(is.na(p), "", sprintf("%.2f",p))))+
    #scale_fill_gradient2(midpoint = 0.5, low = "blue", mid = "white", 
    #                      high = "red", space = "Lab", limits=c(0,1), na.value= "#EEEEEE", guide = "colourbar")+
    scale_fill_gradientn(colors = jet.colors.alpha(100), limits=c(0,1),na.value = "#FFFFFF")+
    scale_color_manual(values=c("#000000FF","#FFFFFF00"),guide = FALSE)+
    #scale_alpha_continuous(limits=c(0,1))+
    scale_x_discrete(position = "top") +
    scale_y_discrete(position = "right")+
    labs(x="", y="Session B",
         fill="P(A>B)", title="") +
    coord_fixed()+
    theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.border = element_blank(),
          panel.background = element_blank())+
    theme(axis.title.x=element_blank(),
          axis.text.x=element_blank(),
          axis.ticks.x=element_blank(),
          axis.text.y=element_text(size=12))+    
    theme(plot.title=element_text(size=15, vjust=3),
          plot.margin = unit(c(.1,.1,.1,.1), "cm")) -> p
  if(card!="NoGoWin"){
    p=p+guides(fill=FALSE)+labs(y="")+theme(axis.title.y=element_blank(),
                                           axis.text.y=element_blank(),
                                           axis.ticks.y=element_blank())
  } 
  if(card=="GoWin"){
    p=p+labs(y="Learning Rate")+scale_y_discrete(position = "left")+
      theme(axis.title.y=element_text(size=17, angle = 90))

  }
  return(p)
})

library(ggpubr)
leg=get_legend(ps[[4]])
ps[[4]] <- ps[[4]]+guides(fill=FALSE)
ps1[[4]] <- ps1[[4]]+guides(fill=FALSE)
p <- ((ps1[[1]]/ps[[1]] | ps1[[2]]/ps[[2]] | ps1[[3]]/ps[[3]] | ps1[[4]]/ps[[4]] | as_ggplot(leg)) + plot_layout(heights=1, widths=c(rep(1,4), 0.4)))
p
sc=0.5
ggsave(plot.filename("paper_acc_matrices.png", bname), height=sc*10, width=sc*20, dpi = 300)

###------------------------------------------------------------------------------
###------------------------------------------------------------------------------
###------------------------------------------------------------------------------

d %>% group_by(participant, session, card_type) %>%
  mutate(trial.cond=1:n(),session_index=as.integer(sorder)) %>%
  ungroup() %>%
  mutate(subj.ix=as.numeric(as.factor(participant))) %>% 
  mutate(response.go=case_when(response==1 ~ "go",
                               response==0 ~ "nogo")) %>%
  ggplot()+
  geom_rect(aes(xmin=trial.cond-.5, xmax=trial.cond+.5, ymin=subj.ix-0.5, ymax=subj.ix+0.5, fill=response.go))+
  scale_y_continuous(breaks = (1:length(unique(d$participant)))-.5, labels=d$participant %>% as.factor %>% levels,
                     sec.axis = sec_axis(~./length(unique(d$participant)), name = "proportion 'go'"), expand = c(0,0))+
  scale_x_continuous(expand = c(0,0))+
  stat_summary(aes(x=trial.cond, y=response),fun.y=function(y) { mean(y)*length(unique(d$participant)) },geom="line",color="red")+
  facet_grid(session~card_type)+
  scale_fill_manual(values=c("white","grey"))+
  labs(y="subj number")+
  theme(
    panel.background = element_rect(fill = "lightblue",
                                    colour = "lightblue",
                                    size = 0.5, linetype = "solid"),
    panel.grid.major = element_blank(), panel.grid.minor = element_blank())
ggsave(plot.filename("fancydescr.png", bname), width=12, height=8)


smoothit <- function(x, win=5){
  n=length(x)
  y=vector(length=n)
  for( i in 1:n ){
    y[i]=mean(x[max(1,i-win):i])
  }
  return(y);
}

d %>% group_by(participant, session, card_type) %>%
  mutate(trial.card=1:n()) %>%
  ungroup %>%
  group_by(session, card_type, trial.card) %>%
  summarise(pgo=mean(response)) %>%
  group_by(session,card_type) %>%
  mutate(spgo=smoothit(pgo,win=5)) %>%
  ungroup %>% gather(var,prob, pgo,spgo) %>%
  mutate(session=str_sub(session,3)) %>%
  mutate(session=fct_recode(session, AM="amp", Peak="peak", Control="cntrl",Training="trng", Trough="trough"))-> d.pgo

d.pgo %>%
  ggplot(aes(trial.card,prob,color=card_type))+
  geom_line()+
  facet_grid(var~session)#,ncol=5)
ggsave(plot.filename("pgo_session_smooth.png", bname), width=10, height=5)


##
## PAPER PLOT
##
conds=make_conditions(d, vars=c("session"))
me2=marginal_effects(mod, effects="ztrial:card_type", conditions=conds,  plot=F)

use.trials=unique(me2$`ztrial:card_type`$ztrial)[seq(1,100,5)]

me2$`ztrial:card_type` %>%
  mutate(pgo=if_else(card_type %in% c("GoWin", "GoAvo"), estimate__, 1-estimate__),
         pgo.lower=if_else(card_type %in% c("GoWin", "GoAvo"), lower__, 1-lower__),
         pgo.upper=if_else(card_type %in% c("GoWin", "GoAvo"), upper__, 1-upper__)) %>%
  mutate(session=map_chr(str_split(session,"_"), ~ .x[2]),
         session=factor(session, levels=rev(session_labels))) %>%
  filter(ztrial %in% use.trials) %>%
  group_by(session,card_type) %>%
  mutate(trial=rank(ztrial)) %>%
  ungroup() %>%
  mutate(session=fct_recode(session, AM="amp", Peak="peak", Control="cntrl",Training="trng", Trough="trough"),
         var="Model") %>%
  full_join(d.pgo %>% filter(var=="pgo") %>% mutate(pgo=prob, var="Data",trial=trial.card)) %>%
  mutate(session=fct_relevel(session, "Training", "Control")) %>%
  ggplot(aes(y=pgo,x=trial,color=card_type,linetype=var,size=var))+
  geom_line()+
  geom_ribbon(aes(ymin=pgo.lower, ymax=pgo.upper,fill=card_type,color=NULL), alpha=0.15)+
  guides(fill=FALSE,size=FALSE)+
  scale_linetype_manual(values=c("twodash", "solid"))+
  scale_size_manual(values=c(0.8,1))+
  labs(x="Trial", y="P(Go)", color="Card", linetype="")+
  facet_wrap(~ session, ncol=5)#-> p1

ggsave(plot.filename("paper_postpred.png", bname), width=10, height=3, dpi=300)



### summary stuff
cards=card_labels #as.character(unique(d$card_type))
M=cbind(samp, b_sessions_trng=0, 
        `b_card_typeGoWin:sessions_trng`=0, `b_card_typeGoAvo:sessions_trng`=0, `b_card_typeNoGoAvo:sessions_trng`=0,`b_card_typeNoGoWin:sessions_trng`=0,
        `b_card_typeGoWin:sessions_amp`=0, `b_card_typeGoWin:sessions_peak`=0, `b_card_typeGoWin:sessions_trough`=0, `b_card_typeGoWin:sessions_cntrl`=0)


card_to_label=c("GoWin"="Go-to-Win", "NoGoWin"="NoGo-to-Win", "GoAvo"="Go-to-Avoid", "NoGoAvo"="NoGo-to-Avoid")

effs.acc=map_df(cards, function(card){
  cat(card)
  map_df(as.data.frame(t(expand.grid(session_labels, session_labels))), function(x){
    a=as.character(x[1])
    b=as.character(x[2])
    alab=sprintf("b_sessions_%s",a)
    blab=sprintf("b_sessions_%s",b)
    cat(sprintf("a=b_card_type%s:sessions_%s\n",card,a))
    cat(sprintf("b=b_card_type%s:sessions_%s\n",card,b))
    
    aeff=M[,alab]+M[,sprintf("b_card_type%s:sessions_%s",card,a)]
    beff=M[,blab]+M[,sprintf("b_card_type%s:sessions_%s",card,b)]
    
    p=sum(aeff-beff<0)/as.numeric(dim(M)[1])
    
    data.frame(card=card,a=a,b=b,p=p,postmean=mean(aeff-beff), lower=hdi(aeff-beff)[1], upper=hdi(aeff-beff)[2])
  }) %>%
    mutate(a=factor(a, levels=session_labels),
           b=factor(b, levels=session_labels)) -> r
  return(r);
}) 

# accuracy
effs.acc %>% filter(b!="trng", a!=b, a=="cntrl") %>% arrange(b) %>%
  mutate(summary=sprintf("%s: $b=%.2f\\ [%.2f,%.2f], p=%.2f$", card, postmean,lower,upper,p)) 


effs.lr=map_df(card_labels, function(card){
  cat(card)
  map_df(as.data.frame(t(expand.grid(session_labels, session_labels))), function(x){
    a=as.character(x[1])
    b=as.character(x[2])
    
    aeff=M.ia %>% filter(session==a,card_type==card) %>% pull(val)
    beff=M.ia %>% filter(session==b,card_type==card) %>% pull(val)
    
    p=sum(aeff-beff<0)/as.numeric(length(aeff))
    data.frame(card=card,a=a,b=b,p=p,postmean=mean(aeff-beff), lower=hdi(aeff-beff)[1], upper=hdi(aeff-beff)[2])
  }) %>%
    mutate(a=factor(a, levels=session_labels),
           b=factor(b, levels=session_labels)) -> r
  return(r);
})
  
# learning rate
effs.lr %>% filter(b!="trng", a!=b, a=="cntrl") %>% arrange(b) %>%
  mutate(summary=sprintf("%s: $b=%.2f\\ [%.2f,%.2f], p=%.2f$", card, postmean,lower,upper,p)) 

  