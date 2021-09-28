from setuptools import setup, find_packages

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="ParseRawHTTP",
    version='1.0',
    description="Load HTTP request from a raw HTTP request",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bronya-Rayi/ParseRawHTTP",
    author="Rayi",
    author_email='931470970@qq.com',
    license='MIT',
    platforms=["all"],
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    keywords='ParseRawHTTP'
)
