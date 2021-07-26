# pydbugstring

Provides a function to call Windows OutputDebugString with any Python Object.  
Here is the definition:

```
import ctypes
W32OutputDebugString = ctypes.windll.kernel32.OutputDebugStringW

def outputDebugString(to_show):
    """ 
    :param to_show: to_show
    :return: the value of W32OutputDebugString
    Sends a string representation of to_show to W32OutputDebugString 
    """
    return W32OutputDebugString(f"{to_show}")

outputDebugString("loaded pydebugstring")

```

The output can be viewed using the DebugView program from the SysInternals  package from Microsoft.



