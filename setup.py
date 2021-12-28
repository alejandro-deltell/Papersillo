from distutils.core import setup
import py2exe, sys

sys.argv.append('py2exe')

options = {"py2exe": {
    "compressed": 1,  # Compresión
    "optimize": 2,
    "bundle_files": 1,  # Todos los archivos están empaquetados en un archivo exe
}}

setup(
    console=[{'script': "main.py", }],
    options=options,
    zipfile=None
)