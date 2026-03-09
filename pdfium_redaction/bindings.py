import ctypes
import pathlib
import platform

pkg_dir = pathlib.Path(__file__).parent

if platform.system() == "Darwin":
    lib_path = pkg_dir / "libpdfium.dylib"
else:
    lib_path = pkg_dir / "libpdfium.so"

_pdfium = ctypes.CDLL(str(lib_path))

FPDFTextObj_RemoveChars = _pdfium.FPDFTextObj_RemoveChars