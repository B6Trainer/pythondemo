import utils.constants.distances

print("Inch to centimetre: %.4f" % utils.constants.distances.INCH_TO_CM)
print("Mile to kilometre: %.4f" % utils.constants.distances.MILE_TO_KM)

from utils.constants import distances

print("Inch to centimetre: %.4f" % distances.INCH_TO_CM)
print("Mile to kilometre: %.4f" % distances.MILE_TO_KM)

from utils.constants.distances import INCH_TO_CM, MILE_TO_KM

print("Inch to centimetre: %.4f" % INCH_TO_CM)
print("Mile to kilometre: %.4f" % MILE_TO_KM)


from utils.messages import *

print("Hello in French: %s" % utils.messages.french.HELLO)
print("Goodbye in French: %s" % utils.messages.french.GOODBYE)
print("Hello in Norwegian: %s" % utils.messages.german.HELLO)
print("Goodbye in Norwegian: %s" % utils.messages.german.GOODBYE) 