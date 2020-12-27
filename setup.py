"""
Simple setup for the mcrflash library using also
setuptools scm to tag published versions
"""
from setuptools import setup, find_packages

MINIMAL_REQUIREMENTS = []
with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="mcrflash",
    use_scm_version={
        "write_to": "mcrflash/_mcrflash_version.py",
        "write_to_template": '__version__ = "{version}"\n',
    },
    description="This module provides version parsing and rendering",
    long_description=readme,
    author="Roberto Ciatti",
    license="MIT",
    url="https://github.com/timequarter/mcrflash",
    packages=find_packages(exclude=["tests", "tests.*"]),
    data_files=[("", ["LICENSE"])],
    install_requires=MINIMAL_REQUIREMENTS,
    zip_safe=False,
    keywords=["micro", "flash"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
