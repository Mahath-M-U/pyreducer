from setuptools import setup
from pathlib import Path

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
      name='pyreducer',
      version='0.0.15',
      description='package for optimize common task ',
      url='https://github.com/Mahath-M-U/pyreducer',
      author='Mahath M U',
      author_email='mahathmu@outlook.com',
      license='GNU GPL v3',
      packages=['pyreducer'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False
      )