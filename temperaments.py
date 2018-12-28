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
    # the six quints are shortened by a 5th of syntonic comma
    octave4 = [262.6914355, 277.0573737, 294.0630272, 312.1124797, 329.1811314, 351.1265398, \
               369.4098316, 393.0593816, 415.5860606, 440.0, 468.1687196, 492.5464421]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs


def valotti4th():
    # three pure thirds
    octave4 = [263.1813856, 276.7134122, 294.2457342, 312.8888889, 328.9767320, 352.0000000, \
               368.9512163, 393.5479641, 415.0701183, 440.0, 469.3333333, 491.9349551]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs


def valotti():
    # the six shortened quints are shortened with 1/6th of pythagorean comma here. No schisma
    octave4 = [262.5133927, 277.1826308, 293.9965771, 311.8304596, 329.2555341, 350.8092676, \
               369.5768411, 392.8817606, 415.7739462, 440, 467.7456894, 492.7691215]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs


def meantone5th():
    octave4 = [262.6914355, 275.6840882, 294.0630272, 313.6672287, 329.1811314, 351.1265398, \
               368.4931706, 393.0593816, 412.5000003, 440, 469.3333328, 492.5464421]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs


def meantone6th():
    octave4 = [262.3653092, 276.1410920, 293.9412856, 312.8888885, 329.3174682, 350.5454376, \
               368.9512164, 392.7339972, 413.3549332, 440, 468.3626210, 492.9545222]
    freqs = []
    for i in range(-1, 9):
        for j in range(12):
            freqs.append(octave4[j] * 2.0 ** (i - 4))
    return freqs

fillNames()
temperaments['meantone'] = meantone()
temperaments['meantone5th'] = meantone5th()
temperaments['meantone6th'] = meantone6th()
temperaments['equal'] = equal()
temperaments['valotti5th'] = valotti5th()
temperaments['valotti4th'] = valotti4th()
temperaments['valotti'] = valotti()


