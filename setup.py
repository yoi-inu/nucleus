import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version:
    VERSION = version.read().strip()

setup(
    name="nucleus",
    version=VERSION,
    description="Template for standalone model-only django app",
    author="Abeer Upadhyay",
    author_email="ab.esquarer@gmail.com",
    url="https://github.com/esquarer/nucleus",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==1.11',
    ],
    zip_safe=False,
    keywords="django models package",
    classifiers=[
        'License :: MIT',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
