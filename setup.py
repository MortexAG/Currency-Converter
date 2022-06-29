from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name="Currency-Converter",
    version="0.0.1",
    author="MortexAG",
    author_email="ahmedgouda100@gmail.com",
    description="Currency Converter That Works With All Currencies",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/MortexAG/Currency-Converter/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
