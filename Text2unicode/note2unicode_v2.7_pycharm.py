# -*- coding: utf-8 -*-
# python version ==  3.10
# music21.__version__ == 5.5.0
# Done
# Notes, keys, time signature, sharp/flat, tail direction, rest
# Not done yet
# beam, symbol
# Problem
# D6, Ornaments,

# The newest update can view the OpenProject

import music21
from music21 import *
import pandas as pd

stream_c = music21.converter.parse('op15_D.mxl')  # Input the song/piece here.

key = stream_c.analyze('key')
meta_key = str(key)

# extract the meta-data, like key, time signature, metronome mark
dict_meta = dict()
dict_meta['key'] = meta_key

TimeSignature = stream_c.recurse().stream().getTimeSignatures()[0]
meta_TimeSignature = str(TimeSignature)
dict_meta['TimeSignature'] = meta_TimeSignature.split(' ')[-1][:-1][0] + meta_TimeSignature.split(' ')[-1][:-1][-1]

metronomeMark = stream_c.metronomeMarkBoundaries()[0][2]
metronomeMark = str(metronomeMark)
dict_meta['metronomeMark'] = metronomeMark.split(' ')[-1][:-1]

tempo_ = dict_meta['metronomeMark']
Time_Signature = dict_meta['TimeSignature']
keys = dict_meta['key']

temp_1 = ['whole', 'half', 'quarter', 'eighth', '16th']
temp_2 = [4, 2, 1, .5, .25]

tempo_dict = dict(zip(temp_1, temp_2))

# Not used
tempo = float(dict_meta['metronomeMark'].split('=')[1])
metro_sig = tempo_dict[str(dict_meta['metronomeMark'].split('=')[0]).lower()]  # ratio to 4-times note

note_list = []
duration_list = []
time_stamp_list = []
note_duration_name = []

for n in stream_c.flat.notesAndRests:
    try:
        # print("Note: %s%d %0.01f" % (n.pitch.name, n.pitch.octave, n.duration.quarterLength))
        temp_name = n.pitch.name
        if n.duration.quarterLength == float(0.0):  # it is an Ornaments
            temp_name = str('Ornaments ') + str(n.pitch.name)  # O for Ornaments

        note_list.append(str(temp_name) + str(n.pitch.octave))
        duration_list.append(n.duration.quarterLength)
        time_stamp_list.append(n.duration.quarterLength * (60 / tempo) / metro_sig)  # *(60/tempo)/metro_sig
        note_duration_name.append(duration.Duration(float(n.duration.quarterLength)).type)

    except:
        try:
            for i in n:
                pass
            # print('------------------It is a chord:------------------')
            temp_note = []
            temp_duration = []
            temp_time_stamp = []
            temp_note_duration_name = []

            for i in n:
                # print("Note: %s%d %0.01f" % (i.pitch.name, i.pitch.octave, i.duration.quarterLength))
                temp_note.append(str(i.pitch.name) + str(i.pitch.octave))
                temp_duration.append(i.duration.quarterLength)
                temp_time_stamp.append(i.duration.quarterLength * (60 / tempo) / metro_sig)  # *(60/tempo)/metro_sig
                temp_note_duration_name.append(duration.Duration(float(i.duration.quarterLength)).type)

            # print('------------------------End------------------------')

            y = ''
            for i in temp_note:
                y += str(i)
                y = y + ','

            # Added
            x = ''
            for i in temp_duration:
                x += str(i)
                x = x + ','

            z = ''
            for i in temp_time_stamp:
                z += str(i)
                z = z + ','

            xx = ''
            for i in temp_note_duration_name:
                xx += str(i)
                xx = xx + ','

            note_list.append(str('chord, ') + y + str('chord end'))
            duration_list.append(str(x[:-1]))  # Changed: del last ','
            time_stamp_list.append(str(z[:-1]))
            note_duration_name.append(str(xx[:-1]))

        except:
            # print("Rest Note: %0.01f" % (n.duration.quarterLength))
            try:
                note_list.append('Rest')
                duration_list.append(n.duration.quarterLength)
                time_stamp_list.append(n.duration.quarterLength * (60 / tempo) / metro_sig)  # *(60/tempo)/time_sig
                note_duration_name.append(duration.Duration(float(n.duration.quarterLength)).type)
            except:
                raise 'It is not a note, chord or rest'

# show(c)
all_list = zip(note_list, duration_list, time_stamp_list, note_duration_name)

pd.set_option('display.max_rows', 1500)

