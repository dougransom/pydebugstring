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
