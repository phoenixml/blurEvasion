from core import utils
import os, importlib

def getout(path):
	utils.printf("Loading file", 'warn')
	try:
		getData = open(path, 'r')
		data = getData.read()
		getData.close()
		utils.printf("Loading data completed", 'good')
		return data
	except:
		utils.printf("Can not read file at {}".format(path), 'bad')

def writeout(data, path):
	utils.printf("Trying to write new data", 'warn')
	try:
		writeData = open(path, 'w')
		writeData.write(data)
		writeData.close()
		utils.printf("Data has been written", 'good')
	except:
		utils.printf("Error while writing data at {}".format(path), 'bad')

def build_exec(platform, architecture, srcPath, destPath, outname):
	if platform == 'windows':
		destPath += '{}.exe'.format(outname)
	else:
		destPath += outname
	build_cmd = {
		'windows': {
			'x86': 'i686-w64-mingw32-gcc {} -o {} -mwindows'.format(srcPath, destPath),
			'x64': 'x86_x64-w64-mingw32-gcc {} -o {} -mwindows'.format(srcPath, destPath)
		},
		'linux': {
			'x86': 'gcc {} -o {} -m32 -static'.format(srcPath, destPath),
			'x64': 'gcc {} -o {} -static'.format(srcPath, destPath)
		}
#		['android', 'davik', 'command']
	}
	utils.printf("Generating build command", 'warn')
	try:
		build_cmd = build_cmd[platform][architecture]
		os.popen(build_cmd)
		utils.printf("Build completed at {}".format(destPath), 'good')
	except:
		utils.printf("Wrong building command. Check your options", 'bad')

def evade(platform, tech, method, data, filename):
	evade_method = "{}_{}".format(method, platform)
	evade_tech = importlib.import_module("evasion.{}".format(tech))
	evade_run = getattr(evade_tech, evade_method)(data, filename)
	return evade_run.run()
