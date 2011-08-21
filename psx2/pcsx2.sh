#!/bin/bash

####################################
# PSX2 LAUNCHER
####################################

# launcher : pcsx2
# manual : man pcsx2
# romext : iso|bin

# command line options :
#	-nogui : Don't load the GUI
#	-cdfile : run specified file (missing from man)
####################################

#tricks to reduce volume level
amixer -c 0 sset Master,0 30%
/usr/games/pcsx2 --nogui "$1"
amixer -c 0 sset Master,0 100%




