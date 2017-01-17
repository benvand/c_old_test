"""
test a
"""
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages

version='1.0.0'

requirements = list(parse_requirements('requirements.txt',
                                       session=pip.download.PipSession()))
install_requires = [str(r.req) for r in requirements]

setup(
    name='c_old_test',
    version='1.0.0',
    url='https://github.com/benvand/c_old_test',
    license='MIT',
    author='benvand',
    description='A',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)