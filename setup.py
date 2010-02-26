

from distutils.core import setup, Extension
from distutils.sysconfig import get_config_var
from distutils.extension import Extension

import os
import sys

# get the version loaded as vstr
execfile('ptsa/versionString.py')

# set up extensions
ext_modules = []
edf_ext = Extension("ptsa.data.edf.edf",
                    sources = ["ptsa/data/edf/edf.c",
                               "ptsa/data/edf/edfwrap.c",
                               "ptsa/data/edf/edflib.c"],
                    define_macros = [('_LARGEFILE64_SOURCE', None),
                                     ('_LARGEFILE_SOURCE', None)])
ext_modules.append(edf_ext)

# define the setup
setup(name='ptsa', 
      version=vstr, 
      maintainer=['Per B. Sederberg'],
      maintainer_email=['psederberg@gmail.com'],
      url=['http://ptsa.sourceforge.net'],
      packages=['ptsa','ptsa.tests','ptsa.data','ptsa.data.tests',
                'ptsa.plotting','ptsa.plotting.tests',
                'dimarray','dimarray.tests'],
      ext_modules = ext_modules
      )

