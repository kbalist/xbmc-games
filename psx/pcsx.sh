#!/usr/bin/env bash

####################################
# PSX LAUNCHER
####################################
# Thanks to http://www.gwenael.org/xbmc/index.php?title=PCSX-Reloaded#Linux

# launcher : pcsx
# manual : man pcsx
# romext : mdf|iso|bin|img
# savegame : yes


# command line options :
#	-nogui : Don't load the GUI
#	-cdfile : run specified file (missing from man)


# usefull tools :
# ecm / unecm : manage ecm archive format ( apt-get install ecm )

####################################

#tricks to reduce volume level
amixer -c 0 sset Master,0 30%
/usr/games/pcsx -nogui -cdfile "$1"
amixer -c 0 sset Master,0 100%
