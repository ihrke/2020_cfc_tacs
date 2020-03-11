data {
  int<lower=1> N; // num subj
  int<lower=1> nblocks; // number of blocks including the baseline block
  int<lower=1> T; // num trials per block
  real outcome[N, nblocks, T]; // reward?
  int<lower=0, upper=1> pressed[N, nblocks, T];  //  1-go, 0-nogo
  int<lower=1, upper=4> cue[N, nblocks, T]; // card-type; 1="go_avoid"   2="go_win"     3="nogo_avoid" 4="nogo_win" 
  int<lower=1, upper=5> tacs[N,nblocks]; // 1=baseline, 2=control, 3=cfc-peak, 4=cfc-trough, 5=cfc-amp
  int<lower=1, upper=5> sorder[N,nblocks]; // order of the blocks for each subject (always baseline==1)
}
transformed data {
  vector[4] initV;
  initV  = rep_vector(0.0, 4);
}
parameters {
  // declare as vectors for vectorizing
  vector[4] mu_p;  
  vector<lower=0>[4] sigma; 
  
  vector[N] ep_pr;          // learning rate 
  vector[N] beta_pr;         // beta, inv temp 
  vector[N] pi_pr;         // pavlovian bias 
  vector[N] b_pr;           // go-bias

  vector[nblocks-1] eff_ep_block_pr; // learning effects (sorder)
  vector[nblocks-1] eff_beta_block_pr; 
  vector[nblocks-1] eff_pi_block_pr; 
  vector[nblocks-1] eff_b_block_pr; 
  /*
  vector[nblocks-1] eff_ep_tacs_pr; // tacs effect
  vector[nblocks-1] eff_beta_tacs_pr; 
  vector[nblocks-1] eff_pi_tacs_pr; 
  vector[nblocks-1] eff_b_tacs_pr; */
}

transformed parameters{
  matrix<lower=0,upper=1>[N,nblocks] ep;
  matrix<lower=0>[N,nblocks] beta;
  matrix[N,nblocks] pi;
  matrix[N,nblocks] b;

  vector[nblocks] eff_ep_block; // learning effects (sorder)
  vector[nblocks] eff_beta_block; 
  vector[nblocks] eff_pi_block; 
  vector[nblocks] eff_b_block; 
  
  /*
  vector[nblocks] eff_ep_tacs; // tacs effect
  vector[nblocks] eff_beta_tacs; 
  vector[nblocks] eff_pi_tacs; 
  vector[nblocks] eff_b_tacs;   */

  eff_ep_block[1]=0;
  eff_beta_block[1]=0;
  eff_pi_block[1]=0;
  eff_b_block[1]=0;

/*
  eff_ep_tacs[1]=0;
  eff_beta_tacs[1]=0;
  eff_pi_tacs[1]=0;
  eff_b_tacs[1]=0;*/

  for( j in 2:nblocks){
    eff_ep_block[j]=eff_ep_block_pr[j-1];
    eff_beta_block[j]=eff_beta_block_pr[j-1];
    eff_pi_block[j]=eff_pi_block_pr[j-1];
    eff_b_block[j]=eff_b_block_pr[j-1];
    /*
    eff_ep_tacs[j]=eff_ep_tacs_pr[j-1];
    eff_beta_tacs[j]=eff_beta_tacs_pr[j-1];
    eff_pi_tacs[j]=eff_pi_tacs_pr[j-1];
    eff_b_tacs[j]=eff_b_tacs_pr[j-1];*/
  }
  

  for (i in 1:N) {
    for( j in 1:nblocks){
      ep[i,j]  = Phi_approx( mu_p[1] + eff_ep_block[sorder[i,j]] + sigma[1] * ep_pr[i] );
      beta[i,j]= exp( mu_p[2] + eff_beta_block[sorder[i,j]] + sigma[2] * beta_pr[i] );
      pi[i,j]  = mu_p[3] + eff_pi_block[sorder[i,j]] + sigma[3] * pi_pr[i];
      b[i,j]   = mu_p[4] + eff_b_block[sorder[i,j]] + sigma[4] * b_pr[i];
    }
  }
}
model {  
  // gng_m1: RW + noise model in Guitart-Masip et al 2012
  // hyper parameters
  mu_p[1]  ~ normal( -.4, .7);  // ep 
  mu_p[2]  ~ normal(-1.5, .8); // beta
  mu_p[3]  ~ normal(0,   1.0); // pi
  mu_p[4]  ~ normal(0,   1.0); // b

  sigma[1] ~ cauchy(0, .02); // ep
  sigma[2] ~ cauchy(0, .10); // beta
  sigma[3] ~ normal(0, 1.0); // pi
  sigma[4] ~ normal(0, 1.0); // b

  // prior on block effects
  eff_ep_block_pr ~ normal(0,1);
  eff_beta_block_pr ~ normal(0,1);
  eff_pi_block_pr ~ normal(0,1);
  eff_b_block_pr ~ normal(0,1);

/*
  eff_ep_tacs_pr ~ normal(0,1);
  eff_beta_tacs_pr ~ normal(0,1);
  eff_pi_tacs_pr ~ normal(0,1);
  eff_b_tacs_pr ~ normal(0,1);
*/

  // individual parameters w/ Matt trick, see https://groups.google.com/forum///!msg/stan-users/4gv3fNCqSNk/J6ZItL2ZJ-IJ
  ep_pr  ~ normal(0, 1.0);   
  beta_pr ~ normal(0, 1.0);
  pi_pr  ~ normal(0, 1.0); 
  b_pr  ~ normal(0, 1.0); 

  for (i in 1:N) {
    vector[4] wv_g;  // action weigth for go
    vector[4] wv_ng; // action weigth for nogo
    vector[4] qv_g;  // Q value for go
    vector[4] qv_ng; // Q value for nogo
    vector[4] pGo;   // prob of go (press) 
    vector[4] sv;    // stimulus value 

    for( j in 1:nblocks){
      wv_g  = initV;
      wv_ng = initV;
      qv_g  = initV;
      qv_ng = initV;
      sv    = initV;

      for (t in 1:T)  {
        wv_g[ cue[i,j,t] ]  = qv_g[ cue[i,j,t] ] + sv[ cue[i,j,t] ] * pi[i,j]+ b[i,j];
        wv_ng[ cue[i,j,t] ] = qv_ng[ cue[i,j,t] ];  // qv_ng is always equal to wv_ng (regardless of action)      
        
        pGo[ cue[i,j,t] ]   = inv_logit( (wv_g[ cue[i,j,t] ] - wv_ng[ cue[i,j,t] ])/beta[i,j] ); 
        pressed[i,j,t] ~ bernoulli( pGo[ cue[i,j,t] ] );
        
        // after receiving feedback, update sv[t+1]
        sv[ cue[i,j,t] ] = sv[ cue[i,j,t] ] + ep[i,j] * ( outcome[i,j,t] - sv[ cue[i,j,t] ] );

        // update action values
        if (pressed[i,j,t]) { // update go value 
            qv_g[ cue[i,j,t] ]  = qv_g[ cue[i,j,t] ] + ep[i,j] * (outcome[i,j,t] - qv_g[ cue[i,j,t] ]);
        } else { // update no-go value
            qv_ng[ cue[i,j,t] ] = qv_ng[ cue[i,j,t] ] + ep[i,j] * (outcome[i,j,t] - qv_ng[ cue[i,j,t] ]);  
        }  
      } // end of t loop (T trials)
    } // end of j loop (nblocks blocks)
  } // end of i loop (N subjects)
}


