# -*- coding: utf-8 -*-
'''
title           :util.py
description     :Utilities for different parts of the project
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20160623
notes           :
python_version  :2.7.6
'''

from __future__ import print_function
import collections


################## CLASSES #########################################
class Queue:
    '''Queue class

    It is a data structure used by the search algorithm to decide the
    order in which to process the locations.
    Itś just a wrapper around the built-in collections.deque class.

    Attrs:
        elements = It's a deque

    '''
    def __init__(self):
        '''It creates a new empty deque'''
        self.elements = collections.deque()

    def empty(self):
        '''Returns True if the queue is empty and False otherwise'''
        return len(self.elements) == 0

    def put(self, x):
        '''Adds a new element to the queue'''
        self.elements.append(x)

    def get(self):
        '''Gets a new element from the left of the queue'''
        return self.elements.popleft()

#################################### FUNCTIONS ##################################3
def getInfoMessage(state):
    '''Returns the info message corresponding to an specific state
    :param state: (int) Represents an execution state (STATE_NONE,STATE_STARTING_POINT,STATE_GOAL_POINT)
    :return: (String) Info message
    '''
    if(state==STATE_NONE):
        return" Click on the grid to add a wall  click on the play button to start the animation"
    elif(state == STATE_STARTING_POINT): #Waiting user to add starting point in the grid
        return "Click anywhere on the grid to add a starting point"
    elif (state == STATE_GOAL_POINT): #Waiting user to add goal point in the grid
        return "Click anywhere on the grid to add a goal point"

################## CONSTANTS ###################################
WIDTH = 640
HEIGHT = 480
BOTTOM_BAR_HEIGHT = 160

COLOR_START_POINT=(255,0,0)
COLOR_GOAL_POINT=(0,75,0)
COLOR_WALL=(100,100,100)
COLOR_TERRAIN = (62,238,18)
COLOR_WHITE=(255,255,255)

STATE_NONE=0
STATE_STARTING_POINT=1
STATE_GOAL_POINT=2

BUTTON_PLAY=0
BUTTON_START_POINT=1
BUTTON_GOAL_POINT=2
BUTTON_RESET=3