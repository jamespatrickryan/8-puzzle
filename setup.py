import pathlib
from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='8_puzzle',
    version='1.0.0',
    description='CSC173 2022-2023 Intelligent Systems',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jamespatrickryan/8-puzzle',
    author='James Patrick Ryan A. Pasaforte',
    author_email='jamespatrick.pasaforte@g.msuiit.edu.ph',
    packages=find_packages()
)