df = pd.DataFrame()
df['Note name'] = note_list
df['duration'] = duration_list
df['Note type'] = note_duration_name
df['duration (in s)'] = time_stamp_list

"""The next box's code not used"""

duration_dictionary = {float(0.0625): 'note 64th', float(0.125): 'note 32nd', float(0.25): 'note 16th',
                       float(0.5): 'note 8th', float(1.0): 'Quarter', float(2.0): 'Half', float(4.0): 'Whole',
                       float(0.0): 'Ornament', float(1.5): 'Quarter with augmentation Dot',
                       float(2.5): 'Half with augmentation Dot',
                       float(0.75): 'note 16th with augmentation Dot'}  # Need to add more cases
duration_list_converted = []

for i in range(len(duration_list)):

    try:
        k = []
        temp = duration_dictionary[duration_list[i]]
        duration_list_converted.append(temp)

    except:
        k = []
        temp_2 = []
        k.append(duration_list[i].split(','))

        for j in k:
            for h in j:
                h = float(h)
                temp_2.append(duration_dictionary[float(h)])

        x = ''
        for j in temp_2:
            x = x + str(j) + ','
        duration_list_converted.append(x[:-1])

"""Not used end"""

# Start
# Dictionary
temp_symbol = ['5-line staff',
               'Single barline', 'Final barline',
               'G clef',
               'metronome whole', 'metronome half', 'metronome quarter', 'metronome note 8th', 'metronome note 16th']
temp_symbol_unicode = ['E01A',
                       'E030', 'E032',
                       'E050',
                       'ECA2', 'ECA3', 'ECA5', 'ECA7', 'ECA9']

temp_symbol_dict = dict(zip(temp_symbol, temp_symbol_unicode))

# Note name
unicode_6 = ['EB90', 'EB91', 'EB92', 'EB93', 'EB94', 'EB95', 'EB96', 'EB97', 'EB91',  # D6 'E511;&#x' + 'EB91'
             '', 'EB98', 'EB99', 'EB9A', 'EB9B', 'EB9C', 'EB9D', 'EB9E', 'EB9F', 'EB99']  # B4, G3
unicode_6_name = ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6',  # D6
                  'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3']  # B4, G3

Note_name_dict = dict(zip(unicode_6_name, unicode_6))

# Note type
unicode_7 = ['E1D2', 'E1D3',
             'E1D5',
             'E1D7',
             'E1D9']
unicode_7_name = ['whole', 'half',
                  'quarter',
                  'eighth',
                  '16th']

unicode_77 = ['E1D2', 'E1D4', 'E1D6', 'E1D8', 'E1DA']
unicode_77_name = ['whole', 'half', 'quarter', 'eighth', '16th']

Note_type_down_dict = dict(zip(unicode_7_name, unicode_7))
Note_type_up_dict = dict(zip(unicode_77_name, unicode_77))
# beam
unicode_8 = ['E8E0', 'E8E1',  # Only for 'note 8th', 'note 16th'
             'E8E2', 'E8E3']
unicode_8_name = ['Begin beam', 'End beam',
                  'Begin tie', 'End tie']

beam_dict = dict(zip(unicode_8_name, unicode_8))
# Rest
# if == rest
unicode_9 = ['E4E0', 'E4E1', 'E4E2', 'E4E3', 'E4E4', 'E4E5', 'E4E6', 'E4E7', 'E4E8']
unicode_9_name = ['restMaxima', 'restLonga', 'restDoubleWhole', 'whole', 'half', 'quarter', 'eighth', '16th', '32nd']
# First 3 have not changed name

rest_dict = dict(zip(unicode_9_name, unicode_9))
# Time signature
unicode_10 = ['E081', 'E082', 'E083', 'E084', 'E085', 'E086', 'E087', 'E088', 'E089']
temp_Time_signature = ['E09E', 'E09F']
unicode_10_name = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

Time_signature_dict = dict(zip(unicode_10_name, unicode_10))

unicode_11_name = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
unicode_11 = ['', 2, '', 1, '', '', '', .5, '']

Time_signature_duration_dict = dict(zip(unicode_11_name, unicode_11))

unicode_12_name = ['A5', 'B5', 'C6', 'D6', 'E6',  # E5 position of legar has problem
                   'C4', 'B3', 'A3', 'G3']

unicode_12 = ['EB95;&#x' + 'E022', 'EB95;&#x' + 'E022', 'EB95;&#x' + 'E022;&#x' + 'EB97;&#x' + 'E022',
              'EB95;&#x' + 'E022;&#x' + 'EB97;&#x' + 'E022', 'EB95;&#x' + 'E022;&#x' + 'EB97;&#x' + 'E022',
              'EB9D;&#x' + 'E022', 'EB9D;&#x' + 'E022', 'EB9D;&#x' + 'E022;&#x' + 'EB9F;&#x' + 'E022',
              'EB9D;&#x' + 'E022;&#x' + 'EB9F;&#x' + 'E022']
