# -*- coding: utf-8 -*-
import readline, os
import utils
from controller import GLOBAL_OPTS

class AutoCompleter(object):
	def __init__(self):
		self.setup()

	def setup(self):
		readline.set_completer(self.complete)
		readline.parse_and_bind('tab: complete')
		readline.set_completer_delims(' \t\n;')
		readline.parse_and_bind('set enable-keypad on')

	def complete(self, text, state):
		if state == 0:
			original_line = readline.get_line_buffer()
			line = original_line.lstrip()
			stripped = len(original_line) - len(line)
			start_index = readline.get_begidx() - stripped
			end_index = readline.get_endidx() - stripped

			if start_index > 0:
				cmd, args = self.parse_line(line)
				if cmd == '':
					complete_func = self.completer
				else:
					try:
						complete_func = getattr(self, 'complete_' + cmd)
					except:
						complete_func = self.completer
			else:
				complete_func = self.raw_command_completer
			self.completion_matches = complete_func(text, line, start_index, end_index)
		try:
			return self.completion_matches[state]
		except:
			return None
	# raw_command_group
	def raw_command_completer(self, text, line, start_index, end_index):
		return filter(lambda entry: entry.startswith(text), self.suggested_commands())
	
	def suggested_commands(self, *ignored):
		return [command.rsplit("_").pop() for command in dir(self) if command.startswith("command_")]
	# end raw_command_group
	def completer(self, *ignored):
		return []

	def parse_line(self, cmd_line):
		#split args and command
		cmd, _,  arg = cmd_line.strip().partition(" ")
		return cmd, arg.strip()
	
	def get_command_handler(self, command):
		#call command and execute command
		try:
			command_handler = getattr(self, 'command_{}'.format(command))
			return command_handler
		except AttributeError:
			utils.printf('Unknow command: {}!'.format(command), 'bad')
			return None
		#return command_handler
	
	def run(self):
		print(self.banner)
		while True:
			try:
				cmd, args = self.parse_line(raw_input(self.prompt()))
				if not cmd:
					continue
				command_handler = self.get_command_handler(cmd)
				if command_handler:
					command_handler(args)
				else:
					pass
			except KeyboardInterrupt:
				pass


	
class Interface(AutoCompleter):
	main_help = '''Main commands:
	exit					exit framework
	help					print help banner
	search	<text>				search modules
	show	<modules/platforms/evasions>	show module list
	use	<module>			use a module'''

	module_help = '''Module commands:
	info					show module information
	options					show module options
	run					execute this module
	set	<option>    <value>		set value for option
	unset	<option>    <value>		remove current value for option'''


	def __init__(self):
		super(Interface, self).__init__()
		self.current_module = None
		self.target = None
		self.module_path = None
		self.main_modules_dir = [module for module in os.listdir(utils.module_dir) if not module.startswith("__")]
		self.modules = utils.all_modules()
		self.show_commands = ['modules', 'evasions', 'options', 'info', 'platforms']
		self.main_commands = ['exit', 'help', 'search ', 'show ', 'use ']
		self.module_commands = ['info', 'options', 'show ', 'run', 'set ', 'unset ', 'back']
		self.banner = '''
   |\\                     /)
 /\\_\\\\__               (_//\t\tBlurEvasion
|   `>\\-`     _._       //`)\tFUD PAYLOAD GENERATOR
 \\ /` \\\\  _.-`:::`-._  //
  `    \\|`    :::    `|/\t\tTesting version
        |     :::     |\t\tAuthor: dmknght
        |.....:::.....|\t\thttps://github.com/dmknght/blurEvasion
        |:::::::::::::|
        |     :::     |\t\tSpecial thanks to: Diego Cornacchini
        \\     :::     /\t\thttps://github.com/oddcod3/Phantom-Evasion/
         \\    :::    /
          `-. ::: .-'
           //`:::`\\\\
          //   '   \\\\
         |/         \\\\
'''
		self.run()

	def suggested_commands(self):
		if self.current_module:
			return self.module_commands + self.main_commands
		else:
			return self.main_commands

	def prompt(self):
		if self.current_module:
			using_module = self.module_path
		else:
			using_module = 'blurEvasion'
		return '\n\033[91m┌──[\033[0m' + os.getcwd() + '\033[91m]─[\033[0m\033[97m' + using_module + '\033[0m\033[91m]\n└──╼\033[0m \033[94m$\033[0m '
#==== Show commands
	@property
	def module_metadata(self):
		return getattr(self.current_module, "_{}__info__".format(self.current_module.__class__.__name__))

	def _show_all(self, root_dir = ''):
		for module in [module for module in self.modules if module.startswith(root_dir)]:
			print(module.replace('.', os.sep))

	def _show_modules(self, root_dir = ''):
		self._show_all()

	def _show_info(self, *args, **kwargs):
		self.command_info()
	
	def command_show(self, *args, **kwargs):
		sub_command = args[0]
		try:
			getattr(self, "_show_{}".format(sub_command))(*args, **kwargs)
		except AttributeError:
			utils.printf("Unknown show \'{}\'!\nTry: show {}".format(sub_command, self.show_commands), 'bad')
