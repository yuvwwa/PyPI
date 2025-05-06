from setuptools import setup, find_packages

setup(
    name='mtracker_yulya_maria',
    version='1.0',
    description='Mtracker',
    license='MIT',
    long_description='Provides a decorator for memory usage tracking. The part of FOSS course.',
    long_description_content_type='text/markdown',
    author='Yulia Kravtsova',
    author_email='yuvwwa@gmail.com',
    url='https://github.com/yuvwwa/PyPI.git',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'test': ['pytest', 'coverage']
    },
    python_requires='>=3.6',
)
