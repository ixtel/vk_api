__author__ = "Kirill Python"
__version__ = "1.1"
__email__ = "mikeking568@gmail.com"
__contact__ = "https://vk.com/python273"


import sys
if sys.version_info[0] == 2:
    from jconfig import *
else:
    from .jconfig import *
