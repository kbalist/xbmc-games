#!/usr/bin/env bash

####################################
# SNES LAUNCHER
####################################
# Thanks to http://www.gwenael.org/xbmc/index.php?title=ZSNES#Linux

# launcher : zsnes
# manual : man zsnes
# romext : zip|smc|sfc

# config : ~/.zsnes/zsnesl.cfg
#	- MusicRelVol=70 Sound Volume Level [0..100]
# 	- DisplayInfo=0 Display ROM Info on Load (0 = No, 1 = YES)

# command line options :
#	-m : Disable GUI (Must specify ROM filename)
#	-r : Set audio sampling rate, where 6 = 48 KHz
#	-s : Enable SPC700/DSP emulation (Sound)
#	-v : Select video mode, where 
#		 18 = 1280x1024 ODS F
#		 22 = CUSTOM OD F
#	-ad : audio driver : sdl
####################################

/usr/bin/zsnes -m -s -v 18 -ad sdl -r 6 "$1"
