from setuptools import setup, find_packages


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=open("README.md").read(),

    packages=find_packages(exclude=('tests',)),
    install_requires=[],
)
