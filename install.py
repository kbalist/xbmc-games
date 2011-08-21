#!/usr/bin/env python

'''install.py: RetroGamez install script.'''

import sys, os
from string import Template
from xml.dom.minidom import parse

TPLFILE  = 'advancedLaunchers.tpl.xml'
TPL  = os.path.join(os.getcwd(), TPLFILE)

print " => RetroGamez Wizzard <="




def browseEmulator(emulator):
	print emulator

	path = os.path.join(GAMESPATH, emulator)
	u = os.listdir(path)
	if EMULAUNCHER not in u:
		print "  No launcher Found at : ", os.path.join(path, EMULAUNCHER)

	if EMUCONFIG in u:
		print "  OK config found at : ", os.path.join(path, EMUCONFIG)

	if 'extra' in u:
		pass
#		print 'getExtras'
#	print u

def browseAllEmulators(root):
	if not os.path.isdir(root):
		return False

	emulators = []
	u = os.listdir(root)
	for e in u:
		if os.path.isdir( os.path.join( root, e ) ) and e not in DIRBLACKLIST:
#			if query_yes_no("Add " + e + " to emulator Scan ?", default = "yes"):
#				emulators.append(e)
			emulators.append(e)

	for emulator in emulators:
		browseEmulator(emulator)


''''''
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

def linkConf(console):
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
			print findConf(soft)
	print "CANT FIND CONFIGURATION"
	return ""

''''''
def install( root = os.getcwd() ):
	if not os.path.isfile(TPL):
		error("NO TEMPLATE FOUND FOR CONF : ",TPLFILE)
		return False
	conf = os.path.join( root, 'advancedLaunchers.xml')
	if not os.path.isfile(conf):
		print "CREATE CONF FROM TEMPLATE" + conf
		conf = createXMLConf(conf)
	print "CHECK CONF : " + conf
	checkXMLConf(conf)

def createXMLConf(configFile):
	
	f = open(TPL, 'r+')
	confTpl = f.read()
	newContent = Template( confTpl ).substitute( dict(path=os.getcwd()) )
	
	sortie = open( configFile, "w")
	sortie.writelines(newContent)
	sortie.close()
	
	if os.path.isfile(configFile):
		return configFile
	return False

def checkXMLConf(conffile):
	dom = parse(conffile)
	#fileNode = ['filename', 'application', 'thumb', 'fanart']
	fileNode = ['filename', 'application']
	for e in fileNode:
		checkXMLNodeFileExist(dom, e)



############### LOW LEVEL ###############

def error(msg):
	print "[!] WARNING : ", msg
	return False

def checkXMLNodeFileExist(dom, search):
	app = dom.getElementsByTagName(search)
	for e in app:
		e = getXMLText(e)
		if not os.path.isfile(e):
			error("CAN'T FIND "+ e)


def getXMLText(node):
	return node.childNodes[0].nodeValue

def query_yes_no(question, default="yes"):
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

############### LOW LEVEL ###############

if len(sys.argv) < 2:
	install()
else:
	install()


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