#	End show commands

### === Complete commands
	def command_quit(self, *args, **kwargs):
		self.command_exit()

	def complete_show(self, text, *args, **kwargs):
		if text:
			return [command for command in self.show_commands if command.startswith(text)]
		else:
			return self.show_commands

	def complete_use(self, text, *args, **kwargs):
		if text:
			return self.modules_completion(text)
		else:
			return self.main_modules_dir

	def modules_completion(self, text):
		text = utils.python_path(text)
		all_matches = filter(lambda x: x.startswith(text), self.modules)
		matches = set()
		for match in all_matches:
			head, sep, tail = match[len(text):].partition('.')
			if not tail:
				sep = ""
			matches.add("".join((text, head, sep)))
		return list(map(utils.normal_path, matches))

	def complete_set(self, text, *args, **kwargs):
		if text:
			return [' '.join((attr, "")) for attr in self.current_module.options if attr.startswith(text)]
		else:
			return self.current_module.options

### === End of completion commands

### === Execute command

	def command_help(self, *args, **kwargs):
		print('\n' + self.main_help)
		if self.current_module:
			print('\n' + self.module_help)

	def command_search(self, *args, **kwargs):
		for arg in args:
			matches = [s for s in self.modules if arg in s]
		for match in matches:
			print(match.replace('.', '/'))

	def command_back(self, *args, **kwargs):
		self.current_module = None

	def command_exit(self, *args, **kwargs):
		utils.printf("Stopped!", 'bad')
		exit(0)
	
	def command_use(self, module_path, *args, **kwargs):
		if not module_path:
			utils.printf("Use something??", 'warn')
		else:
			self.module_path = module_path
			module_path = utils.python_path(module_path)
			module_path = '.'.join(('modules', module_path))
			try:
				self.current_module = utils.import_module(module_path)()
			except:
				utils.printf("Error while loading module", 'bad')

	def command_run(self, *args, **kwargs):
		utils.printf("Module is running", 'warn')
		try:
			self.current_module.run()
		except KeyboardInterrupt:
			utils.printf("Operation cancelled by user", 'warn')
		except:
			utils.printf("Error while using module", 'bad')

	def _show_options(self, *args, **kwargs):
		self.command_options()

	def _show_evasions(self, *args, **kwargs):
		headers = ("Name", "Platform", "Description")
		info = [
			["MHA", "Windows / Linux", "[PhantomEvasion] Multipath HeapAlloc (C)"],
			["MVA", "Windows", "[PhantomEvasion] Multipath VirtualAlloc (C)"],
			["Polymorphic_MHA", "Windows / Linux", "[PhantomEvasion] Polymorphic HeapAlloc (C)"],
			["Polymorphic_MVA", "Windows", "[PhantomEvasion] Polymorphic VirtualAlloc (C)"]
		]
		utils.print_table(headers, *info)
		print('')

	def _show_platforms(self, *args, **kwargs):
		headers = ("Name", "Architecture", "Description")
		info = [
			["windows", "x86 / X64", ""],
			["linux", "x86 / x64", ""],
#			["android", "davik", "Android mobile system"],
#			["osx", "x86 / x64", ""]
		]
		utils.print_table(headers, *info)
		print('')

	@utils.module_required
	def command_options(self, *args, **kwargs):
		module_opts = [opt for opt in self.current_module.options]
		headers = ("Name", "Current Settings", "Description")
		print("Target options: \n")
		utils.print_table(headers, *self.get_opts(*module_opts))
		print('')

	@utils.module_required
	def get_opts(self, *args):
		for opt_key in args:
			try:
				opt_description = self.current_module.module_attributes[opt_key]
				opt_value = getattr(self.current_module, opt_key)
			except (KeyError, AttributeError):
				pass
			else:
				yield opt_key, opt_value, opt_description

	@utils.module_required
	def command_info(self, *args, **kwargs):
		utils.print_dict(
			self.module_metadata,
			("name", "description", "authors", "references"),
		)

	@utils.module_required
	def command_set(self, *args, **kwargs):
		variable, _, value = args[0].partition(' ')
		if variable in self.current_module.options:
			setattr(self.current_module, variable, value)
			if kwargs.get("glob", False):
				GLOBAL_OPTS[variable] = value
			print({variable: value})
		else:
			utils.printf("You can't set option {}.\nAvaliable options: {}".format(variable, self.current_module.options), 'bad')

	def complete_set(self, text, *args, **kwargs):
		if text:
			return [' '.join((attr, "")) for attr in self.current_module.options if attr.startswith(text)]
		else:
			return self.current_module.options
# End of execute command

