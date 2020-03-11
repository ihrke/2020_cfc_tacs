##
#
#
library(ProjectTemplate)
load.project()
library(bayesplot)
library(tidybayes)  
library(rstan)

theme_set(theme_bw())
options(mc.cores = parallel::detectCores())
rstan_options(auto_write = TRUE)

bname<-tools::file_path_sans_ext(basename(this.file.name()))
#stop()

### MCMC parameters iterations
n.chains=6
n.cores=6
n.iter=2000
n.warmup=1000

##================================================================================================
# prior
#mu_p[1]  ~ normal( -.4, .7);  // ep 
#mu_p[2]  ~ normal(-1.5, .8); // beta
#mu_p[3]  ~ normal(0,   10.0); // pi
#mu_p[4]  ~ normal(0,   10.0); // b

#sigma[1] ~ cauchy(0, .02); // ep
#sigma[2] ~ cauchy(0, .10); // beta
#sigma[3] ~ normal(0, 1.0); // pi
#sigma[4] ~ normal(0, 1.0); // b

library(truncnorm)
library(truncdist)
library(crch)
n=100000
mu.alpha=pnorm(rnorm(n, mean=0, sd=.8)+rtruncnorm(n, mean = 0, sd = 0.5, a=0)*rnorm(n))
mu.beta=exp(rnorm(n,0,0.5) + rtruncnorm(n,mean=0,sd=1,a=0)*rnorm(n))

pdf(plot.filename("prior.pdf",bname), width = 10,height = 5)
par(mfrow=c(1,2))
plot(density(mu.alpha))
plot(density(mu.beta),xlim=c(0,100))
dev.off()

##================================================================================================
# model fitting
data.stan$sample_prior=0
if(!is.cached.var("mod", base=bname)){
  mod = stan(file=sprintf("src/%s.stan", bname), data = data.stan, cores=n.cores, chains = n.chains, iter = n.iter, warmup = n.warmup, init = 0 )
  cache.var("mod", bname)
} else {
  mod <- load.cache.var("mod",bname)
}

#stop()
##================================================================================================
## diagnostics
pdf(file=plot.filename("diagnostics.pdf", base=bname), onefile=TRUE)
mcmc_rhat(rhat(mod)) %>% print
mcmc_neff(neff_ratio(mod)) %>% print
npages=50
modm = as.array(mod)
nvar=dim(modm)[3]
for(p in split(1:nvar, ceiling(seq_along(1:nvar)/(nvar/npages)))){
  cat(".")
#  mcmc_trace(modm[,,p]) %>% print
}
dev.off()


##================================================================================================
# parameters

## group-level
modm=as.array(mod)
mcmc_areas_ridges(modm, pars=c("mu_ep", "mu_beta", "mu_pi", "mu_b"))+ggtitle(bname)
ggsave(filename = plot.filename("grouppars.pdf", base=bname))

mcmc_areas_ridges(modm, regex_pars="eff_.*_block")+geom_vline(xintercept = 0)+ggtitle(bname)
ggsave(filename = plot.filename("effects_block.pdf", base=bname))

mcmc_areas_ridges(modm, regex_pars="eff_.*_tacs")+geom_vline(xintercept = 0)+ggtitle(bname)
ggsave(filename = plot.filename("effects_tacs.pdf", base=bname))




## effects

tacs_labels=c("training", "control", "peak", "trough", "amp")

mod %>% gather_draws(eff_ep_tacs[tacs], eff_beta_tacs[tacs], eff_pi_tacs[tacs], eff_b_tacs[tacs]) %>%
  ungroup %>%
  mutate(tacs=factor(tacs, levels=seq(1,5), labels=tacs_labels)) -> d.eff

d.eff %>% ungroup %>% group_by(.variable, tacs) %>%
  nest() %>%
  mutate(summary=map(data, ~mean_hdi(.$.value))) %>%
  select(-data) %>%
  unnest %>%
  data.frame
#summarise()

d.eff %>%
  ggplot(aes(x=.value, y=tacs))+  
  geom_halfeyeh(fun.data=mean_hdih, .prob = c(.05, .95))+
  geom_vline(xintercept = 0)+
  facet_wrap(~.variable, scales="free")+ggtitle(bname)
ggsave(plot.filename("effects_tacs.pdf", bname), width=12,height=6)


mod %>% gather_draws(eff_ep_block[block], eff_beta_block[block], eff_pi_block[block], eff_b_block[block]) %>%
  ungroup %>%
  mutate(block=factor(block, levels=seq(1,5), labels=seq(1,5))) -> d.eff.block

d.eff.block %>%
  ggplot(aes(x=.value, y=block))+  
  geom_halfeyeh(fun.data=mean_hdih, .prob = c(.05, .95))+
  geom_vline(xintercept = 0)+
  facet_wrap(~.variable, scales="free")+ggtitle(bname)
ggsave(plot.filename("effects_block.pdf", bname), width=12,height=6)


## group-level
mcmc_areas_ridges(modm, regex_pars="sigma")
ggsave(filename = plot.filename("grouppars_sigma.pdf", base=bname))

##================================================================================================
# model-selection


##================================================================================================
# postpred

extract=rstan::extract
source(sprintf("src/%s_ppred.R", bname))

nrep=1000

if(!is.cached.var("ppred.subj", base=bname)){
  ppred.subj <- get.ppred.pgo.subj(nrep)
  cache.var("ppred.subj", bname)
} else {
  ppred.subj <- load.cache.var("ppred.subj",bname)
}

ppred.subj %>% group_by(subj,session,card_type,card_trial) %>%
  summarise(mean=mean(pGo), lower=hdi(pGo)[1], upper=hdi(pGo)[2]) -> d.ppred

session.labels=c("s_trng", "s_cntrl", "s_peak", "s_trough", "s_amp")

learn %>% group_by(participant, session,card_type) %>%
  mutate(card_trial=1:n()) %>% 
  ungroup %>%
  group_by(session,card_type,card_trial) %>%
  summarise(mean=mean(response)) -> d.real

d.ppred %>% ungroup %>% 
  mutate(session=factor(session, levels=1:5, labels=session.labels),
         card_type=fct_recode(card_type, GoWin="go_win", GoAvo="go_avoid",
                              NoGoAvo="nogo_avoid", NoGoWin="nogo_win")) %>%
  ggplot(aes(card_trial, mean,color=card_type, fill=card_type))+
  stat_summary(fun.data=mean_qi, geom="ribbon", color=NA, alpha=0.1)+
  stat_summary(fun.y=mean, geom="line", size=2)+
  geom_line(data=d.real)+
  facet_wrap(~session)
ggsave(plot.filename("ppred_sessions.pdf",bname), width=10,height=6)
