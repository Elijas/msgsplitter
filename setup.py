import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='msgsplitter',
    version='1.0.1',
    author="Elijas Dapšauskas",
    author_email="master.elijas@gmail.com",
    description="Split messages (strings) to fit an arbitrary character limit",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/Elijas/msgsplitter",
    platforms="Any",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
