from setuptools import find_packages, setup

with open('README.md') as r:
    readme = r.read()

setup(
    name='calculator',
    version="0.0.1",
    description='Simple memory-based calculator',
    long_description=readme,
    packages=find_packages(exclude=('tests')),
    install_requires=[], 
    extras_require={
        'test': ['pytest'],
    },
)
