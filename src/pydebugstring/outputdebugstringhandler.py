import logging

from  pydebugstring.output import outputDebugString
class OutputDebugStringHandler(logging.Handler):
    """
    OutputDebugStringHandler sends logging output via the Windows OutputDebugStringW function.
    The Output can be viewed in DebugView https://learn.microsoft.com/en-us/sysinternals/downloads/debugview
    """
    def emit(self,arg):
        outputDebugString(arg)
        return True

if __name__ == "__main__":
    import sys
    print("foo")
    l=logging.getLogger()
    h1=OutputDebugStringHandler()
    h2=logging.StreamHandler(sys.stdout)
    l.setLevel(logging.DEBUG)
    for h in [h1,h2]:
       l.addHandler(h)
    logging.info("Sample message, you should see it on sys.stdout and in DbgView.exe\nhttps://learn.microsoft.com/en-us/sysinternals/downloads/debugview")
