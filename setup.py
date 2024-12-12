from setuptools import setup, find_packages

setup(
    name="password-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": ["pytest"]
    },
)