#!/usr/bin/env python

import os
from string import Template


ROOT = os.getcwd()
TPL  = os.path.join(ROOT,'advancedLaunchers.tpl.xml')
DEST = os.path.join(ROOT,'advancedLaunchers.xml')
DICO = dict(path=ROOT)


def updateConf():
	if not os.path.isfile(TPL):
		return False
				
#	if os.path.isfile(DEST)
	
	f = open(TPL, 'r+')
	confTpl = f.read()
	
	newConfTpl = Template( confTpl ).substitute( DICO )
	
	sortie = open( DEST, "w")
	sortie.writelines(newConfTpl)
	sortie.close()
	
#	print newConfTpl






	
	g = open(DEST, 'r+')
	g.write(newConfTpl)
		
#	confTpl = '<application>${path}/_settings/bash</application>'

#	template = Template(confTpl)
#	replace = template.substitute(dict(path=ROOT))

updateConf()
