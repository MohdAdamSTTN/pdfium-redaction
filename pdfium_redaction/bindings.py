import ctypes
import pathlib
import platform

pkg_dir = pathlib.Path(__file__).parent

# select correct library
if platform.system() == "Darwin":
    lib_path = pkg_dir / "libpdfium.dylib"
elif platform.system() == "Linux":
    lib_path = pkg_dir / "libpdfium.so"
else:
    raise RuntimeError("Unsupported platform")

_pdfium = ctypes.CDLL(str(lib_path))

# declare function
FPDFTextObj_RemoveChars = _pdfium.FPDFTextObj_RemoveChars

FPDFTextObj_RemoveChars.argtypes = [
    ctypes.c_void_p,  # FPDF_PAGEOBJECT
    ctypes.c_int,     # index
    ctypes.c_int      # count
]

FPDFTextObj_RemoveChars.restype = None