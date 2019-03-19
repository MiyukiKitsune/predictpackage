from setuptools import setup, find_packages

setup(
    name='predictpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Predict python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/MiyukiKitsune/predictpackage',
    author='Charne Nieuwoudt',
    author_email='friesian22@gmail.com'
)