generated quantities {
  real<lower=0, upper=1> mu_ep;
  real<lower=0> mu_beta;
  real mu_pi;
  real mu_b;
  real log_lik[N];
  
  mu_ep  = Phi_approx(mu_p[1]);
  mu_beta = exp(mu_p[2]);
  mu_pi = mu_p[3];
  mu_b = mu_p[4];

  { // local section, this saves time and space
    for (i in 1:N) {
      vector[4] wv_g;  // action wegith for go
      vector[4] wv_ng; // action wegith for nogo
      vector[4] qv_g;  // Q value for go
      vector[4] qv_ng; // Q value for nogo
      vector[4] pGo;   // prob of go (press) 
      vector[4] sv;    // stimulus value 

      log_lik[i] = 0;
      
      for( j in 1:nblocks){
        wv_g  = initV;
        wv_ng = initV;
        qv_g  = initV;
        qv_ng = initV;
        sv    = initV;
        
        for (t in 1:T)  {
          wv_g[ cue[i,j,t] ]  = qv_g[ cue[i,j,t] ] + sv[ cue[i,j,t] ] * pi[i,j] + b[i,j];
          wv_ng[ cue[i,j,t] ] = qv_ng[ cue[i,j,t] ];  // qv_ng is always equal to wv_ng (regardless of action)      
          
          pGo[ cue[i,j,t] ]   = inv_logit( (wv_g[ cue[i,j,t] ] - wv_ng[ cue[i,j,t] ])/beta[i,j] ); 
          log_lik[i] = log_lik[i] + bernoulli_lpmf( pressed[i,j,t] | pGo[ cue[i,j,t] ] );
  
          // after receiving feedback, update sv[t+1]
            sv[ cue[i,j,t] ] = sv[ cue[i,j,t] ] + ep[i,j] * ( outcome[i,j,t] - sv[ cue[i,j,t] ] );

          // update action values
         if (pressed[i,j,t]) { // update go value 
            qv_g[ cue[i,j,t] ]  = qv_g[ cue[i,j,t] ] + ep[i,j] * (outcome[i,j,t] - qv_g[ cue[i,j,t] ]);
          } else { // update no-go value
            qv_ng[ cue[i,j,t] ] = qv_ng[ cue[i,j,t] ] + ep[i,j] * (outcome[i,j,t] - qv_ng[ cue[i,j,t] ]);  
          } 
        } // end of t loop (T trials)        
        
      } // end of j loop
    } // end of i loop
  } // end of local section
}  
