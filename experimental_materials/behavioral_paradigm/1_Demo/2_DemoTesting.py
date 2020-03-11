#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.07), April 21, 2016, at 10:37
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
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
expName = 'Demo_Testing'  # from the Builder filename that created this script
expInfo = {}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + expInfo['date']

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

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
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
go = visual.TextStim(win=win, ori=0, name='go',
    text=u'Waiting to start...\r\n',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
funf = visual.TextStim(win=win, ori=0, name='funf',
    text='5',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
vier = visual.TextStim(win=win, ori=0, name='vier',
    text='4',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
drei = visual.TextStim(win=win, ori=0, name='drei',
    text='3',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
zwei = visual.TextStim(win=win, ori=0, name='zwei',
    text='2',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
eins = visual.TextStim(win=win, ori=0, name='eins',
    text='1',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "fix1"
fix1Clock = core.Clock()
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='Das Fadenkreuz',    font='Arial',
    pos=[0, 0.5], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cue_image = visual.ImageStim(win=win, name='cue_image',
    image='stim\\1.png', mask=None,
    ori=0, pos=[-0.3, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='Das Kartenpaar',    font='Arial',
    pos=[0, 0.5], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
image_7 = visual.ImageStim(win=win, name='image_7',
    image='stim\\2.png', mask=None,
    ori=0, pos=[0.3, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)

# Initialize components for Routine "trial2_2"
trial2_2Clock = core.Clock()
image_8 = visual.ImageStim(win=win, name='image_8',
    image='stim\\1.png', mask=None,
    ori=0, pos=[-0.3, 0], size=[0.25, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=0.2,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
image_13 = visual.ImageStim(win=win, name='image_13',
    image='stim\\2.png', mask=None,
    ori=0, pos=[0.3, 0], size=[0.35, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-1.0)
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text='Die Antwort',    font='Arial',
    pos=[0, 0.5], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
mouse_11 = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "fix1"
fix1Clock = core.Clock()
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='Das Fadenkreuz',    font='Arial',
    pos=[0, 0.5], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "blink1_2"
blink1_2Clock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='Blinzeln und schlucken: 3-2-1',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='Blinzeln und schlucken',    font='Arial',
    pos=[0, 0.5], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Ende der Presentation. ',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
# keep track of which components have finished
startComponents = []
startComponents.append(go)
startComponents.append(mouse)
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
    
    # *go* updates
    if t >= 0.0 and go.status == NOT_STARTED:
        # keep track of start time/frame for later
        go.tStart = t  # underestimates by a little under one frame
        go.frameNStart = frameN  # exact frame index
        go.setAutoDraw(True)
    # *mouse* updates
    if t >= 0.0 and mouse.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse.tStart = t  # underestimates by a little under one frame
        mouse.frameNStart = frameN  # exact frame index
        mouse.status = STARTED
        event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
    if mouse.status == STARTED:  # only update if started and not stopped!
        buttons = mouse.getPressed()
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
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = []
fixationComponents.append(funf)
fixationComponents.append(vier)
fixationComponents.append(drei)
fixationComponents.append(zwei)
fixationComponents.append(eins)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *funf* updates
    if t >= 0.0 and funf.status == NOT_STARTED:
        # keep track of start time/frame for later
        funf.tStart = t  # underestimates by a little under one frame
        funf.frameNStart = frameN  # exact frame index
        funf.setAutoDraw(True)
    if funf.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        funf.setAutoDraw(False)
    
    # *vier* updates
    if t >= 1.0 and vier.status == NOT_STARTED:
        # keep track of start time/frame for later
        vier.tStart = t  # underestimates by a little under one frame
        vier.frameNStart = frameN  # exact frame index
        vier.setAutoDraw(True)
    if vier.status == STARTED and t >= (1.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        vier.setAutoDraw(False)
    
    # *drei* updates
    if t >= 2.0 and drei.status == NOT_STARTED:
        # keep track of start time/frame for later
        drei.tStart = t  # underestimates by a little under one frame
        drei.frameNStart = frameN  # exact frame index
        drei.setAutoDraw(True)
    if drei.status == STARTED and t >= (2.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        drei.setAutoDraw(False)
    
    # *zwei* updates
    if t >= 3.0 and zwei.status == NOT_STARTED:
        # keep track of start time/frame for later
        zwei.tStart = t  # underestimates by a little under one frame
        zwei.frameNStart = frameN  # exact frame index
        zwei.setAutoDraw(True)
    if zwei.status == STARTED and t >= (3.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        zwei.setAutoDraw(False)
    
    # *eins* updates
    if t >= 4.0 and eins.status == NOT_STARTED:
        # keep track of start time/frame for later
        eins.tStart = t  # underestimates by a little under one frame
        eins.frameNStart = frameN  # exact frame index
        eins.setAutoDraw(True)
    if eins.status == STARTED and t >= (4.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        eins.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    #------Prepare to start Routine "fix1"-------
    t = 0
    fix1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_9
    # keep track of which components have finished
    fix1Components = []
    fix1Components.append(text_10)
    fix1Components.append(mouse_9)
    fix1Components.append(text_11)
    for thisComponent in fix1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fix1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fix1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        # *mouse_9* updates
        if t >= 0.0 and mouse_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_9.tStart = t  # underestimates by a little under one frame
            mouse_9.frameNStart = frameN  # exact frame index
            mouse_9.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse_9.status == STARTED:  # only update if started and not stopped!
            buttons = mouse_9.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fix1"-------
    for thisComponent in fix1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    x, y = mouse_9.getPos()
    buttons = mouse_9.getPressed()
    trials.addData('mouse_9.x', x)
    trials.addData('mouse_9.y', y)
    trials.addData('mouse_9.leftButton', buttons[0])
    trials.addData('mouse_9.midButton', buttons[1])
    trials.addData('mouse_9.rightButton', buttons[2])
    # the Routine "fix1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(cue_image)
    trialComponents.append(mouse_3)
    trialComponents.append(text_3)
    trialComponents.append(image_7)
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
        
        # *cue_image* updates
        if t >= 0.0 and cue_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue_image.tStart = t  # underestimates by a little under one frame
            cue_image.frameNStart = frameN  # exact frame index
            cue_image.setAutoDraw(True)
        # *mouse_3* updates
        if t >= 0.0 and mouse_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_3.tStart = t  # underestimates by a little under one frame
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse_3.status == STARTED:  # only update if started and not stopped!
            buttons = mouse_3.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t  # underestimates by a little under one frame
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        
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
    # store data for trials (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    trials.addData('mouse_3.x', x)
    trials.addData('mouse_3.y', y)
    trials.addData('mouse_3.leftButton', buttons[0])
    trials.addData('mouse_3.midButton', buttons[1])
    trials.addData('mouse_3.rightButton', buttons[2])
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "trial2_2"-------
    t = 0
    trial2_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_11
    # keep track of which components have finished
    trial2_2Components = []
    trial2_2Components.append(image_8)
    trial2_2Components.append(image_13)
    trial2_2Components.append(text_14)
    trial2_2Components.append(mouse_11)
    for thisComponent in trial2_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial2_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trial2_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_8* updates
        if t >= 0.0 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t  # underestimates by a little under one frame
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        
        # *image_13* updates
        if t >= 0.0 and image_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_13.tStart = t  # underestimates by a little under one frame
            image_13.frameNStart = frameN  # exact frame index
            image_13.setAutoDraw(True)
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        # *mouse_11* updates
        if t >= 0.0 and mouse_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_11.tStart = t  # underestimates by a little under one frame
            mouse_11.frameNStart = frameN  # exact frame index
            mouse_11.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse_11.status == STARTED:  # only update if started and not stopped!
            buttons = mouse_11.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial2_2"-------
    for thisComponent in trial2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    x, y = mouse_11.getPos()
    buttons = mouse_11.getPressed()
    trials.addData('mouse_11.x', x)
    trials.addData('mouse_11.y', y)
    trials.addData('mouse_11.leftButton', buttons[0])
    trials.addData('mouse_11.midButton', buttons[1])
    trials.addData('mouse_11.rightButton', buttons[2])
    # the Routine "trial2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "fix1"-------
    t = 0
    fix1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_9
    # keep track of which components have finished
    fix1Components = []
    fix1Components.append(text_10)
    fix1Components.append(mouse_9)
    fix1Components.append(text_11)
    for thisComponent in fix1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fix1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fix1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if t >= 0.0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        # *mouse_9* updates
        if t >= 0.0 and mouse_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_9.tStart = t  # underestimates by a little under one frame
            mouse_9.frameNStart = frameN  # exact frame index
            mouse_9.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse_9.status == STARTED:  # only update if started and not stopped!
            buttons = mouse_9.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fix1"-------
    for thisComponent in fix1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    x, y = mouse_9.getPos()
    buttons = mouse_9.getPressed()
    trials.addData('mouse_9.x', x)
    trials.addData('mouse_9.y', y)
    trials.addData('mouse_9.leftButton', buttons[0])
    trials.addData('mouse_9.midButton', buttons[1])
    trials.addData('mouse_9.rightButton', buttons[2])
    # the Routine "fix1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "blink1_2"-------
    t = 0
    blink1_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_7
    # keep track of which components have finished
    blink1_2Components = []
    blink1_2Components.append(text_8)
    blink1_2Components.append(mouse_7)
    blink1_2Components.append(text_4)
    for thisComponent in blink1_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "blink1_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = blink1_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        # *mouse_7* updates
        if t >= 0.0 and mouse_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_7.tStart = t  # underestimates by a little under one frame
            mouse_7.frameNStart = frameN  # exact frame index
            mouse_7.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse_7.status == STARTED:  # only update if started and not stopped!
            buttons = mouse_7.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blink1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "blink1_2"-------
    for thisComponent in blink1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    x, y = mouse_7.getPos()
    buttons = mouse_7.getPressed()
    trials.addData('mouse_7.x', x)
    trials.addData('mouse_7.y', y)
    trials.addData('mouse_7.leftButton', buttons[0])
    trials.addData('mouse_7.midButton', buttons[1])
    trials.addData('mouse_7.rightButton', buttons[2])
    # the Routine "blink1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text_2)
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
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    if text_2.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)
    
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
