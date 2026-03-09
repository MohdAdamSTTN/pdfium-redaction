import os
import pathlib

# locate bundled PDFium library
lib_path = pathlib.Path(__file__).parent / "libpdfium.dylib"

# tell pypdfium2 to use this library
os.environ["PDFIUM_BINARY"] = str(lib_path)