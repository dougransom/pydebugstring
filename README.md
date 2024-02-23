# pydbugstring

Provides a function OutputDebugString to call:
    - on win32 platforms, calls the ctypes.windll.kernel32.OutputDebugStringW with any Python Object, after converting that object to a string.  
    - on other platforms, converts the argument to a string and discards it, returns 0

Provides a handler for the Python Logging Module which sends logging to OutputDebugString.  On platforms other than win32, the logging output is disccarded.


The output can be viewed using the [DebugView](https://learn.microsoft.com/en-us/sysinternals/downloads/debugview) program from the SysInternals  package from Microsoft.


# Sample Use

```
import  pydebugstring
import sys
import logging
#send an object to OutputDebugString
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(pydebugstring.OutputDebugStringHandler())
print(f"Sending sys.path [{sys.path}]  to outputDebugString")
pydebugstring.outputDebugString(sys.path)

debug_message = "Sample Debug Message"
print(f"Sending [{debug_message}] with logging.info")

logging.info(debug_message)

```
