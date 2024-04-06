from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kgcPy',
    version='1.1.3',
    keywords=['KoppenGeiger'],
    description='Aids in identifying the Koeppen-Geiger (KG) climatic zone for a given lat and lon of any location',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://engineering.case.edu/centers/sdle/',
    author='Xuanji Yu, Chelsey Bryant, Nicholas R. Wheeler, Franz Rubel, Julian Ascencio Vasquez, Roger H. French',
    author_email='xuanjiy@bu.edu, clb117@case.edu, nrw16@case.edu, franz.rubel@vetmeduni.ac.at, julian.ascencio@envision-digital.com, rxf131@case.edu',
    project_urls={'Documentation':'https://kgcpy-doc.bitbucket.io/'},

    # BSD 3-Clause License:
    # - http://choosealicense.com/licenses/bsd-3-clause
    # - http://opensource.org/licenses/BSD-3-Clause
    license='BSD License (BSD-3)',
    packages=find_packages(),
    include_package_data=True,
)