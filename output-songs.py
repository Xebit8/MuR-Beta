import pyglet
from os import walk
from time import sleep
from random import randint


dir = 'C:\\Users\\I\\Desktop\\MuR-Beta\\mp3\\'

f = []
# id = 1
# n = 0

for (dirpath, dirnames, filenames) in walk(dir):

    f.extend(filenames)
    rand = randint(0, len(f)-1)

    for songs in f:
        # print(songs)
        print(str(rand+1)+". "+f[rand])
        song = pyglet.media.load(dir+f[rand])
        # id += 1
        # n += 1
        song.play()
        pyglet.app.run()

