from setuptools import setup, find_packages

setup(
    name="FlightPricePrediction",
    version="0.0.1",
    author="Mohan C C",
    author_email="mohancc91@gmail.com",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=[
        "flask",
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "joblib",
        "gunicorn"
    ]
)
