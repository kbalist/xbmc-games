#!/usr/bin/env bash

####################################
# GAMECUBE LAUNCHER
####################################
# Thanks to http://www.gwenael.org/xbmc/index.php?title=Dolphin#Linux

# launcher : dolphin-emu
# manual : man dolphin-emu
# romext : elf|dol|gcm|iso|wad

# config : 
# Prior to use Dolphin emulator with XBMC you need to use its GUI to modify some options. Into Options/Configure/Display menu:
# 	- Check "Start Renderer in Fullscreen" option
# 	- Check "Hide mouse cursor" option
# 	- Uncheck "Confirm on Stop" option
# 	- Into Options/Configure/Path menu select the directory where are located your iso files.
#
# For some Linux system configuration, the Dolphin emulator cannot be directly started from XBMC due to a problem related to users privilege access. This could be bypassed by stating dolphin-emu using the sudo command line as follow.
# Application
# 		/usr/bin/sudo
# Arguments
# 		-u username /usr/bin/dolphin-emu -e "%rom%" -b
# Where username is the name of the user with the rights to execute dolphin-emu.

# command line options :
#	-e : rom to load
#	-b : ??
####################################

/usr/games/dolphin-emu