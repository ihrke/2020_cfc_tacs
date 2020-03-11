#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.01), April 21, 2016, at 09:37
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui, parallel, hardware
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'PracticeLearning'  # from the Builder filename that created this script
expInfo = {u'session': u'p', u'participant': u'p'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s_%s' %('P',expInfo['participant'], 'S',expInfo['session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
import pyxid #to use the Cedrus response box

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "start"
startClock = core.Clock()
textStart = visual.TextStim(win=win, ori=0, name='textStart',
    text=u'Waiting to start...',    font=u'Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
mouseStart = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "countback"
countbackClock = core.Clock()
textFive = visual.TextStim(win=win, ori=0, name='textFive',
    text='5',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
textFour = visual.TextStim(win=win, ori=0, name='textFour',
    text='4',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
textThree = visual.TextStim(win=win, ori=0, name='textThree',
    text='3',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
textTwo = visual.TextStim(win=win, ori=0, name='textTwo',
    text='2',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
textOne = visual.TextStim(win=win, ori=0, name='textOne',
    text='1',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
textStimulation = visual.TextStim(win=win, ori=0, name='textStimulation',
    text=u'Blinzeln und schlucken.',    font=u'Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
textPreCue = visual.TextStim(win=win, ori=0, name='textPreCue',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
p_port = parallel.ParallelPort(address=u'0xE010')

# Initialize components for Routine "trial"
trialClock = core.Clock()
imageCard = visual.ImageStim(win=win, name='imageCard',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
textPrepResponse = visual.TextStim(win=win, ori=0, name='textPrepResponse',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
p_port_cue = parallel.ParallelPort(address=u'0xE010')

# Initialize components for Routine "circle"
circleClock = core.Clock()
imageCircle = visual.ImageStim(win=win, name='imageCircle',
    image=u'circle.png', mask=None,
    ori=0, pos=[0, 0], size=[0.35, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
p_port_circle = parallel.ParallelPort(address=u'0xE010')
for n in range(10): #Cedrus connection doesn't always work first time!
    try:
        devices = pyxid.get_xid_devices()
        core.wait(0.1)
        buttonBox_Response = devices[0]
        break #once we found the device we can break the loop
    except:
        pass
buttonBox_Response.status = NOT_STARTED
buttonBox_Response.clock = core.Clock()

# Initialize components for Routine "response"
responseClock = core.Clock()
textPreFback = visual.TextStim(win=win, ori=0, name='textPreFback',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
p_port_response = parallel.ParallelPort(address=u'0xE010')

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
imageFeedback = visual.ImageStim(win=win, name='imageFeedback',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.6, 0.4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
p_port_feedback = parallel.ParallelPort(address=u'0xE010')

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
textBaseline = visual.TextStim(win=win, ori=0, name='textBaseline',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
p_port_bline = parallel.ParallelPort(address='0xE010')

# Initialize components for Routine "end"
endClock = core.Clock()
textEnd = visual.TextStim(win=win, ori=0, name='textEnd',
    text=u'Ende der Aufgabe.',    font=u'Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# setup some python lists for storing info about the mouseStart
# keep track of which components have finished
startComponents = []
startComponents.append(textStart)
startComponents.append(mouseStart)
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "start"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textStart* updates
    if t >= 0.0 and textStart.status == NOT_STARTED:
        # keep track of start time/frame for later
        textStart.tStart = t  # underestimates by a little under one frame
        textStart.frameNStart = frameN  # exact frame index
        textStart.setAutoDraw(True)
    # *mouseStart* updates
    if t >= 0.0 and mouseStart.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouseStart.tStart = t  # underestimates by a little under one frame
        mouseStart.frameNStart = frameN  # exact frame index
        mouseStart.status = STARTED
        event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
    if mouseStart.status == STARTED:  # only update if started and not stopped!
        buttons = mouseStart.getPressed()
        if sum(buttons) > 0:  # ie if any button is pressed
            # abort routine on response
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "countback"-------
t = 0
countbackClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
countbackComponents = []
countbackComponents.append(textFive)
countbackComponents.append(textFour)
countbackComponents.append(textThree)
countbackComponents.append(textTwo)
countbackComponents.append(textOne)
for thisComponent in countbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "countback"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = countbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textFive* updates
    if t >= 0.0 and textFive.status == NOT_STARTED:
        # keep track of start time/frame for later
        textFive.tStart = t  # underestimates by a little under one frame
        textFive.frameNStart = frameN  # exact frame index
        textFive.setAutoDraw(True)
    if textFive.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        textFive.setAutoDraw(False)
    
    # *textFour* updates
    if t >= 1.0 and textFour.status == NOT_STARTED:
        # keep track of start time/frame for later
        textFour.tStart = t  # underestimates by a little under one frame
        textFour.frameNStart = frameN  # exact frame index
        textFour.setAutoDraw(True)
    if textFour.status == STARTED and t >= (1.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        textFour.setAutoDraw(False)
    
    # *textThree* updates
    if t >= 2.0 and textThree.status == NOT_STARTED:
        # keep track of start time/frame for later
        textThree.tStart = t  # underestimates by a little under one frame
        textThree.frameNStart = frameN  # exact frame index
        textThree.setAutoDraw(True)
    if textThree.status == STARTED and t >= (2.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        textThree.setAutoDraw(False)
    
    # *textTwo* updates
    if t >= 3.0 and textTwo.status == NOT_STARTED:
        # keep track of start time/frame for later
        textTwo.tStart = t  # underestimates by a little under one frame
        textTwo.frameNStart = frameN  # exact frame index
        textTwo.setAutoDraw(True)
    if textTwo.status == STARTED and t >= (3.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        textTwo.setAutoDraw(False)
    
    # *textOne* updates
    if t >= 4.0 and textOne.status == NOT_STARTED:
        # keep track of start time/frame for later
        textOne.tStart = t  # underestimates by a little under one frame
        textOne.frameNStart = frameN  # exact frame index
        textOne.setAutoDraw(True)
    if textOne.status == STARTED and t >= (4.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        textOne.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "countback"-------
for thisComponent in countbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'xlsx\\Practice_Learning_S'+str(expInfo['session'])+'_P'+str(expInfo['participant'])+'.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "pause"-------
    t = 0
    pauseClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = []
    pauseComponents.append(textStimulation)
    pauseComponents.append(textPreCue)
    pauseComponents.append(p_port)
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pause"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textStimulation* updates
        if t >= 0.0 and textStimulation.status == NOT_STARTED:
            # keep track of start time/frame for later
            textStimulation.tStart = t  # underestimates by a little under one frame
            textStimulation.frameNStart = frameN  # exact frame index
            textStimulation.setAutoDraw(True)
        if textStimulation.status == STARTED and t >= (0.0 + (preCueStart-win.monitorFramePeriod*0.75)): #most of one frame period left
            textStimulation.setAutoDraw(False)
        
        # *textPreCue* updates
        if t >= preCueStart and textPreCue.status == NOT_STARTED:
            # keep track of start time/frame for later
            textPreCue.tStart = t  # underestimates by a little under one frame
            textPreCue.frameNStart = frameN  # exact frame index
            textPreCue.setAutoDraw(True)
        if textPreCue.status == STARTED and t >= (preCueStart + (preCueStop-win.monitorFramePeriod*0.75)): #most of one frame period left
            textPreCue.setAutoDraw(False)
        # *p_port* updates
        if t >= 0.0 and p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port.tStart = t  # underestimates by a little under one frame
            p_port.frameNStart = frameN  # exact frame index
            p_port.status = STARTED
            win.callOnFlip(p_port.setData, int(trigStimulator))
        if p_port.status == STARTED and t >= (0.0 + (portStop-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port.status = STOPPED
            win.callOnFlip(p_port.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port.status == STARTED:
        win.callOnFlip(p_port.setData, int(0))
    # the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    imageCard.setImage(cue)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(imageCard)
    trialComponents.append(textPrepResponse)
    trialComponents.append(p_port_cue)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageCard* updates
        if t >= 0.0 and imageCard.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageCard.tStart = t  # underestimates by a little under one frame
            imageCard.frameNStart = frameN  # exact frame index
            imageCard.setAutoDraw(True)
        if imageCard.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageCard.setAutoDraw(False)
        
        # *textPrepResponse* updates
        if t >= 1.0 and textPrepResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            textPrepResponse.tStart = t  # underestimates by a little under one frame
            textPrepResponse.frameNStart = frameN  # exact frame index
            textPrepResponse.setAutoDraw(True)
        if textPrepResponse.status == STARTED and t >= (1.0 + (prepRespStop-win.monitorFramePeriod*0.75)): #most of one frame period left
            textPrepResponse.setAutoDraw(False)
        # *p_port_cue* updates
        if t >= 0.0 and p_port_cue.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_cue.tStart = t  # underestimates by a little under one frame
            p_port_cue.frameNStart = frameN  # exact frame index
            p_port_cue.status = STARTED
            win.callOnFlip(p_port_cue.setData, int(cueMarker))
        if p_port_cue.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port_cue.status = STOPPED
            win.callOnFlip(p_port_cue.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_cue.status == STARTED:
        win.callOnFlip(p_port_cue.setData, int(0))
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "circle"-------
    t = 0
    circleClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    buttonBox_Response.keys = []  # to store response values
    buttonBox_Response.rt = []
    # keep track of which components have finished
    circleComponents = []
    circleComponents.append(imageCircle)
    circleComponents.append(p_port_circle)
    circleComponents.append(buttonBox_Response)
    for thisComponent in circleComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "circle"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = circleClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageCircle* updates
        if t >= 0.0 and imageCircle.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageCircle.tStart = t  # underestimates by a little under one frame
            imageCircle.frameNStart = frameN  # exact frame index
            imageCircle.setAutoDraw(True)
        if imageCircle.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageCircle.setAutoDraw(False)
        # *p_port_circle* updates
        if t >= 0.0 and p_port_circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_circle.tStart = t  # underestimates by a little under one frame
            p_port_circle.frameNStart = frameN  # exact frame index
            p_port_circle.status = STARTED
            win.callOnFlip(p_port_circle.setData, int(circleMarker))
        if p_port_circle.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port_circle.status = STOPPED
            win.callOnFlip(p_port_circle.setData, int(0))
        # *buttonBox_Response* updates
        if t >= 0.0 and buttonBox_Response.status == NOT_STARTED:
            # keep track of start time/frame for later
            buttonBox_Response.tStart = t  # underestimates by a little under one frame
            buttonBox_Response.frameNStart = frameN  # exact frame index
            buttonBox_Response.status = STARTED
            buttonBox_Response.clock.reset()  # now t=0
            # clear buttonBox_Response responses (in a loop - the Cedrus own function doesn't work well)
            buttonBox_Response.poll_for_response()
            while len(buttonBox_Response.response_queue):
                buttonBox_Response.clear_response_queue()
                buttonBox_Response.poll_for_response() #often there are more resps waiting!
        if buttonBox_Response.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            buttonBox_Response.status = STOPPED
        if buttonBox_Response.status == STARTED:
            theseKeys=[]
            theseRTs=[]
            # check for key presses
            buttonBox_Response.poll_for_response()
            while len(buttonBox_Response.response_queue):
                evt = buttonBox_Response.get_next_response()
                if evt['key'] not in [3, None]:
                    continue #we don't care about this key
                if evt['pressed']: #could be extended to examine releases too?
                  theseKeys.append(evt['key'])
                  theseRTs.append(buttonBox_Response.clock.getTime())
                buttonBox_Response.poll_for_response()
            buttonBox_Response.clear_response_queue() # make sure we don't process these evts again
            if len(theseKeys) > 0:  # at least one key was pressed
                if buttonBox_Response.keys == []:  # then this was the first keypress
                    buttonBox_Response.keys = theseKeys[0]  # just the first key pressed
                    buttonBox_Response.rt = theseRTs[0]
                    # was this 'correct'?
                    if (buttonBox_Response.keys == str(cResponse)) or (buttonBox_Response.keys == cResponse):
                        buttonBox_Response.corr = 1
                    else:
                        buttonBox_Response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in circleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "circle"-------
    for thisComponent in circleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_circle.status == STARTED:
        win.callOnFlip(p_port_circle.setData, int(0))
    # check responses
    if buttonBox_Response.keys in ['', [], None]:  # No response was made
       buttonBox_Response.keys=None
       # was no response the correct answer?!
       if str(cResponse).lower() == 'none': buttonBox_Response.corr = 1  # correct non-response
       else: buttonBox_Response.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('buttonBox_Response.keys',buttonBox_Response.keys)
    trials.addData('buttonBox_Response.corr', buttonBox_Response.corr)
    if buttonBox_Response.keys != None:  # we had a response
        trials.addData('buttonBox_Response.rt', buttonBox_Response.rt)
    
    #------Prepare to start Routine "response"-------
    t = 0
    responseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    responseComponents = []
    responseComponents.append(textPreFback)
    responseComponents.append(p_port_response)
    for thisComponent in responseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "response"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = responseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textPreFback* updates
        if t >= 0.0 and textPreFback.status == NOT_STARTED:
            # keep track of start time/frame for later
            textPreFback.tStart = t  # underestimates by a little under one frame
            textPreFback.frameNStart = frameN  # exact frame index
            textPreFback.setAutoDraw(True)
        if textPreFback.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            textPreFback.setAutoDraw(False)
        # *p_port_response* updates
        if t >= 0.0 and p_port_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_response.tStart = t  # underestimates by a little under one frame
            p_port_response.frameNStart = frameN  # exact frame index
            p_port_response.status = STARTED
            if (buttonBox_Response.keys == str(cResponse)) or (buttonBox_Response.keys == cResponse) or str(cResponse).lower() == 'none':
                win.callOnFlip(p_port_response.setData, int(cRespMarker))
            else:
                win.callOnFlip(p_port_response.setData, int(icRespMarker))
        if p_port_response.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port_response.status = STOPPED
            win.callOnFlip(p_port_response.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_response.status == STARTED:
        win.callOnFlip(p_port_response.setData, int(0))
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if (buttonBox_Response.corr == 1):
        imageFeedback.setImage(cFback)
    else:
        imageFeedback.setImage(icFback)
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(imageFeedback)
    feedbackComponents.append(p_port_feedback)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageFeedback* updates
        if t >= 0.0 and imageFeedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageFeedback.tStart = t  # underestimates by a little under one frame
            imageFeedback.frameNStart = frameN  # exact frame index
            imageFeedback.setAutoDraw(True)
        if imageFeedback.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageFeedback.setAutoDraw(False)
        # *p_port_feedback* updates
        if t >= 0.0 and p_port_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_feedback.tStart = t  # underestimates by a little under one frame
            p_port_feedback.frameNStart = frameN  # exact frame index
            p_port_feedback.status = STARTED
            if (buttonBox_Response.corr == 1):
                win.callOnFlip(p_port_feedback.setData, int(cFbackMarker))
            else:
                win.callOnFlip(p_port_feedback.setData, int(icFbackMarker))
        if p_port_feedback.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port_feedback.status = STOPPED
            win.callOnFlip(p_port_feedback.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_feedback.status == STARTED:
        win.callOnFlip(p_port_feedback.setData, int(0))
    
    #------Prepare to start Routine "baseline"-------
    t = 0
    baselineClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    baselineComponents = []
    baselineComponents.append(textBaseline)
    baselineComponents.append(p_port_bline)
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "baseline"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBaseline* updates
        if t >= 0.0 and textBaseline.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBaseline.tStart = t  # underestimates by a little under one frame
            textBaseline.frameNStart = frameN  # exact frame index
            textBaseline.setAutoDraw(True)
        if textBaseline.status == STARTED and t >= (0.0 + (blineStop-win.monitorFramePeriod*0.75)): #most of one frame period left
            textBaseline.setAutoDraw(False)
        # *p_port_bline* updates
        if t >= 0.0 and p_port_bline.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port_bline.tStart = t  # underestimates by a little under one frame
            p_port_bline.frameNStart = frameN  # exact frame index
            p_port_bline.status = STARTED
            win.callOnFlip(p_port_bline.setData, int(20))
        if p_port_bline.status == STARTED and t >= (0.0 + (blineStop-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port_bline.status = STOPPED
            win.callOnFlip(p_port_bline.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if p_port_bline.status == STARTED:
        win.callOnFlip(p_port_bline.setData, int(0))
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(textEnd)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEnd* updates
    if t >= 0.0 and textEnd.status == NOT_STARTED:
        # keep track of start time/frame for later
        textEnd.tStart = t  # underestimates by a little under one frame
        textEnd.frameNStart = frameN  # exact frame index
        textEnd.setAutoDraw(True)
    if textEnd.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        textEnd.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
