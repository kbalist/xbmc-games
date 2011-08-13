#!/usr/bin/env python

import os
from string import Template



def updateConf():
	tpl = 'advancedLaunchers.xml.tpl'
	dest = 'advancedLaunchers.xml'
	
	ROOT = os.getcwd()
#	print ROOT
	
	f = open(tpl, 'r+')
	confTpl = f.read()
#	print contents
	
#	f = open('/tmp/workfile', 'r+')
#	>>> f.write('0123456789abcdef')
	
#	confTpl = '<application>${path}_settings/bash</application>'

	template = Template(confTpl)
	
#	print confTpl
#	print confTpl%{"path": ROOT}
	print template.substitute(dict(path=ROOT))



updateConf()