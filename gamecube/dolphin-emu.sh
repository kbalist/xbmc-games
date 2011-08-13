#!/usr/bin/env bash

####################################
# GAMECUBE LAUNCHER
####################################
# Thanks to http://www.gwenael.org/xbmc/index.php?title=Dolphin#Linux

# launcher : dolphin-emu
# manual : man dolphin-emu
# romext : elf|dol|gcm|iso|wad
# savegame : yes

# TODO:
#	- fix sound problem
#	- display 16/9

# config : 
# Prior to use Dolphin emulator with XBMC you need to use its GUI to modify some options. Into Options/Configure/Display menu:
# 	- Check "Start Renderer in Fullscreen" option
# 	- Check "Hide mouse cursor" option
# 	- Uncheck "Confirm on Stop" option
# 	- Into Options/Configure/Path menu select the directory where are located your iso files.

# command line options :
#	-e : rom to load
#	-b : ??
####################################

/usr/games/dolphin-emu -b -e "$1"