import math
from rag import red, amber

globallist=dir()

def print_module_names():
	print("Names in the math module:")
	print(dir(math))
	print("\nNames in the current module:")
	print(globallist)


def print_dunder_values_for_module(mod):
	"""Print each dunder attribute name and its value for given module/object."""
	mod_name = getattr(mod, "__name__", repr(mod))
	print(f"\nDunder values for module {mod_name}:")
	for name in dir(mod):
		if name.startswith("__") and name.endswith("__"):
			try:
				value = getattr(mod, name)
			except Exception as exc:
				value = f"<error: {exc}>"
			print(f"{name}: {value!r}")


def print_dunder_values_current():
	"""Print dunder names from the current module and their values from globals()."""
	print("\nDunder values in current module:")
	for name in sorted(globallist):
		if name.startswith("__") and name.endswith("__"):
			value = globals().get(name, "<not found>")
			print(f"{name}: {value!r}")


if __name__ == "__main__":
	print_module_names()
	print_dunder_values_for_module(math)
	print_dunder_values_current()

