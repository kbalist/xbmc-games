#!/usr/bin/env python

import libxml2, sys, os
from string import Template
from xml.dom.minidom import parse


ROOT = os.getcwd()
TPL  = os.path.join(ROOT,'advancedLaunchers.tpl.xml')
DEST = os.path.join(ROOT,'advancedLaunchers.xml')
DICO = dict(path=ROOT)

def getText(node):
	return node.childNodes[0].nodeValue

def readConf(filePath):
	if not os.path.isfile(filePath):
		return False
	f = open(TPL, 'r+')
	return f.read()
	
def writeConf(content):
	sortie = open( DEST, "w")
	sortie.writelines(content)
	sortie.close()

def checkConf():
	dom = parse(DEST)
	checkFileFromXML(dom, 'filename')
	checkFileFromXML(dom, 'application')

def checkFileFromXML(dom, search):
	app = dom.getElementsByTagName(search)
	for e in app:
		e = getText(e)
		if not os.path.isfile(e):
			print "[!] WARNING : CAN'T FIND ",e

def updateConf():
	confTpl = readConf(TPL)
	
	newConfTpl = Template( confTpl ).substitute( DICO )
	writeConf(newConfTpl)
	checkConf()

updateConf()
