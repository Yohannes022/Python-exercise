"""cs module: class scope demonstration module."""
mod_var = "module variable: mode_var"
def mod_func():
	return ("module level function: mod_func()")

class SuperClass:
	super_class_var = "Superclass class variable: self.super_class_var"
	__priv_super_class_var = "private superclass class variable: no access"
	def __init__(self):
		self.super_instance_var = "superclass instance variable: self.super_instance_var"
		self.__psiv = "pricate superclass instance variable: no access"
	def super_class_method(self):
		return ("superclass method: self.super_class_method()")
	def __superclass_priv_method(self):
		return ("superclass private method: no access")

class Class_(SuperClass):
	class_var = "class variable: self.class_var or Class_.class_var(for assignment)"
	__priv_class_var = "class private variable: self.__priv_class_var or Class_.__priv_class_var"

	def __init__(self):
		super().__init__(self)
		self.__priv_instance_var = "private instance variable: self.__priv_instance_var"
	def method_2(self):
		return "method: self.method_2"