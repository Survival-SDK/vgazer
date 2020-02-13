from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
 name="vgazer",
 version="0.0.0",
 url="https://github.com/edomin/vgazer",
 license="CC0",
 author="Vasiliy Edomin",
 author_email="Vasiliy.Edomin@gmail.com",
 description="Library for checking versions and installing various software",
 #long_description=long_description,
 #long_description_content_type="text/markdown",
 packages=find_packages(exclude=["samples"]),
 install_requires=[
  "requests",
  "bs4",
 ],
 classifiers=[
  "Development Status :: 2 - Pre-Alpha",
  "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
  "Natural Language :: English",
  "Operating System :: POSIX :: Linux",
  "Programming Language :: Python :: 3",
  "Topic :: Software Development :: Build Tools",
 ],
 zip_safe=False
)
