from setuptools import setup, find_packages

setup(
    name="FlightPricePrediction",
    version="0.0.1",
    author="Mohan C C",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
