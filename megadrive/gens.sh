#!/usr/bin/env bash

####################################
# MEGADRIVE / GENESIS LAUNCHER
####################################
# Thanks to http://doc.ubuntu-fr.org/gens-gs

# launcher : gens
# manual : 
# romext : zip|bin|cue|iso|32x
# savegame : yes

# TODO:
#	- fix sound volume

# config : ~/.gens/gens.cfg 
#
# Prior to use Dolphin emulator with XBMC you need to use its GUI to modify some options. Into Options/Configure/Display menu:
# 	- Check "Start Renderer in Fullscreen" option
# 	- Check "Hide mouse cursor" option
# 	- Uncheck "Confirm on Stop" option
# 	- Into Options/Configure/Path menu select the directory where are located your iso files.

# command line options :
#	-fs : fullscreen
#	--quickexit 
# 	--disable-led
#	--disable-message
####################################

/usr/bin/gens --fs --quickexit --disable-led --disable-message "$1"

