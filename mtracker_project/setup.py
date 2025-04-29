from setuptools import setup, find_packages

setup(
    name='mtracker_project_yulya',
    version='1.0.0',
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
