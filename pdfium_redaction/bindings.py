import ctypes

_pdfium = ctypes.CDLL(None)

FPDFTextObj_RemoveChars = _pdfium.FPDFTextObj_RemoveChars
FPDFTextObj_RemoveChars.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
FPDFTextObj_RemoveChars.restype = None