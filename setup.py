from setuptools import setup, find_packages

setup(
 name='vgazer',
 version='0.0',
 url='https://github.com/edomin/vgazer',
 license='CC0',
 author='Vasiliy Edomin',
 author_email='Vasiliy.Edomin@gmail.com',
 description='Tool for checking versions of various software',
 packages=find_packages(exclude=['tests']),
 long_description=open('README').read(),
 zip_safe=False
)
