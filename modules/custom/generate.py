
from core import controller, utils
from libs import actions

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
	evasion_method = controller.Options('MHA', 'Evasion method. Usage :show evasions')
	output_name = controller.Options('evil', 'Name of output executable file')

	def run(self):
		try:
			data = actions.getout(self.source)
			data = actions.evade(self.platform, self.evasion_tech, self.evasion_method, data, self.output_name)
		# Get new data, start writing to output file
			if self.destination[-1] != '/':
				self.destination += '/'
			output_payload = self.destination + 'output.c'

			actions.writeout(data, output_payload)
			# Write done!, start building exe file
			actions.build_exec(self.platform, self.architecture, output_payload, self.destination, self.output_name)
		except:
			utils.printf("Error while running module", 'bad')
