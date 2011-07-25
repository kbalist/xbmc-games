#!/usr/bin/env bash

####################################
# N64 LAUNCHER
####################################
# Thanks to http://www.gwenael.org/xbmc/index.php?title=Mupen64_Plus#Linux

# launcher : mupen64plus
# manual : man mupen64plus
# romext : z64|zip|n64|rom

# config : Launch it without any option to configure it using the GUI:
#	- go into Option/Configure
#	- Main Settings: Check "Always start in full screen mode" option.
#	- Plugins: Be sure that you to have selected a Graphic, an Audio and an Input plugin.
#	- Graphic Plugin: Uncheck the "FPS counter" option in the "Speed" box.
#	- Rom Browser: You must add the path where are stored your Nintendo 64 roms.


# command line options :
#	--nogui : Starts the emulator without a graphical frontend.
#	--noask : Do not prompt user if rom file is hacked or a bad dump.
#	--noosd : Disable onscreen display.
#	--fullscreen : Run emulator in fullscreen mode.
####################################

/usr/games/mupen64plus --nogui --noask --noosd --fullscreen "$1"