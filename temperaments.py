"""This module initializes a few global variables containing
settings for a few temperaments, in 440Hz pitch"""
import numpy as np

temperaments = dict()

noteNames = [] # will contain, in order, names of the notes.


def fillNames():
    global noteNames
    notes = ['C', 'C#', 'D', 'E#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    for octave in range(-1, 8):
        for i in range(12):
            noteNames.append(notes[i]+str(octave))


def meantone():
    octave4 = [263.1813856, 275.0000000, 294.2457342, 314.8383713, 328.9767320, 352.0000000,\
               367.8071678, 393.5479641, 411.2209150, 440.0, 470.7931747, 491.9349551]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0**(i-4))
    return freqs


def equal():
    octave4 = [440.0 * (2.0**(k / 12)) for k in range(-9, 3)]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs


def valotti5th():
    octave4 = [262.6914355, 277.0573737, 294.0630272, 312.1124797, 329.1811314, 351.1265398, \
               369.4098316, 393.0593816, 415.5860606, 440.0, 468.1687196, 492.5464421]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs


def valotti4th():
    octave4 = [263.1813856, 276.7134122, 294.2457342, 312.8888889, 328.9767320, 352.0000000,
               368.9512163, 393.5479641, 415.0701183, 440.0, 469.3333333, 491.9349551]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs


def valotti():
    pass


def meantone5th():
    pass


def meantone6th():
    pass

fillNames()
temperaments['meantone'] = meantone()
temperaments['equal'] = equal()
temperaments['valotti5th'] = valotti5th()
temperaments['valotti4th'] = valotti4th()