Legar_dict = dict(zip(unicode_12_name, unicode_12))  # position of the line

# Keys (Not finished yet)
unicode_13_name = ['C major', 'G major', 'D major']  # , 'A major', 'E major', 'B major',
# 'F# major', 'B- major', 'E- major', 'A- major', 'D- major'] # minor
unicode_13 = ['', 'E01A;&#x' + 'EB93;&#x' + 'E262',
              'E01A;&#x' + 'EB93;&#x' + 'E262;&#x' + '2004;&#x' + 'E01A;&#x' + 'EB91;&#x' + 'E262',
              'E01A;&#x' + 'EB93;&#x' + 'E262;&#x' + 'E01A;&#x' + '2004;&#x' + 'EB91;&#x' + 'E262;&#x' + 'E01A;&#x' +
              '2004;&#x' + 'EB94;&#x' + 'E262']

key_dict = dict(zip(unicode_13_name, unicode_13))

unicode_14_name = ['#', '-', '##', '--', 'n']  # n for natural sign
unicode_14 = ['E262', 'E260', 'E263', 'E264', 'E261']
standard_accidentals_dict = dict(zip(unicode_14_name, unicode_14))

# Dictionary end

# checking list
beam_checking_list = ['eighth', '16th']
note_check_list = ['A5', 'B5', 'C6', 'D6', 'E6',
                   'C4', 'B3', 'A3', 'G3']
key_check_list = ['C major',
                  'G major', 'D major', 'A major', 'E major', 'B major',
                  'C- major',
                  'F# major',
                  'F major', 'B- major', 'E- major', 'A- major', 'D- major',
                  'C# major',
                  'G- major']
key_list = [[''],
            ['F#'], ['F#', 'D#'], ['F#', 'D#', 'G#'], ['F#', 'D#', 'G#', 'D#'], ['F#', 'D#', 'G#', 'D#', 'A#'],
            ['B-', 'E-', 'A-', 'D-', 'G-', 'C-', 'F-'],  # not always used
            ['F#', 'D#', 'G#', 'D#', 'A#', 'E#'],
            ['B-'], ['B-', 'E-'], ['B-', 'E-', 'A-'], ['B-', 'E-', 'A-', 'D-'], ['B-', 'E-', 'A-', 'D-', 'G-'],
            ['F#', 'D#', 'G#', 'D#', 'A#', 'E#', 'B#'],  # not always used
            ['B-', 'E-', 'A-', 'D-', 'G-', 'C-']]
# minor not have yet done, but the same method.
key_check_list_dict = dict(zip(key_check_list, key_list))

# checking list end

"""Tail down or up part"""

# case for 3/8
base_unit = Time_signature_duration_dict[str(dict_meta['TimeSignature'][-1])]

temp_container = []
temp = []
tt = list(Note_name_dict)
t = 0
bar_separated = []
for i in range(df.shape[0]):
    t += float(df.iloc[i, 1])

    if len(str(df.iloc[i, 0])) == 3:
        df.iloc[i, 0] = df.iloc[i, 0][0] + df.iloc[i, 0][-1]

    if dict_meta['TimeSignature'] != str(38):
        break

    if len(str(df.iloc[i, 0])) == 2:

        temp_ = (tt.index(str(df.iloc[i, 0])) - 9)
        temp_container.append(temp_)

        if temp_ < 0:
            temp__ = -1

        elif temp_ > 0:
            temp__ = 1

        else:
            temp__ = 0

    else:
        temp__ = 0

    temp.append(temp__)
    while t == int(dict_meta['TimeSignature'][0]) * base_unit:

        if sum(temp) == 0:  # special case, we will use weighting to decide is it up or not (down)
            bar_separated.append(sum(temp_container))
        else:
            bar_separated.append(sum(temp))

        temp = []
        temp_container = []
        t = 0

# tail part end

# Unicode part
# For time signature 38 only
Unicode = []
clef = 'G clef'

tt = list(Note_name_dict)

# sharp: E262 flat: E260 double
# 5-line staff
Unicode.append(temp_symbol_dict['5-line staff'])

# clef
Unicode.append(temp_symbol_dict[clef])

# key (sharp/flat)
Unicode.append(key_dict[keys])
Unicode.append('2004')

