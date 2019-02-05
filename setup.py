from setuptools import setup, find_packages

requirements = [
    'pandas',
    'numpy',
    'scipy',
    'future',
    'marshmallow==3.0.0.b9'
]

setup(name='Superplus',
      version='1.0',
      description='Collection of simulation tools for performing MPC',
      author='Sam Currie',
      author_email='sam@sarocu.com',
      url='https:sarocu.com',
      packages=find_packages(),
     )