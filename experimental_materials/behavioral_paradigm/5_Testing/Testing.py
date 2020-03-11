#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.01), April 21, 2016, at 10:46
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui, hardware, parallel
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
expName = 'Testing'  # from the Builder filename that created this script
expInfo = {u'session': u'', u'participant': u''}
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
    text='Waiting to start...',    font='Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
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

# Initialize components for Routine "prefixation"
prefixationClock = core.Clock()
textPreFixation = visual.TextStim(win=win, ori=0, name='textPreFixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
imageLeft = visual.ImageStim(win=win, name='imageLeft',
    image='sin', mask=None,
    ori=0, pos=[-0.3, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imageRight = visual.ImageStim(win=win, name='imageRight',
    image='sin', mask=None,
    ori=0, pos=[0.3, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
for n in range(10): #Cedrus connection doesn't always work first time!
    try:
        devices = pyxid.get_xid_devices()
        core.wait(0.1)
        buttonBox = devices[0]
        break #once we found the device we can break the loop
    except:
        pass
buttonBox.status = NOT_STARTED
buttonBox.clock = core.Clock()
p_port = parallel.ParallelPort(address=u'0xE010')

# Initialize components for Routine "highlight"
highlightClock = core.Clock()
imageLeftHL = visual.ImageStim(win=win, name='imageLeftHL',
    image='sin', mask=None,
    ori=0, pos=[-0.3, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imageRightHL = visual.ImageStim(win=win, name='imageRightHL',
    image='sin', mask=None,
    ori=0, pos=[0.3, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "blink"
blinkClock = core.Clock()
textBlink3 = visual.TextStim(win=win, ori=0, name='textBlink3',
    text=u'Blinzeln und schlucken: 3',    font=u'Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
textBlink2 = visual.TextStim(win=win, ori=0, name='textBlink2',
    text=u'Blinzeln und schlucken: 2',    font=u'Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
textBlink1 = visual.TextStim(win=win, ori=0, name='textBlink1',
    text=u'Blinzeln und schlucken: 1',    font=u'Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0)

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
trials = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'xlsx\\SPP1665_Testing_S'+str(expInfo['session'])+'_P'+str(expInfo['participant'])+'.xlsx'),
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
    
    #------Prepare to start Routine "prefixation"-------
    t = 0
    prefixationClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    prefixationComponents = []
    prefixationComponents.append(textPreFixation)
    for thisComponent in prefixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prefixation"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prefixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textPreFixation* updates
        if t >= 0.0 and textPreFixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            textPreFixation.tStart = t  # underestimates by a little under one frame
            textPreFixation.frameNStart = frameN  # exact frame index
            textPreFixation.setAutoDraw(True)
        if textPreFixation.status == STARTED and t >= (0.0 + (prefTime-win.monitorFramePeriod*0.75)): #most of one frame period left
            textPreFixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prefixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prefixation"-------
    for thisComponent in prefixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prefixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    imageLeft.setImage(symbol1)
    imageRight.setImage(symbol2)
    buttonBox.keys = []  # to store response values
    buttonBox.rt = []
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(imageLeft)
    trialComponents.append(imageRight)
    trialComponents.append(buttonBox)
    trialComponents.append(p_port)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageLeft* updates
        if t >= 0.0 and imageLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageLeft.tStart = t  # underestimates by a little under one frame
            imageLeft.frameNStart = frameN  # exact frame index
            imageLeft.setAutoDraw(True)
        if imageLeft.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageLeft.setAutoDraw(False)
        
        # *imageRight* updates
        if t >= 0.0 and imageRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageRight.tStart = t  # underestimates by a little under one frame
            imageRight.frameNStart = frameN  # exact frame index
            imageRight.setAutoDraw(True)
        if imageRight.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageRight.setAutoDraw(False)
        # *buttonBox* updates
        if t >= 0.0 and buttonBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            buttonBox.tStart = t  # underestimates by a little under one frame
            buttonBox.frameNStart = frameN  # exact frame index
            buttonBox.status = STARTED
            buttonBox.clock.reset()  # now t=0
            # clear buttonBox responses (in a loop - the Cedrus own function doesn't work well)
            buttonBox.poll_for_response()
            while len(buttonBox.response_queue):
                buttonBox.clear_response_queue()
                buttonBox.poll_for_response() #often there are more resps waiting!
        if buttonBox.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            buttonBox.status = STOPPED
        if buttonBox.status == STARTED:
            theseKeys=[]
            theseRTs=[]
            # check for key presses
            buttonBox.poll_for_response()
            while len(buttonBox.response_queue):
                evt = buttonBox.get_next_response()
                if evt['key'] not in [2, 4]:
                    continue #we don't care about this key
                if evt['pressed']: #could be extended to examine releases too?
                  theseKeys.append(evt['key'])
                  theseRTs.append(buttonBox.clock.getTime())
                buttonBox.poll_for_response()
            buttonBox.clear_response_queue() # make sure we don't process these evts again
            if len(theseKeys) > 0:  # at least one key was pressed
                if buttonBox.keys == []:  # then this was the first keypress
                    buttonBox.keys = theseKeys[0]  # just the first key pressed
                    buttonBox.rt = theseRTs[0]
                    # was this 'correct'?
                    if (buttonBox.keys == str(cResponse)) or (buttonBox.keys == cResponse):
                        buttonBox.corr = 1
                    else:
                        buttonBox.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        # *p_port* updates
        if t >= 0.0 and p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port.tStart = t  # underestimates by a little under one frame
            p_port.frameNStart = frameN  # exact frame index
            p_port.status = STARTED
            win.callOnFlip(p_port.setData, int(choiceMarker))
        if p_port.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port.status = STOPPED
            #if buttonBox.corr == 1:
                #win.callOnFlip(p_port.setData, int(cResponseMarker))
            #elif buttonBox.corr == 0:
                #win.callOnFlip(p_port.setData, int(icResponseMarker))
        
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
    # check responses
    if buttonBox.keys in ['', [], None]:  # No response was made
       buttonBox.keys=None
       win.callOnFlip(p_port.setData, int(lResponseMarker))
       # was no response the correct answer?!
       if str(cResponse).lower() == 'none': buttonBox.corr = 1  # correct non-response
       else: buttonBox.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('buttonBox.keys',buttonBox.keys)
    trials.addData('buttonBox.corr', buttonBox.corr)
    if buttonBox.keys != None:  # we had a response
        trials.addData('buttonBox.rt', buttonBox.rt)
    if p_port.status == STARTED:
        if len(theseKeys) > 0 and (buttonBox.corr == 1):
            win.callOnFlip(p_port.setData, int(cResponseMarker))
        elif len(theseKeys) > 0 and (buttonBox.corr == 0):
            win.callOnFlip(p_port.setData, int(icResponseMarker))
        elif buttonBox.keys==None:
            win.callOnFlip(p_port.setData, int(lResponseMarker))
    
    #------Prepare to start Routine "highlight"-------
    t = 0
    highlightClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    imageLeftHL.setImage(symbol1)
    imageRightHL.setImage(symbol2)
    # keep track of which components have finished
    highlightComponents = []
    highlightComponents.append(imageLeftHL)
    highlightComponents.append(imageRightHL)
    for thisComponent in highlightComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "highlight"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = highlightClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageLeftHL* updates
        if t >= 0.0 and imageLeftHL.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageLeftHL.tStart = t  # underestimates by a little under one frame
            imageLeftHL.frameNStart = frameN  # exact frame index
            if buttonBox.keys == 2:
                imageLeftHL.setOpacity(1.0)
                imageLeftHL.setSize([0.35,0.6])
                imageLeftHL.setAutoDraw(True)
            elif buttonBox.keys == 4:
                imageLeftHL.setOpacity(0.2)
                imageLeftHL.setSize([0.25,0.45])
                imageLeftHL.setAutoDraw(True)
        if imageLeftHL.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageLeftHL.setAutoDraw(False)
        
        # *imageRightHL* updates
        if t >= 0.0 and imageRightHL.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageRightHL.tStart = t  # underestimates by a little under one frame
            imageRightHL.frameNStart = frameN  # exact frame index
            if buttonBox.keys == 4:
                imageRightHL.setOpacity(1.0)
                imageRightHL.setSize([0.35,0.6])
                imageRightHL.setAutoDraw(True)
            elif buttonBox.keys == 2:
                imageRightHL.setOpacity(0.2)
                imageRightHL.setSize([0.25,0.45])
                imageRightHL.setAutoDraw(True)
        if imageRightHL.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            imageRightHL.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in highlightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "highlight"-------
    for thisComponent in highlightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "blink"-------
    t = 0
    blinkClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blinkComponents = []
    blinkComponents.append(textBlink3)
    blinkComponents.append(textBlink2)
    blinkComponents.append(textBlink1)
    blinkComponents.append(text)
    for thisComponent in blinkComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "blink"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blinkClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlink3* updates
        if t >= 0.0 and textBlink3.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBlink3.tStart = t  # underestimates by a little under one frame
            textBlink3.frameNStart = frameN  # exact frame index
            textBlink3.setAutoDraw(True)
        if textBlink3.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            textBlink3.setAutoDraw(False)
        
        # *textBlink2* updates
        if t >= 1.0 and textBlink2.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBlink2.tStart = t  # underestimates by a little under one frame
            textBlink2.frameNStart = frameN  # exact frame index
            textBlink2.setAutoDraw(True)
        if textBlink2.status == STARTED and t >= (1.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            textBlink2.setAutoDraw(False)
        
        # *textBlink1* updates
        if t >= 2.0 and textBlink1.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBlink1.tStart = t  # underestimates by a little under one frame
            textBlink1.frameNStart = frameN  # exact frame index
            textBlink1.setAutoDraw(True)
        if textBlink1.status == STARTED and t >= (2.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            textBlink1.setAutoDraw(False)
        
        # *text* updates
        if t >= 3.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        if text.status == STARTED and t >= (3.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "blink"-------
    for thisComponent in blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
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
