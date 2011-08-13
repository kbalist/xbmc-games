#!/usr/bin/env bash

####################################
# NES LAUNCHER
####################################
# Thanks to http://www.gwenael.org/xbmc/index.php?title=FCEUX#Linux
# 			http://forums.gentoo.org/viewtopic-t-637583-start-0.html

# launcher : fceux
# manual : man fceux
# romext : zip|nes

# config : ~/.fceux/fceux.cfg
#	- SDL.SoundVolume = 90 : Sound Volume Level [0..100]
#   - SDL.Fullscreen = 1 : Autostart FCEUX in fullscreen 
#	- SDL.Frameskip = 0
#	- SDL.GameGenie = 0

# To quit FCEUX emulator using the ESC key you have to edit ~/.fceux/fceux.cfg 
# and put the SDL.Hotkeys.Quit value equal to 27.
#	SDL.Hotkeys.Pause = 19
#	SDL.Hotkeys.Quit = 27
#	SDL.Hotkeys.Reset = 292

# command line options :
#	--fullscreen 1 
#   --autoscale 1 
#   --volume 90 
#   --soundq 1 
#   --input1 gamepad1 
#   --input2 gamepad2
####################################

/usr/bin/fceux --fullscreen 1 --autoscale 1 --volume 90 --soundq 1 --input1 GamePad.0 --input2 GamePad.1 "$1"