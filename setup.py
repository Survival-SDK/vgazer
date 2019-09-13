from setuptools import setup, find_packages

setup(
 name='vgazer',
 version='0.0',
 url='https://github.com/edomin/vgazer',
 license='CC0',
 author='Vasiliy Edomin',
 author_email='Vasiliy.Edomin@gmail.com',
 description='Tool for checking versions of various software',
 packages=find_packages(exclude=["samples"]),
 long_description=open('README.md').read(),
 zip_safe=False
)
