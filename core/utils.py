import os, importlib, sys
from functools import wraps

from abc import ABCMeta, abstractmethod

import modules as module_path

module_dir = module_path.__path__[0]

def all_modules(main_path = module_dir):
	list_module = []
	for root, dirs, files in os.walk(main_path):
		_, package, root = root.rpartition('modules/'.replace('/', os.sep))
		root = root.replace(os.sep, '.')
		files = filter(lambda x: not x.startswith("__") and x.endswith('.py'), files)
		list_module.extend(map(lambda x: '.'.join((root, os.path.splitext(x)[0])), files))
	return list_module
	# search and list all module

def python_path(path):
	# convert path to module syntax
	return path.replace('/', '.')

def normal_path(path):
	# convert python path to normal path
	return path.replace('.', '/')


def import_module(path):
	try: #edit here, add try, remove comments
		module = importlib.import_module(path)
		return getattr(module, 'Payload')
	except:
		printf("Can not import {}".format(normal_path(path)), 'bad')
		return False

def printf(msgText, msgType):
	msgText = {
		'bad': '\033[91m{}\033[00m\n'.format(msgText),
		'warn': '\033[93m{}\033[00m\n'.format(msgText),
		'good': '\033[92m{}\033[00m\n'.format(msgText)
	}
	print(msgText[msgType])
	

def print_dict(dictionary, order = None):
	order = order or ()

	def prettyprint(title, body):
		print("\n{}:".format(title.capitalize()))
		if not isinstance(body, str):
			for value_element in value:
				print('- ', value_element)
		else:
			try:
				print(value)
			except:
				print('')

	keys = dictionary.keys()
	for element in order:
		try:
			key = keys.pop(keys.index(element))
			value = dictionary[key]
		except (KeyError, ValueError):
			pass
		else:
			prettyprint(element, value)

	for rest_keys in keys:
		prettyprint(rest_keys, dictionary[rest_keys])


def module_required(fn):
	@wraps(fn)
	def wrapper(self, *args, **kwargs):
		if not self.current_module:
			printf("You have to active module with use command", 'bad')
			return
		return fn(self, *args, **kwargs)
	try:
		name = 'module_required'
		wrapper.__decorators__.append(name)
	except AttributeError:
		wrapper.__decorators__ = [name]
	return wrapper

def print_table(headers, *args, **kwargs):
	extra_fill = kwargs.get("extra_fill", 5)
	header_separator = kwargs.get("header_separator", "-")
	if not all(map(lambda x: len(x) == len(headers), args)):
		printf("Error headers", 'bad')
		return
	def custom_len(x):
		try:
			return len(x)
		except TypeError:
			return 0
	fill = []
	headers_line = '   '
	headers_separator_line = '   '
	for idx, header in enumerate(headers):
		column = [custom_len(arg[idx]) for arg in args]
		column.append(len(header))
		current_line_fill = max(column) + extra_fill
		fill.append(current_line_fill)
		headers_line = "".join((headers_line, "{header:<{fill}}".format(header = header, fill = current_line_fill)))
		headers_separator_line = "".join((
			headers_separator_line,
			'{:<{}}'.format(header_separator * len(header), current_line_fill)
		))
	print(headers_line)
	print(headers_separator_line)
	for arg in args:
		content_line = '   '
		for idx, element in enumerate(arg):
			content_line = "".join((
				content_line,
				'{:{}}'.format(element, fill[idx])
			))
		print(content_line)

class NonStringIterable:
	__metaclass__ = ABCMeta
	@abstractmethod
	def __iter__(self):
		while False:
			yield None
	@classmethod
	def __subclasshook__(cls, C):
		if cls is NonStringIterable:
			if any("__iter__" in B.__dict__ for B in C.__mro__):
				return True
		return NotImplemented

