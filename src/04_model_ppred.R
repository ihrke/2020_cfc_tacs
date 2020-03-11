##================================================================================================
# posterior predictive


## posterior predictive for pGo for each real subjects (ignoring group-level distribution)
get.ppred.pgo.subj <- function(nrep){
  initV=rep(0,4)
  #mu_p=extract(mod, "mu_p")[[1]]
  #nsamp=dim(mu_p)[1]
  attach(data.stan)
  
  ppred=NULL
  
  beta_s = extract(mod, "beta")[[1]]
  ep_s = extract(mod, "ep")[[1]]
  pi_s = extract(mod, "pi")[[1]]
  b_s =  extract(mod, "b")[[1]]
  nsamp=dim(ep_s)[1]
  
  for( k in 1:nrep ){
    cat(".")
    ix=sample(1:nsamp, 1)
    beta=beta_s[ix,,]
    ep=ep_s[ix,,]
    pi=pi_s[ix,,]
    b=b_s[ix,,]

    rdf = array(dim = c(N,nblocks,T/4,4))  
    sim.outcome=array(data=0, dim=c(N,nblocks,T))
    #pGo_sum=array(0, dim=c(N, T/4, 4))
    pGo=array(0, dim=c(N,nblocks,T/4,4))
    
    for( i in 1:N){
      for( j in 1:nblocks){
        wv_g  = initV;
        wv_ng = initV;
        qv_g  = initV;
        qv_ng = initV;
        sv    = initV;
        
        ctrial=rep(0,4)
        for (t in 1:T)  {
          ctrial[ cue[i,j,t] ] = ctrial[ cue[i,j,t] ]+1 # trial counter per card_type
          
          
          wv_g[ cue[i,j,t] ]  = qv_g[ cue[i,j,t] ] + sv[ cue[i,j,t] ] * (pi[i,j]) + b[i,j];
          wv_ng[ cue[i,j,t] ] = qv_ng[ cue[i,j,t] ];  # qv_ng is always equal to wv_ng (regardless of action) 
          current.pGo=boot::inv.logit( (wv_g[ cue[i,j,t] ] - wv_ng[ cue[i,j,t] ])/beta[i,j] ); 
          pGo[ i,j,ctrial[cue[i,j,t]], cue[i,j,t] ]   = current.pGo
          
          current.resp=sample(c(0,1), size=1, replace = T, prob = c( 1-current.pGo, current.pGo ) )
          rdf[ i,j,ctrial[cue[i,j,t]], cue[i,j,t] ]   = current.resp
          
          ## update outcome
          # card-type; 1="go_avoid"   2="go_win"     3="nogo_avoid" 4="nogo_win" 
          if(cue[i,j,t]==1){ # go-avoid
            pwin=ifelse( current.resp, 0.65, 0.35)
            sim.outcome[i,j,t]=sample(c(-10,0), 1, prob=c(1-pwin, pwin))
          } else if(cue[i,j,t]==2){ # go-win
            pwin=ifelse( current.resp, 0.65, 0.35)
            sim.outcome[i,j,t]=sample(c(0,10), 1, prob=c(1-pwin, pwin))
          } else if(cue[i,j,t]==3){ # nogo-avoid
            pwin=ifelse( current.resp, 0.35, 0.65)
            sim.outcome[i,j,t]=sample(c(-10,0), 1, prob=c(1-pwin, pwin))
          } else if(cue[i,j,t]==4){ # nogo-win
            pwin=ifelse( current.resp, 0.35, 0.65)
            sim.outcome[i,j,t]=sample(c(0,10), 1, prob=c(1-pwin, pwin))
          }
          if(current.resp){
            # go-cost
            sim.outcome[i,j,t] = sim.outcome[i,j,t]-1
          }
          
          # after receiving feedback, update sv[t+1]
          sv[ cue[i,j,t] ] = sv[ cue[i,j,t] ] + ep[i,j] * ( sim.outcome[i,j,t] - sv[ cue[i,j,t] ] );
          
          # update action values
          if (current.resp) { # update go value 
            qv_g[ cue[i,j,t] ]  = qv_g[ cue[i,j,t] ] + ep[i,j] * (sim.outcome[i,j,t] - qv_g[ cue[i,j,t] ]);
          } else { # update no-go value
            qv_ng[ cue[i,j,t] ] = qv_ng[ cue[i,j,t] ] + ep[i,j] * (sim.outcome[i,j,t] - qv_ng[ cue[i,j,t] ]);  
          }  
        } # end of t loop (T trials)
      } # end of j loop (nblocks)
    } # end of i loop (N subjects)  
    
    #pGo_sum = pGo_sum
    responses=as.data.frame.table(rdf)[,5]
    as.data.frame.table(pGo) %>%
      setNames(c("subj", "session","card_trial", "card_type", "pGo")) %>%
      mutate(k=k,
             subj=as.integer(subj),
             session=as.integer(session),
             card_trial=as.integer(card_trial),
             card_type=fct_recode(card_type, 
                                  go_avoid="A", go_win="B", 
                                  nogo_avoid="C", nogo_win="D"),
             resp=responses
      ) -> d.tmp
    ppred=rbind(ppred, d.tmp)
  }
  detach("data.stan")
  
  #ppred %>% data.frame %>% 
  #  setNames(c("k","trial","go_avoid", "go_win", "nogo_avoid", "nogo_win")) -> ppred
  
  ppred
}
