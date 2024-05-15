# setup.py

from setuptools import setup, find_packages

setup(
    name='country-coordinates',
    version='0.2',
    packages=find_packages(),
    author='Emmanuel Gyimah Annor',
    author_email='eannor707@gmail.com',
    description='Get longitude and latitude coordinates of countries that you can use with xarray.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Annor-Gyimah/country_coord',  
    keywords=['python','coordinates','countries'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
