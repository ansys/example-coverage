import setuptools
import os

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# loosely from https://packaging.python.org/guides/single-sourcing-package-version/
current_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_dir, "src", "pyaedt", "version.txt"), 'r') as f:
    version = f.readline()


setuptools.setup(
    name="example-coverage",
    version="0.0.1",
    author='ANSYS, Inc.',
    author_email="maxime.rey@ansys.com",
    description="Tools to assess the docstring examples coverage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pyansys/example-coverage",
    project_urls={
        "Bug Tracker": "https://github.com/pyansys/example-coverage/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
