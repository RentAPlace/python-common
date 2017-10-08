from setuptools import (find_packages, setup)

from rap import common

setup(
    name=common.__pkgname__,
    description=common.__description__,
    version=common.__version__,
    packages=["rap.common"]
)
