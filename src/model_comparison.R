library(ProjectTemplate)
load.project()
library(loo)

get.ics <- function(mod.nums){
  fpath="cache/vars/"
  loos <- list()
  waics=list()
  for(mod.num in mod.nums){
    mod.fname <- list.files(fpath, pattern=sprintf("^%s_.*_mod.RData", mod.num))
    bname=tools::file_path_sans_ext(mod.fname)
    bname=substr(bname, 1, (nchar(bname)-4))
    mod <- load.cache.var("mod",bname)
    loos[[mod.num]] <- loo(extract_log_lik(mod))
    waics[[mod.num]] <- loo::waic(extract_log_lik(mod))
  }
  list(loo=loos,waic=waics)
}

delta.loo <- function(loos){
  mods.ordered<-rev(rownames(compare(x=loos)))
  nmods=length(loos) 
  delta=list()
  for(i in 1:(nmods-1)){
    delta[[sprintf("%s-%s", mods.ordered[i], mods.ordered[i+1])]]<-compare(loos[[ mods.ordered[i] ]], loos[[ mods.ordered[i+1] ]])
  }
  do.call(rbind, delta)
}

ics <- get.ics(c( "04","05","06", "07"))
compare(x=ics$loo)
compare(x=ics$waic)
delta.loo(ics$loo)
delta.loo(ics$waic)

ics$loo

