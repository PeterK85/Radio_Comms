from pynput.keyboard import Listener, Key # used for listening for keyboard input
import pygame as pg # used for playing audio
import threading # used for threading

# global variables for flagging
listener_flag = True
music_flag = False
play_flag = False

def on_press(key):
    try:
        if(key.char == 'p'):
            global music_flag
            global play_flag
        
            # start playing music
            if music_flag == False:
                music_flag = True
                play_flag = True

                music_thread = threading.Thread(target = music_func, args = ("imps_alarm.mp3", 0.8,))
                # no join because python threads are automically detached in c/c++ source code
                music_thread.start()
            # music thread has been created
            elif music_flag == True:
                play_flag = False
            else:
                print("...error - music flag not True or False")
    except AttributeError:
        # do nothing for special keys
        print("...error - special key pressed...")

def on_release(key):
    try: 
        # return false ends the listener
        # stops the program right now
        if(key.char == 'q'):
            global listener_flag
            listener_flag = False
            return listener_flag
    except AttributeError:
        # do nothing for special keys
        print("...error - special key released...")

def listener_func():
    # loop until q is pressed
    global listener_flag
    while listener_flag: #TODO: does this need to be an infinite loop??
        # start listening for key presses
        with Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()

def music_func(music_file, volume=0.8):
    # flag for if the music is to be played or not
    global music_flag
    global play_flag

    # boiler plate overhead
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048

    # create the player
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()

    try:
        pg.mixer.music.load(music_file)
    except pg.error:
        print("...error - could not load music file...")

    pg.mixer.music.play()
    
    # loop until song is over or flag was flipped
    while play_flag and pg.mixer.music.get_busy():
        clock.tick(30)

    # music was stopped prematurely
    if play_flag == False:
        pg.mixer.music.stop()

    # reset flag for new music
    play_flag = False
    music_flag = False

def main():
    # create and listeners and music profiles
    listener_thread = threading.Thread(target = listener_func) 

    # start the "meat and potatos" of the program 
    listener_thread.start()

    # wait for the other threads to play
    listener_thread.join()

if __name__ == "__main__":
    main()
