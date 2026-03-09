import os
import pathlib
import platform

pkg_dir = pathlib.Path(__file__).parent

# locate bundled PDFium library
if platform.system() == "Darwin":
    lib_path = pkg_dir / "libpdfium.dylib"
else:
    lib_path = pkg_dir / "libpdfium.so"

# force pypdfium2 to use this binary
os.environ["PDFIUM_BINARY"] = str(lib_path)

# export function
from .bindings import FPDFTextObj_RemoveChars

__all__ = ["FPDFTextObj_RemoveChars"]