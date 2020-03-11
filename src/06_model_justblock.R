##
# only NHG group from Szeged
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
# data preparation in munge

##================================================================================================
# model fitting
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
  mcmc_trace(modm[,,p]) %>% print
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

#mcmc_areas_ridges(modm, regex_pars="eff_.*_tacs")+geom_vline(xintercept = 0)+ggtitle(bname)
#ggsave(filename = plot.filename("effects_tacs.pdf", base=bname))




## effects

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
