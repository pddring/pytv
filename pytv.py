from __future__ import print_function
import os.path
import getopt
import sys
import time

# defaults
interval = 5

print("Welcome PyTV: CCTV on a Raspberry Pi")

# get command line options
try:
   opts, args = getopt.getopt(sys.argv[1:], "i:", ["interval="])
except:
   print("Usage: pytv.py -i interval")
   exit()

# parse command line options
for opt, arg in opts:
   # help
   if opt in ("-h", "--help"):
      print("Usage: pytv.py -i interval")

   # take picture interval
   if opt in ("-i", "--interval"):
      interval = int(arg)

print("Taking pictures every", interval,"second(s)")

# test for webcam on /dev/video0
print("Checking for webcam... ", end='')
if os.path.exists('/dev/video0'):
   print("found")
else:
   print("not found")
   exit()

# load opencv
print("Loading...")
import cv2

# Connect to webcam
import cv2
cam = cv2.VideoCapture(0)

while True:
   filename = time.strftime("%a %d %b %y-%H_%M_%Ss.jpg")
   print("Saving " + filename)
   retval, img = cam.read()

   cv2.imwrite(filename, img)
   time.sleep(interval)

