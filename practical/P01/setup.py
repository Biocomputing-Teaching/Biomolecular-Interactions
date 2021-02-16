import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_scrapy", 
    version="1.0.0",
    author="your_name",
    author_email="your_email",
    description="A Scrapy-based program for getting stuff from the internet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Biocomputing-Teaching/Biomolecular-Interactions/tree/P01/practical/P01",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
