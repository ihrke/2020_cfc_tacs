d <- learn %>%
  filter(!(participant %in% exclude.subjects)) %>%
  droplevels

d %>% group_by(participant,sorder) %>%
  summarise(tacs_int=first(tacs_int),
            sorder_int=first(sorder)) -> d2

d$reward=d$reward*10
data.stan=list(
  N=length(unique(d$participant)),
  nblocks=length(unique(d$session)),
  T=length(unique(d$trial.session)),
  outcome=xtabs(reward ~ participant + sorder+trial.session, data=d),
  pressed=xtabs(response ~ participant + sorder+trial.session, data=d),
  cue=xtabs(card_type_int ~ participant + sorder+trial.session, data=d),
  tacs=xtabs(tacs_int ~ participant + sorder, data=d2),
  sorder=xtabs(sorder_int ~ participant + sorder, data=d2)
)
remove(d)
