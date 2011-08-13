#!/usr/bin/env python

'''install.py: RetroGamez install script.'''

ROOT = os.pwd()


print "Hello, I'm RetroGamez Wizzard"

def findConf(soft):
	applications = {
		'dolphin-emu' : '',
		'gens' : ' ~/.gens/gens.cfg',
		'mupen64plus' : '',
		'fceux' : '~/.fceux/fceux.cfg',
		'pcsx2' : '',
		'pcsx' : '',
		'zsnes' : '~/.zsnes/zsnesl.cfg'
    }
    for app, confPath in applications.iteritems():
		if (app.find(app) > 0):
            return confPath
	print "CANT FIND CONFIGURATION"
    return ""


def linkConf(console)
	applications = {
		'gamecube' : 'dolphin-emu',
		'megadrive' : 'gens',
		'n64' : 'mupen64plus',
		'nes' : 'fceux',
		'psx2' : 'pcsx2',
		'psx' : 'pcsx',
		'snes' : 'zsnes'
    }
    for app, soft in applications.iteritems():
        if (app.find(app) > 0):
			# cd folder
			# getCon
			print findConf(soft)
	print "CANT FIND CONFIGURATION"
    return ""


'''
echo "* SETTINGS"
cd "./_settings"
ln -s /bin/bash
cd ".."
echo "####################################"

echo "* ZSNES"
cd ./snes/
ln -s ~/.zsnes/zsnesl.cfg
cd ".."
'''