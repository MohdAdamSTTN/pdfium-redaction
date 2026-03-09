import ctypes
import os

LIB_PATH = os.path.join(os.path.dirname(__file__), "libpdfium.so")

_pdfium = ctypes.CDLL(LIB_PATH)

FPDFTextObj_RemoveChars = _pdfium.FPDFTextObj_RemoveChars

FPDFTextObj_RemoveChars.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
]

FPDFTextObj_RemoveChars.restype = None