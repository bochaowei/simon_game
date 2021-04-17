import threading
from playsound import playsound

# OSX install of playsound (allows you to play sound files!)
# Should work on Windows too
# from terminal, make sure you are in the right conda env
# >> source activate cs6452
# Now install playsound deps
# >> pip install pyobjc
# >> pip install playsound
# NOTE: On OSX, the path to sound file appears to require no spaces in path names. Possibly same problem on Windows

def playsoundasync(path):
    t1 = threading.Thread(target=playsound, args=[path])
    t1.start()
