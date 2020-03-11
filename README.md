# 2020_cfc_tacs
Data, analysis and experimental materials for our paper "Theta-gamma cross-frequency transcranial alternating current stimulation over the peak improves, over the trough impairs cognitive control"

If you want to use this data/analysis in a research publication, please cite [our paper](http://psyarxiv.com).


~~~{bibtex}
@article{Turietal2020,
  author={},
  title={},
  year=2020,
  journal={},
  volume=,
  number=,
  doi=
}
~~~

## Requirements

Analysis are coded in [R](http://r-project.org) and [stan](http://mc-stan.org). Quite a lot R-packages and the [Stan](http://mc-stan.org) are required. 

## Setup

This repository uses the
[ProjectTemplate](http://projecttemplate.net/) directory layout. 

## Data

Raw data is located in `data/raw` and is provided in `.csv` format.

The `.R` scripts located in `data` load the raw files into `R`
workspace under the name of the `R`-file (without the `.R` extension).

**NOTE**: there are also pre-processed exports of all the variables discussed next; those are located under [data/export](data/export). These files have been created by the script [src/export_data.R](src/export_data.R).


The data is structured as follows (refer to [the paper](http://) for
details).

Data from the five different sessions are stored in a single, unified data.frame `learn`.

~~~
> summary(learn)
  participant      accuracy       button     reaction_time     card_type       corr_fb         icorr_fb    
 1      : 400   Min.   :0.0000       :   0   Min.   :0.017   GoAvo  :2400   Min.   :-1.00   Min.   :-1.00  
 2      : 400   1st Qu.:1.0000   3   :5116   1st Qu.:0.267   GoWin  :2400   1st Qu.: 0.00   1st Qu.:-1.00  
 3      : 400   Median :1.0000   None:4484   Median :0.317   NoGoAvo:2400   Median : 0.00   Median : 0.00  
 4      : 400   Mean   :0.7667               Mean   :0.366   NoGoWin:2400   Mean   : 0.15   Mean   :-0.15  
 5      : 400   3rd Qu.:1.0000               3rd Qu.:0.417                  3rd Qu.: 1.00   3rd Qu.: 0.00  
 6      : 400   Max.   :1.0000               Max.   :0.983                  Max.   : 1.00   Max.   : 1.00  
 (Other):7200                                NA's   :4484                                                  
             cue       correct.response     session         trial        sorder_fname        year     
 stim_v05/1.png: 420   Min.   :0.0      s_amp   :1920   Min.   : 1.00   Min.   :1.000   Min.   :2017  
 stim_v05/2.png: 420   1st Qu.:0.0      s_cntrl :1920   1st Qu.:20.75   1st Qu.:2.000   1st Qu.:2017  
 stim_v05/3.png: 420   Median :0.5      s_peak  :1920   Median :40.50   Median :3.000   Median :2017  
 stim_v05/4.png: 420   Mean   :0.5      s_trng  :1920   Mean   :40.50   Mean   :3.067   Mean   :2017  
 stim_v06/1.png: 420   3rd Qu.:1.0      s_trough:1920   3rd Qu.:60.25   3rd Qu.:4.000   3rd Qu.:2017  
 stim_v06/2.png: 420   Max.   :1.0                      Max.   :80.00   Max.   :6.000   Max.   :2017  
 (Other)       :7080                                                                                  
     month            day             date                sorder  trial.session       reward        
 Min.   :2.000   Min.   : 1.00   Min.   :2017-02-03   Min.   :1   Min.   : 1.00   Min.   :-1.00000  
 1st Qu.:3.000   1st Qu.: 8.00   1st Qu.:2017-03-13   1st Qu.:2   1st Qu.:20.75   1st Qu.: 0.00000  
 Median :4.000   Median :14.00   Median :2017-04-04   Median :3   Median :40.50   Median : 0.00000  
 Mean   :3.908   Mean   :15.06   Mean   :2017-04-12   Mean   :3   Mean   :40.50   Mean   : 0.07125  
 3rd Qu.:5.000   3rd Qu.:22.25   3rd Qu.:2017-05-14   3rd Qu.:4   3rd Qu.:60.25   3rd Qu.: 1.00000  
 Max.   :7.000   Max.   :31.00   Max.   :2017-07-05   Max.   :5   Max.   :80.00   Max.   : 1.00000  
                                                                                                    
    response      card_type_int     tacs_int
 Min.   :0.0000   Min.   :1.00   Min.   :1  
 1st Qu.:0.0000   1st Qu.:1.75   1st Qu.:2  
 Median :1.0000   Median :2.50   Median :3  
 Mean   :0.5329   Mean   :2.50   Mean   :3  
 3rd Qu.:1.0000   3rd Qu.:3.25   3rd Qu.:4  
 Max.   :1.0000   Max.   :4.00   Max.   :5 
~~~

Relevant variables are coded as follows:

- `Participant` - number of the participant (consistent across the five sessions)
- `card_type` - factor for which of the four cards was presented
- `session` - factor coding for tACS session
- `trial` - current trial number for each session
- `sorder` - order in which the sessions were presented to each participant
- `reward` - reward received by the subject
- `response` - 0=NoGo, 1=Go
- `accuracy` - accuracy: 1 correct, 0 incorrect, -1 no response


## Analyses

All analyses are located in `src/`. To run the scripts, you need to
have the `ProjecTemplate` package and various other packages
installed.

The first two lines in each file
~~~{R}
library(ProjectTemplate)
load.project()
~~~
convert the raw data into a more convenient format by

1. running the `data/<dataset>.R` file
2. running the preprocessing scripts in `munge`
3. loading the convenience functions in `lib`
