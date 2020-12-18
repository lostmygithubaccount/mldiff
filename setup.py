from pathlib import Path
from setuptools import setup

setup(
    name="mldiff",
    version=open(Path(__file__).parent.absolute().joinpath("mldiff", "VERSION")).read().strip(),
    description="diff data with ml",
    url="https://github.com/lostmygithubaccount/mldiff",
    author="Cody",
    author_email="cody.dkdc@gmail.com",
    license="MIT",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)
