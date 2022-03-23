from setuptools import setup ,find_packages

setup(
    name='Mypackage',
    version='O.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('readme.md').read(),
    author='<Nkosingiphile>',
    url='https://githup.com/<username>/<package-name>',
    author_email='<ndlovungiphiles@gmail.com>'
)