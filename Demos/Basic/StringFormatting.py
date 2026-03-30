"""String formatting demos converted to functions.

Each original section is now a function that prints that section.
The `main()` function runs all sections using default sample values.
"""

def _sep():
	print("*" * 70 + "\n")


def sample_values():
	"""Return default sample values used by examples."""
	name = "Alice"
	age = 30
	num = 42
	large_num = 1000000
	pi = 3.14159
	percentage = 0.8567
	_sep()
	return name, age, num, large_num, pi, percentage


def basic_formatting(name="Alice", age=30, pi=3.14159):
	_sep()
	print(f"String: {name}")
	print(f"Integer: {age}")
	print(f"Float: {pi}")


def float_precision(pi=3.14159):
	_sep()
	print(f"2 decimal places: {pi:.2f}")
	print(f"No decimals: {pi:.0f}")
	print(f"3 decimal places: {pi:.3f}")


def width_and_alignment(num=42):
	_sep()
	print(f"Right aligned (width 5): '{num:>5}'")
	print(f"Left aligned (width 5):  '{num:<5}'")
	print(f"Center aligned (width 5):'{num:^5}'")


def zero_padding(num=42):
	_sep()
	print(f"Zero padded: {num:05}")


def sign_handling(num=42):
	_sep()
	print(f"Positive with sign: {num:+}")
	print(f"Negative with sign: {-num:+}")


def thousands_separator(large_num=1000000):
	_sep()
	print(f"With commas: {large_num:,}")


def percentage_format(percentage=0.8567):
	_sep()
	print(f"Percentage: {percentage:.2%}")


def number_bases(num=42):
	_sep()
	print(f"Binary: {num:b}")
	print(f"Octal: {num:o}")
	print(f"Hex (lower): {num:x}")
	print(f"Hex (upper): {num:X}")


def scientific_notation(large_num=1000000):
	_sep()
	print(f"Scientific (default): {large_num:e}")
	print(f"Scientific (2 decimals): {large_num:.2e}")


def general_format(large_num=1000000):
	_sep()
	print(f"General format: {large_num:g}")


def combined_example(name="Alice", age=30, pi=3.14159, num=42):
	_sep()
	print(f"Name: {name}, Age: {age}, Pi: {pi:.2f}, Number: {num:05}")


def main():
	name, age, num, large_num, pi, percentage = sample_values()
	basic_formatting(name, age, pi)
	float_precision(pi)
	width_and_alignment(num)
	zero_padding(num)
	sign_handling(num)
	thousands_separator(large_num)
	percentage_format(percentage)
	number_bases(num)
	scientific_notation(large_num)
	general_format(large_num)
	combined_example(name, age, pi, num)


if __name__ == "__main__":
	main()