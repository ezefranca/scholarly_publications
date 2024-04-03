from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '0.4'

setup(
    name='scholarly_publications',
    version=version,
    description='A tool to fetch scholarly publications from Google Scholar by author ID',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ezefranca/scholarly_publications',
    author='Ezequiel França',
    author_email='ezequiel.franca@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='scholarly publications google scholar fetcher academia',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'scholarly_publications=scholarly_publications.cli:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/ezefranca/scholarly_publications/issues',
        'Source': 'https://github.com/ezefranca/scholarly_publications',
    },
)