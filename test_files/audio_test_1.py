import pygame as pg
import time

def play_music(music_file, vol=0.8):
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.mixer.music.set_volume(vol)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("Could not open file: ", music_file)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        print("...ticking...")
        clock.tick(30)


music_file = "jabba_flow.mp3"
vol = 0.8
play_music(music_file, vol)
