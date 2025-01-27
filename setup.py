from setuptools import setup, find_packages

setup(
    name="perf_cprofiler",
    version="0.1.0",
    author="Ahmad Alwareh",
    author_email="ahmadalwareh8@gmail.com",
    description="A lightweight profiling utility for sync and async functions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ahmadalwareh/perf_cprofiler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
