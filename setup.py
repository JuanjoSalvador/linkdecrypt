from setuptools import setup, find_packages

setup(name='linkdecrypt',
      version='0.0.1',
      install_requires = [
            "beautifulsoup4",
            "certifi",
            "chardet",
            "click",
            "idna",
            "requests",
            "urllib3",
      ],
      entry_points = {
        'console_scripts': ['linkdecrypt=LinkDecrypt.main:main'],
      },
      url='https://github.com/juanjosalvador/linkdecrypt',
      download_url = 'https://github.com/juanjosalvador/linkdecrypt/archive/0.0.1.tar.gz',
      license='MIT',
      author='Juanjo Salvador',
      author_email='juanjosalvador@netc.eu',
      description='Decrypt Adf.ly URLs in batch mode',
      packages=find_packages(exclude=['tests']),
      zip_safe=False)