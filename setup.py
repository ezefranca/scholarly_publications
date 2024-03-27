from setuptools import setup, find_packages

setup(
    name="scholarly_publications",
    version="0.2",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points='''
        [console_scripts]
        scholarly_publications=scholarly_publications.cli:main
    ''',
)