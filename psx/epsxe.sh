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
#	-loadiso : run specified file (missing from man)

####################################


/media/data/games/psx/epsxe/epsxe -nogui -loadiso "$1"

