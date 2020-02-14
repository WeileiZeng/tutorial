import msvcrt

def doKeyEvent(key):
    if key == '\x00' or key == '\xe0': # non ASCII
       key = msvcrt.getch() # fetch second character
    print ord(key)

def doQuitEvent(key):
    raise SystemExit

lines = 25      # number of lines in console
for line in range(lines):
    print       # clear the screen of clutter
print "Hit space to quit..."
print

# Now mainloop runs "forever"
while True:
   ky = msvcrt.getch()
   length = len(ky)
   if length != 0:
      # send events to event handling functions
      if ky == " ": # check for quit event
         doQuitEvent(ky)
      else: 
         doKeyEvent(ky)
