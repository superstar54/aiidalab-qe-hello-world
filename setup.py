import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name="aiidalab-qe-hello-world",
    version="0.0.1",
    description="A aiidalab-qe plugin to calculate the equation of state of a crystal.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/superstar54/aiidalab-qe-hello-world",
    author="Xing Wang",
    author_email="xingwang1991@gmail.com",
    classifiers=[],
    packages=find_packages(),
    entry_points={
        "aiidalab_qe.properties": [
            "hello_world = aiidalab_qe_hello_world:property",
        ],
    },
    install_requires=[

    ],
    package_data={},
    python_requires=">=3.6",
)
