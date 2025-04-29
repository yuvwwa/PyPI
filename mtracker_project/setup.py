from setuptools import setup

import json
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def read_dependencies(fname):
    filepath = path.join(here, fname)
    with open(filepath) as piplock:
        content = json.load(piplock)
        return [dependency for dependency in content.get('default')]

setup(
    name='mtracker-project-yulya',
    version='1.0.1',
    description='Provides a decorator for memory usage tracking. The part of FOSS course.',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yulia Kravtsova',
    author_email='yuvwwa@gmail.com',
    url='https://github.com/yuvwwa/PyPI.git',
    packages=['mtracker'],
    install_requires=[],
    extras_require={
        'test': ['pytest', 'coverage']
    },
    python_requires='>=3.6',
)
