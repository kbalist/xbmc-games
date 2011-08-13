#!/usr/bin/env bash

####################################
# PSX LAUNCHER
####################################
# Thanks to http://www.gwenael.org/xbmc/index.php?title=PCSX-Reloaded#Linux

# launcher : pcsx
# manual : man pcsx
# romext : mdf|iso|bin|img
# savegame : yes

# TODO:
#	- fix sound volume

# command line options :
#	-nogui : Don't load the GUI
#	-cdfile : run specified file (missing from man)
####################################

/usr/games/pcsx -nogui -cdfile "$1"