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
    install_requires=[
        "numpy",
        "pandas",
        "attrs",
        "dataclasses",
        "protobuf>=3.5.0.post1,<6",  # Per https://github.com/grpc/grpc/blob/v1.45.3/requirements.txt
        "msgpack>=0.5.0",  # msgpack 0.5.0 is required for strict_types argument, needed for correct pickling fallback
        "pyyaml",
        "packaging",
    ]
)