from setuptools import setup, find_packages

setup(
    name='mfrt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click>=8.3.0',
    ],
    entry_points={
        'console_scripts': [
            'mfrt = mfrt.cli:main',
        ],
    },
)