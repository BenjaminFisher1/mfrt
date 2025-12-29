from setuptools import setup, find_packages

setup(
    name='Mass-File-Renamer-Tool',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click>=8.3.0',
    ],
    entry_points={
        'console_scripts': [
            'Mass-File-Renamer-Tool = Mass-File-Renamer-Tool.cli:main',
        ],
    },
)