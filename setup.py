from setuptools import setup, find_packages

setup(
    name="scholarly_publications",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points='''
        [console_scripts]
        scholarly_publications=scholarly_publications.cli:main
    ''',
)