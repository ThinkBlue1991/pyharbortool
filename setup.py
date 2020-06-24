import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyharborsdk",
    version="0.1",
    author="zhangjx",
    author_email="1075495029@qq.com",
    description="SDK about harbor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThinkBlue1991/pyharbortool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
