#!/usr/bin/python

import sys
import subprocess
import json
import string

# Gitp!
version = "0.1"
url = "https://github.com/SaguiTech/gitp/"


args = sys.argv

if len(args) < 2:
	print "Gitp version "+version+" - Making git more extensible! See more at "+url
	sys.exit(0)

args[0] = 'git'

gitp = json.load(open('gitp.json'))

def explode(str):
	return str.split(' ')

def execute(args):
	try:
		print subprocess.check_output(args)

	except subprocess.CalledProcessError as e:
		sys.exit(e.returncode)

def runTriggers(when):
	print '[Gitp] Executing triggers '+when+' "'+args[1]+'"...'

	for command in gitp[args[1]][when]:
		arrCommand = explode(command)
		print '[Gitp] Executing command "'+arrCommand[0]+'"...'
		execute(arrCommand)


if args[1] in gitp:
	actions = gitp[args[1]]

	if 'before' in actions:
		runTriggers('before')

	print '[Gitp] Executing "'+args[1]+'"...'
	execute(args)

	if 'after' in actions:
		runTriggers('after')

else:
	execute(args)