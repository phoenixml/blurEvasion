import socket

def ipv4(address):
	try:
		socket.inet_pton(socket.AF_INET, address)
	except AttributeError:
		try:
			socket.inet_aton(address)
		except socket.error:
			print "Invalid IP address"
		if address.count('.') == 3:
			return address
		else:
			print "Invalid IP address format"
	except socket.error:
		print "Invalid IP address"
	return address

def platform(usrPlatform):
	platform = ['windows', 'linux', 'android']
	if usrPlatform not in platform:
		print "Invalid platform! Platform must be {}. Set to default ({})".format(', '.join(platform), platform[0])
	return platform[0]

def port(usrPort):
	try:
		int(usrPort)
		return usrPort
	except:
		print "Port must be an int number. Use default value ({})".format('4444')
		return '4444'

def arch(usrArch):
#	arch = {
#		'windows': ['x86', 'x64'],
#		'linux': ['x86', 'x64'],
#		'android': ['davik']
#	}
	arch = ['x86', 'x64'] #edit here, each platform has own arches
	if usrArch not in arch:
		print "Invalid Arch! Arch must be {}, set to default ({})".format(', '.join(arch), arch[0])
	return arch[0]
