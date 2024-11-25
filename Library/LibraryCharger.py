import ctypes , ctypes.util
from ctypes import WinDLL

library = ctypes.util.find_library("./Library")
if not library:
    print("Library not found1")

try:
    lib = ctypes.CDLL(library)
    print("Library loaded")
    lib_test = lib.printHello()
except Exception as e:
    print("Error loading library2" + str(e))