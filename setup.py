LONG_DESCRIPTION = """

This package provides a Python tool for building visualizations of data related to 
the climate change all over the world and levels of pollutans in United States. 


"""

DESCRIPTION         = "Climate Police: Analysis and visualization of Climate change and its correlation with pollution"
NAME                = "Climate_Police"
PACKAGES            = ['Climate_Police',
                       'Climate_Police.data',
                       'Climate_Police.examples',
                       'Climate_Police.tests',
                       ]
PACKAGE_DATA        = {'Climate_Police': ['examples/*.ipynb']}
AUTHOR              = "Abhishek Sugam | Yuanqi Mao | Giovanni Sinapi"
AUTHOR_EMAIL        = "/"
URL                 = 'https://github.com/abhisheksugam/Climate_Police'
DOWNLOAD_URL        = 'https://github.com/abhisheksugam/Climate_Police'
LICENSE             = 'MIT'
INSTALL_REQUIRES    = ['ipython','pandas','plotly']


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name=NAME,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      install_requires=INSTALL_REQUIRES,
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
     )