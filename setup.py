import sys
import os

from setuptools import setup, find_packages
import support
support.use("system")
support.set_package_name("minimuse")
from support.setup_codes import setup_commands

name = 'minimuse'
version = "0.0.1"
author = 'The Amuse/ Omuse/ Hymuse Team'
author_email = 'info@amusecode.org'
license_ = "Apache License 2.0"
url = 'http://www.github.com/eWaterCycle'
install_requires = [
    'wheel>=0.32',
    'docutils>=0.6',
    'numpy>=1.2.2',
    'nose>=0.11.1',
    'mpi4py>=1.1.0',
    'h5py>=1.1.0',
    'amuse-framework>=12.0.0rc3'
]
description = 'miniMUSE: a minimal example for a MUSE package'
with open("README.md", "r") as fh:
    long_description = fh.read()
long_description_content_type = "text/markdown"
classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: C',
    'Programming Language :: C++',
    'Programming Language :: Fortran',
]

extensions = []

all_data_files = []

packages = find_packages('src')

package_data = {
}

mapping_from_command_name_to_command_class=setup_commands()

setup(
    name=name,
    version=version,
    classifiers=classifiers,
    url=url,
    author_email=author_email,
    author=author,
    license=license_,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    install_requires=install_requires,
    cmdclass=mapping_from_command_name_to_command_class,
    ext_modules=extensions,
    package_dir = {'': 'src'},
    packages=packages,
    package_data=package_data,
    data_files=all_data_files,
)
