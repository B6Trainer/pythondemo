import importlib.util
import os

# Load SimpleFunctions.py from the original folder with spaces in its name
_base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '04 - Functions'))
_simple_path = os.path.join(_base, 'SimpleFunctions.py')

spec = importlib.util.spec_from_file_location(__name__ + '.SimpleFunctions', _simple_path)
_sf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_sf)

# expose as package attribute so callers can do `from functions import SimpleFunctions`
SimpleFunctions = _sf

__all__ = ['SimpleFunctions']
