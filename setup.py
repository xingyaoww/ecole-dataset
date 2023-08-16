from setuptools import setup, find_packages

setup(
    name="ecole-dataset",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "datasets>=1.11.0",
    ],
    author="Xingyao Wang",
    author_email="xingyao6@illinois.edu",
    description="A unified dataset interface for ECOLE project.",
    url="https://github.com/xingyaoww/ecole-dataset",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
