from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "SUBHASRI DASARI"
AUTHOR_EMAIL = "subhasridasari.01@gmail.com"  # <-- fix email format
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small example package for movies recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[SRC_REPO],  # <-- Use find_packages instead of manually specifying list
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)
