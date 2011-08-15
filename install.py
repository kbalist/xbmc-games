#!/usr/bin/env python

'''install.py: RetroGamez install script.'''

import sys, os
from string import Template
from xml.dom.minidom import parse

TPLFILE  = 'advancedLaunchers.tpl.xml'
TPL  = os.path.join(os.getcwd(), TPLFILE)

print " => RetroGamez Wizzard <="



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
def install(root):
	if not os.path.isfile(TPL):
		error("NO TEMPLATE FOUND FOR CONF : ",TPLFILE)
		return False
	conffile = createXMLConf(root)
	checkXMLConf(conffile)
	


def createXMLConf(confpath):
	DEST = os.path.join(confpath,'advancedLaunchers.xml')

	f = open(TPL, 'r+')
	confTpl = f.read()
	newContent = Template( confTpl ).substitute( dict(path=confpath) )
	sortie = open( DEST, "w")
	sortie.writelines(newContent)
	sortie.close()
	
	if os.path.isfile(DEST):
		return DEST
	return False

def checkXMLConf(conffile):
	dom = parse(conffile)
	nodeToCheck = ['filename', 'application', 'thumb', 'fanart']
	for e in nodeToCheck:
		checkXMLNodeFileExist(dom, e)
	return True

def error(msg):
	print "[!] WARNING : ", msg
	return False



def checkXMLNodeFileExist(dom, search):
	app = dom.getElementsByTagName(search)
	for e in app:
		e = getXMLText(e)
		if not os.path.isfile(e):
			error("CAN'T FIND ", e)
			return False
	return True


def getXMLText(node):
	return node.childNodes[0].nodeValue


install(os.getcwd())

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