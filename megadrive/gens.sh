#!/usr/bin/env bash

####################################
# MEGADRIVE / GENESIS LAUNCHER
####################################
# Thanks to http://doc.ubuntu-fr.org/gens-gs

# launcher : gens
# manual : 
# romext : zip|bin|cue|iso|32x|gen|smd

# config : ~/.gens/gens.cfg 
#
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

#tricks to reduce volume level
amixer -c 0 sset Master,0 30%
/usr/bin/gens --fs --quickexit --disable-led --disable-message "$1"
amixer -c 0 sset Master,0 100%
