import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='service_monitor',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'celery'
    ]
)
