import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepwto",
    version="0.0.4",
    author="zcryoon",
    author_email="syyun@snu.ac.kr",
    description="DeepWTO Database API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepWTO/deepwto-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires='>=3.6',
)

