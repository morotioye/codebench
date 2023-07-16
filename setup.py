from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Codebench",
    version="1.0.0",
    author="Akella Research",
    author_email="moroti@akellaresearch.org",
    description="A package for benchmarking LMs on Programming Tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AkellaResearch/Codebench",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
