from setuptools import setup

setup(
    py_modules=['test'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'testcli = test:cli',
        ],
    },
)
