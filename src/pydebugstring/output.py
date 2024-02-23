import ctypes
from sys import platform
if platform == "win32":
    W32OutputDebugString = ctypes.windll.kernel32.OutputDebugStringW 
else:
    def W32OutputDebugString(arg):
        """Dummy function as an alternative to W32OutputDebugString in case code using this module 
         is run on platfomrs other than win32.  W32OutputDebugString does nothing, returns 0.
        """
        return 0

def outputDebugString(to_show):
    """ 
    :param to_show: to_show
    :return: the value of W32OutputDebugString
    Sends a string representation of to_show to W32OutputDebugString 
    """
    return W32OutputDebugString(f"{to_show}")

outputDebugString("loaded pydebugstring")
