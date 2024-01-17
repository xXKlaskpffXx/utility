from setuptools import find_packages, setup

setup(
    name='utilitj',
    packages=find_packages(include=['utilitj']),
    version='0.1.0',
    description='some simple utility functions',
    author='LesterNich',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)