#   Copyright 2017 ProjectQ-Framework (www.projectq.ch)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os

from setuptools import setup, find_packages

# This reads the __version__ variable from projectq/_version.py
exec(open('src/fermilib/_version.py').read())
# Readme file as long_description:
long_description = open('README.rst').read()
# Read in requirements.txt
requirements = open('requirements.txt').readlines()
requirements = [r.strip() for r in requirements]


setup(
    name='fermilib',
    version=__version__,
    author='FermiLib developers',
    author_email='fermilib@projectq.ch',
    url='http://www.projectq.ch',
    description=('FermiLib - '
                 'An open source package for analyzing, compiling and '
                 'emulating quantum algorithms for simulation of fermions.'),
    long_description=long_description,
    install_requires=requirements,
    license='Apache 2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        '': [os.path.join('src', 'fermilib', 'data', '*.hdf5'),
             os.path.join('src', 'fermilib', 'data', '*.npy')]
    }
)
