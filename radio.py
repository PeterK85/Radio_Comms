# The directory containing the audio files.
# TODO: add note on how to find directory path
# Example: "~/audio_clips/star_wars/"
# NOTE: Make sure to put the directory in quotation marks ""
# NOTE: Currently Supported Audio Formats
#       - mp3
audio_directory = "/home/peter/projects/mandos/dray/code"

#------------------------------------------------------------------------------------
#
#                      DO NOT CHANGE ANYTHING BELOW THIS POINT
#                           (UNLESS YOU ARE CONFIDENT)
#
#------------------------------------------------------------------------------------
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pynput.keyboard import Listener, Key
import pygame as pg
import threading
import speech_recognition as sr
import pocketsphinx

# This function is used to grab all of the files paths in a directory.
# The file that is searched is set as a global variable at the top of the files.
# The directory that is loaded should contain the audio files that are desired for
# the radio/comms/whatever the hell you want audio for.
def load_files(directory):
    #create a list of file and sub-directories
    list_of_file = os.listdir(directory)
    files = list()

    # go over all of the files in the directory
    for entry in list_of_file:
        # get full path of file
        full_path = os.path.join(directory, entry)
        # if there is a sub-directory then get those files
        if os.path.isdir(full_path):
            files = files + load_files(full_path)
        else:
            files.append(full_path)

    return files

# This function is used for removing unsupported files (.txt, .pdf, etc.) only 
# accepted audio formats.
# NOTE - ACCEPTED AUDIO FORMATS - mp3
# TODO: Test audio formats
def cleanse_file_list(files):
    audio_files = list()
    for f in files:
        if "mp3" in f:
            audio_files.append(f)

    return audio_files

def main():
    global audio_directory
    files = load_files(audio_directory)
    audio_files = cleanse_file_list(files)
    for f in audio_files:
        print(f)

# runs main function when started up
if __name__ == "__main__":
    main()

