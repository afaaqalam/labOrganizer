#!/usr/bin/python

import os, sys, shutil, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--lab', '-l', help='specify lab sections', required=True, action='append')
parser.add_argument('--dest', '-d', help='specify destination folder', required=True, action='store')
parser.add_argument('--src', '-s', help='specify source folder', required=True, action='store')
args = parser.parse_args()

if not os.path.exists(args.dest):
	print('Incorrect destination path')
	sys.exit()

args.lab = list(set(args.lab))
print(args.lab)

if not os.path.exists(args.src):
	print('Incorrect source path')
	sys.exit()

sections = {}
for sec in args.lab:
	sections[sec] = args.dest+"/"+sec

if args.src:
	if not os.path.exists(args.src):
		print('Incorrect source path')
		sys.exit()
else:
	source = raw_input('Enter source path: ')
	if not os.path.exists(source):
		print('Incorrect source path')
		sys.exit()			

allFiles = os.listdir(os.getcwd())
allFiles = [files for files in allFiles if files.endswith('.py')]
count = 0

for sec in sections:
	destination = sections[sec]
	if not os.path.exists(destination):
		os.makedirs(destination)
	for f in allFiles:
		if sec in f:
			count += 1
			source = args.src + "/" + f
			shutil.copy(source, destination) 
	print('Copied {} files to {}'.format(count, destination))	
	count = 0			
