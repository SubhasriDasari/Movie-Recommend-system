from setuptools import setup, find_packages

setup(
    name='movie_recommender',
    version='0.0.1',
    author='SUBHASRI DASARI',
    author_email='subhasridasari.01@gmail.com',
    description='A small example package for movies recommendation',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),  # ✅ This finds all valid packages automatically
    install_requires=['streamlit', 'requests', 'pandas', 'numpy', 'scikit-learn', 'nltk'],
    python_requires='>=3.7',
)

