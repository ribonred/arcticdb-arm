from setuptools import setup, find_packages
import os

setup(
    name="arcticdb",
    version="5.4.0",
    description="ArcticDB - ARM64 Linux build",
    author="ribonred",
    author_email="ribonred@gmail.com",
    packages=find_packages(),
    python_requires=">=3.11",
    include_package_data=True,
    package_data={
        '': ['dist/arcticdb-0.0.0.dev0-cp311-cp311-linux_aarch64.whl'],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Topic :: Database",
    ],
)