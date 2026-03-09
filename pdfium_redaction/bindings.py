import ctypes
import pathlib

# locate bundled PDFium library
lib_path = pathlib.Path(__file__).parent / "libpdfium.dylib"

# load your custom PDFium build
_pdfium = ctypes.CDLL(str(lib_path))

FPDFTextObj_RemoveChars = _pdfium.FPDFTextObj_RemoveChars
FPDFTextObj_RemoveChars.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
FPDFTextObj_RemoveChars.restype = None