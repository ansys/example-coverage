import setuptools
import os
from io import open as io_open


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# loosely from https://packaging.python.org/guides/single-sourcing-package-version/
current_dir = os.path.abspath(os.path.dirname(__file__))

# Get version from version file
__version__ = None
version_file = os.path.join(current_dir, 'ansys', 'tools', 'example_coverage',
                            '_version.py')

with io_open(version_file, mode='r') as fd:
    # execute file from raw string
    exec(fd.read())


# find namespace packages
packages = []
for package in setuptools.find_namespace_packages(include='ansys*'):
    if package.startswith('ansys.tools.example_coverage'):
        packages.append(package)


setuptools.setup(
    name="ansys-tools-example-coverage",
    version=__version__,
    author='ANSYS, Inc.',
    maintainer_email="pyansys.core@ansys.com",
    description="Tools to assess the docstring examples coverage.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/pyansys/example-coverage",
    project_urls={
        "Bug Tracker": "https://github.com/pyansys/example-coverage/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=packages,
    python_requires=">=3.6",
)
