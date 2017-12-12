import validators
from itertools import chain
from utils import NonStringIterable
from weakref import WeakKeyDictionary #edit here, maybe delete

GLOBAL_OPTS = {}

class Options(object):
	def __init__(self, default, description = "", validators = ()):
		self.label = None
		if isinstance(validators, NonStringIterable):
			self.validators = validators
		else:
			self.validators = (validators,)
		self.default = default
		self.description = description
		self.data = WeakKeyDictionary() #edit here, maybe delete

	def __get__(self, instance, owner):
		try:
			return self.data[instance]
		except KeyError:
			pass
		try:
			return self._apply_widgets(GLOBAL_OPTS[self.label])
		except KeyError:
			return self.default

	def __set__(self, instance, value):
		self.data[instance] = self._apply_widgets(value)

	def _apply_widgets(self, value):
		for validator in self.validators:
			value = validator(value)
		return value

class ModuleOptionsAggregator(type):
	""" Metaclass for module base class.

	Metaclass is aggregating all possible Attributes that user can set
	for tab completion purposes.
	"""
	def __new__(cls, name, bases, attrs):
		try:
			base_module_attributes = chain(map(lambda x: x.module_attributes, bases))
		except AttributeError:
			attrs['module_attributes'] = {}
		else:
			attrs['module_attributes'] = {k: v for d in base_module_attributes for k, v in d.iteritems()}

		for key, value in attrs.iteritems():
			if isinstance(value, Options):
				value.label = key
				attrs['module_attributes'].update({key: value.description})
			elif key == "__info__":
				attrs["_{}{}".format(name, key)] = value
				del attrs[key]
			elif key in attrs['module_attributes']:  # Removing module_attribute that was overwritten
				del attrs['module_attributes'][key]  # in the child and is not a Option() instance.
		return super(ModuleOptionsAggregator, cls).__new__(cls, name, bases, attrs)


class Module(object):
	""" Base class for modules. """

	__metaclass__ = ModuleOptionsAggregator
	# edit here if needed
	# needs add platform, evasion_type,architecture
#	platform = Options(default = "windows", description = "Target platform", validators = validators.platform)
	#global_test = Options("test", "test")
	
	@property
	def options(self):
		""" Returns list of options that user can set.

		Returns list of options aggregated by
		ModuleOptionsAggregator metaclass that user can set.

		:return: list of options that user can set
		"""
		return self.module_attributes.keys()

	def run(self):
		raise NotImplementedError("You have to define your own 'run' method.")
