from setuptools import setup, find_packages

setup(
    name='mi_explorer',
    version='0.1.0',
    description='MIExplorerTest',

    author='pondelion',
    url='https://github.com/pondelion/MIExplorerTest',

    packages=find_packages(where='backend/mi_explorer'),
    package_dir={'': 'backend/mi_explorer'},

    install_requires=[],
    extras_require={},

    entry_points={
        'console_scripts': [
            'mi_explorer = mi_explorer'
        ]
    },
)