# time signature
Unicode.append(temp_Time_signature[0] + ';&#x' + Time_signature_dict[dict_meta['TimeSignature'][0]] +
               ';&#x' + temp_Time_signature[-1] + ';&#x' + Time_signature_dict[dict_meta['TimeSignature'][-1]])
Unicode.append(temp_symbol_dict['5-line staff'])
Unicode.append('2004')
Unicode.append(temp_symbol_dict['5-line staff'])
Unicode.append('2004')

base_unit = Time_signature_duration_dict[str(dict_meta['TimeSignature'][-1])]
counting = 0
classifier = 0

for i in range(df.shape[0]):

    if dict_meta['TimeSignature'] != str(38):  # Checking is it 38
        break

    counting += float(df.iloc[i, 1])
    Unicode.append(temp_symbol_dict['5-line staff'])  # add 5-line

    # Handling the # or flat if they have already in the key
    if len(str(df.iloc[i, 0])) == 3 and (df.iloc[i, 0][:2] in key_check_list_dict[keys]):
        df.iloc[i, 0] = df.iloc[i, 0][0] + df.iloc[i, 0][-1]

    # handling the natural sign
    elif len(str(df.iloc[i, 0])) == 2 and (df.iloc[i, 0][:2] in [classifier[0] for classifier in key_check_list_dict[
        keys]]):
        df.iloc[i, 0] = df.iloc[i, 0][0] + 'n' + df.iloc[i, 0][-1]

    # Handling the temporary # or flat
    if len(str(df.iloc[i, 0])) == 3:
        temp_key = str(df.iloc[i, 0][1])
        df.iloc[i, 0] = df.iloc[i, 0][0] + df.iloc[i, 0][-1]
        # Unicode.append(temp_symbol_dict['5-line staff'])
        Unicode.append(Note_name_dict[df.iloc[i, 0]])
        Unicode.append(standard_accidentals_dict[temp_key])
        Unicode.append('')  # space
        Unicode.append(temp_symbol_dict['5-line staff'])

    # Nots' type
    if df.iloc[i, 0] == 'Rest':
        Unicode.append(rest_dict[df.iloc[i, 2]])
        # blank
        Unicode.append('2004')

    elif str(df.iloc[i, 0])[:9] == 'Ornaments':
        pass
    elif len(str(df.iloc[i, 0])) == 2:  # normal notes
        '''    # Checking the tail should up or down
        temp__ = tt.index(str(df.iloc[i,0]))'''

        #############################################################
        if df.iloc[i, 0] == str('B4'):  # == B4
            if bar_separated[classifier] < 0:
                '''if df.iloc[i,2] in beam_checking_list and df.iloc[i + 1,2] in beam_checking_list: # add beam
        Unicode.append(beam_dict['Begin beam'])'''

                Unicode.append(Note_type_up_dict[df.iloc[i, 2]])
                Unicode.append('2005')

            else:
                Unicode.append(Note_type_down_dict[df.iloc[i, 2]])

        #############################################################
        else:  # != 'B4'
            if bar_separated[classifier] < 0:
                '''if df.iloc[i,2] in beam_checking_list and df.iloc[i + 1,2] in beam_checking_list: # add beam
        Unicode.append(beam_dict['Begin beam'])'''
                Unicode.append(Note_name_dict[df.iloc[i, 0]] + ';&#x' + Note_type_up_dict[df.iloc[i, 2]])

                if df.iloc[i, 0] in note_check_list:  # need external lines
                    Unicode.append(Legar_dict[df.iloc[i, 0]])

            else:
                Unicode.append(Note_name_dict[df.iloc[i, 0]] + ';&#x' + Note_type_down_dict[df.iloc[i, 2]])

                if df.iloc[i, 0] in note_check_list:  # need external lines
                    Unicode.append(Legar_dict[df.iloc[i, 0]])

            Unicode.append('2002')
        # blank

    while counting == int(dict_meta['TimeSignature'][0]) * base_unit:
        try:  # Checking is it the last bar
            temp___ = df.iloc[i + 1, 0]
            Unicode.append(temp_symbol_dict['Single barline'])
            Unicode.append(temp_symbol_dict['5-line staff'])
            Unicode.append('2004')
            classifier += 1

        except:
            pass

        counting = 0

Unicode.append(temp_symbol_dict['Final barline'])

all_ = '&#x'

for i in range(len(Unicode)):
    all_ = all_ + Unicode[i] + ';' + '&#x'

all_ = all_[:-3]
print(all_)

with open('D_wav.txt', 'w') as f:
    f.write(all_)  # Copy it and run it as html
