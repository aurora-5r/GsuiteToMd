import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='GsuiteToMd',
    version='0.1',
    author='Laurent Maumet',
    author_email='laurent@aurora-5r.fr',
    url='https://github.com/laurentmau/GsuiteToMd',
    description='Tools to convert gsuite Documents to markdown',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License : : OSI Approved : : GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    python_requires='>=3.6',

)
