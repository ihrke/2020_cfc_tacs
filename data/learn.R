# participant-info within files may be wrong, use filenames!
# 

sessions=c("s_trng", "s_cntrl", "s_peak", "s_trough", "s_amp")

map_df(sessions, function(session){
  dpath<-file.path('data','raw','1_learning', session)
  fnames<-list.files(dpath,pattern="*.csv")
  
  map_df(fnames, function(fname){
    read.table(file.path(dpath,fname),header=T,sep=",") %>%
      select(participant=participant,accuracy=buttonBox_Response.corr,button=buttonBox_Response.keys, 
             reaction_time=buttonBox_Response.rt,
             card_type=cType,corr_fb=cFback,icorr_fb=icFback,cue=cue) %>%
      slice(2:n()) %>% ## dropping first "weird" row
      mutate(participant=as.integer(strsplit(fname,'_')[[1]][2]),
             card_type=droplevels(card_type),
             corr_fb=droplevels(corr_fb),
             icorr_fb=droplevels(icorr_fb),
             cue=as.character(droplevels(cue)),
             correct.response=factor(ifelse(card_type=="GoWin" | card_type=="GoAvo","Approach","Avoid")),
             session=session,
             trial=1:n(),
             sorder_fname=as.integer(strsplit(fname,"_")[[1]][4]),
             year=as.integer(strsplit(fname,'_')[[1]][8]),
             month=strsplit(fname,'_')[[1]][9],
             day=as.integer(strsplit(fname,'_')[[1]][10])) -> d
    return(d)
  })  -> d.session
  return(d.session)
}) %>%
  mutate(participant=factor(participant),
         cue=factor(cue),
         correct.response=factor(correct.response),
         session=factor(session),
          month=as.integer(factor(month,levels=c("Feb","Mrz","Apr","Mai","Jun","Jul")))+1,
         date=ymd(sprintf('%04d%02d%02d',year,month,day))) -> learn

learn %>% arrange(participant,date,trial) %>%
  group_by(participant) %>%
  mutate(sorder=rep(1:5,each=max(trial))) %>%
  ungroup -> learn


unit.reward=1
learn %>% group_by(participant,session) %>%
  mutate(trial.session=1:n()) %>%
  mutate(corr_fb=case_when(str_detect(corr_fb, "Neg") ~ -unit.reward,
                           str_detect(corr_fb, "Neu") ~ 0,
                           str_detect(corr_fb, "Pos") ~ unit.reward),
         icorr_fb=case_when(str_detect(icorr_fb, "Neg") ~ -unit.reward,
                            str_detect(icorr_fb, "Neu") ~ 0,
                            str_detect(icorr_fb, "Pos") ~ unit.reward),
         reward=if_else(accuracy==1, corr_fb, icorr_fb),
         correct.response=if_else(correct.response=="Approach", 1, 0),
         response=if_else(is.na(reaction_time),0,1),
         card_type_int=case_when(card_type=="GoAvo" ~ 1,
                                 card_type=="GoWin" ~ 2,
                                 card_type=="NoGoAvo" ~ 3,
                                 card_type=="NoGoWin" ~ 4),
         tacs_int=case_when(session=="s_trng" ~ 1,
                            session=="s_cntrl" ~ 2,
                            session=="s_peak" ~ 3,
                            session=="s_trough" ~ 4,
                            session=="s_amp" ~ 5)) %>%
  arrange(participant, sorder, trial.session) -> learn

