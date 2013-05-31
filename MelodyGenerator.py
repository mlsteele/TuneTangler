import math
import random

# NotesDict = {}
# n = 1
# for octave in range(1,9):
# 	for note in ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']:
# 		NotesDict[(note, octave)] = n
# 		n += 1
# doubleNotes = ['Db', 'Eb', 'Gb', 'Ab', 'Bb']
# n2 = 0
# for note in ['C#', 'D#', 'F#', 'G#', 'A#']:
# 	for octave in range(1,9):
# 		NotesDict[(note, octave)] = NotesDict[(doubleNotes[n2], octave)]
# 	n2 += 1
# print NotesDict

# NotesDict = {}
# n = 1
# for note in ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']:
# 	NotesDict[note] = n
# 	n += 1
# print NotesDict
# doubleNotes = ['Db', 'Eb', 'Gb', 'Ab', 'Bb']
# n2 = 0
# for note in ['C#', 'D#', 'F#', 'G#', 'A#']:
# 	NotesDict[note] = NotesDict[doubleNotes[n2]]
# 	n2 += 1
# print NotesDict


noteBaseValues = {'A': 10, 'C': 1, 'Ab': 9, 'E': 5, 'D': 3, 'G': 8, 'F': 6,
 'Bb': 11, 'Db': 2, 'Eb': 4, 'B': 12, 'Gb': 7}

baseValuetoNote = {1: 'C', 2: 'Db', 3: 'D', 4: 'Eb', 5: 'E', 6: 'F', 7: 'Gb',
  8: 'G', 9: 'Ab', 10: 'A', 11: 'Bb', 12: 'B'}

class Note:
	def __init__(self, note, octave):
		self.note = note
		self.octave = octave
		self.name = note + str(octave)
		self.value = noteBaseValues[note] + (octave-1)*12

def noteFromValue(num):
	octave = math.floor(num/12.0) + 1
	baseValue = num % 12
	note = baseValuetoNote[baseValue]
	return Note(note, octave)

class Melody:
	def __init__(self, sequence):
		self.notes = sequence
		self.startNote = sequence[0]

def makeMelody(key, length):
	sequence = []
	


# NotesList = []
# for octave in range(1,9):
# 	for note in noteBaseValues.keys():
# 		NotesList.append(Note(note, octave))
# print NotesList


# noteValues = {('C', 6): 61, ('F', 1): 6, ('Bb', 1): 11, ('C#', 3): 26, ('Gb', 8): 91, 
# ('C#', 8): 86, ('Gb', 5): 55, ('E', 2): 17, ('Db', 8): 86, ('Ab', 2): 21, ('G#', 4): 45, 
# ('Eb', 3): 28, ('A#', 1): 11, ('F', 4): 42, ('A', 6): 70, ('Bb', 2): 23, ('G#', 2): 21, 
# ('D', 2): 15, ('Db', 2): 14, ('E', 7): 77, ('Ab', 1): 9, ('C', 1): 1, ('Eb', 6): 64, 
# ('A#', 2): 23, ('A', 3): 34, ('D', 8): 87, ('C#', 2): 14, ('D', 5): 51, ('Db', 7): 74, 
# ('E', 4): 41, ('F#', 4): 43, ('D#', 7): 76, ('Eb', 8): 88, ('C', 2): 13, ('Eb', 5): 52, 
# ('Bb', 5): 59, ('A#', 7): 83, ('G', 4): 44, ('Bb', 8): 95, ('D#', 3): 28, ('Gb', 1): 7, 
# ('Db', 4): 38, ('F#', 3): 31, ('Ab', 6): 69, ('C', 7): 73, ('Bb', 6): 71, ('A#', 8): 95, 
# ('G', 1): 8, ('D#', 6): 64, ('C#', 1): 2, ('Gb', 4): 43, ('E', 3): 29, ('G#', 8): 93, 
# ('B', 5): 60, ('B', 4): 48, ('Ab', 5): 57, ('D#', 8): 88, ('Eb', 2): 16, ('C', 8): 85, 
# ('F', 7): 78, ('A', 7): 82, ('Bb', 3): 35, ('G', 2): 20, ('D', 1): 3, ('Gb', 7): 79, 
# ('Db', 3): 26, ('F#', 8): 91, ('B', 3): 36, ('Eb', 1): 4, ('A#', 3): 35, ('A', 4): 46, 
# ('D', 4): 39, ('E', 5): 53, ('F#', 7): 79, ('C', 3): 25, ('C#', 6): 62, ('Eb', 4): 40, 
# ('A#', 4): 47, ('G', 5): 56, ('A', 1): 10, ('B', 8): 96, ('D#', 2): 16, ('G', 8): 92, 
# ('D', 7): 75, ('G#', 7): 81, ('Db', 5): 50, ('F#', 2): 19, ('C', 4): 37, ('F', 3): 30, 
# ('Bb', 7): 83, ('G', 6): 68, ('D#', 5): 52, ('Gb', 3): 31, ('B', 7): 84, ('F#', 1): 7, 
# ('Ab', 4): 45, ('G#', 1): 9, ('C#', 5): 50, ('F', 6): 66, ('G', 3): 32, ('C#', 7): 74, 
# ('Gb', 6): 67, ('E', 1): 5, ('G#', 6): 69, ('B', 2): 24, ('Ab', 3): 33, ('F', 5): 54, 
# ('A', 5): 58, ('A', 8): 94, ('D', 3): 27, ('Db', 1): 2, ('E', 6): 65, ('F#', 6): 67, 
# ('B', 1): 12, ('Eb', 7): 76, ('A#', 5): 59, ('C#', 4): 38, ('F', 8): 90, ('A', 2): 22, 
# ('D#', 1): 4, ('E', 8): 89, ('D', 6): 63, ('Db', 6): 62, ('F#', 5): 55, ('Ab', 8): 93, 
# ('C', 5): 49, ('F', 2): 18, ('Bb', 4): 47, ('A#', 6): 71, ('G', 7): 80, ('G#', 3): 33, 
# ('D#', 4): 40, ('Gb', 2): 19, ('B', 6): 72, ('G#', 5): 57, ('Ab', 7): 81}

# Key sequences - represents in semitones the values of the next notes in the key, per octave
majorSequence = (2, 2, 1, 2, 2, 2, 1)
naturalMinorSequence = (2, 1, 2, 2, 1, 2, 2)
harmonicMinorSequence = (2, 1, 2, 2, 1 , 3, 1)
dorianSequence = (2, 1, 2, 2, 2, 1, 2)
phrygianSequence = (1, 2, 2, 2, 1, 2, 2)


class Key:
	def __init__(self, note, mode = majorSequence):
		self.startNote = note



class MajorKey(Key):
	def __init__(self, note, register = 'Middle'):
		pass

