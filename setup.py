from setuptools import setup, find_packages

setup(
    name='metroconv',
    version='1.0',
    packages=find_packages(),
    url='',
    license='BSD',
    author='Zoltan Kozma',
    author_email='zoltan@miracode.co.uk',
    description='Metro Bank CSV  to FreeAgent CSV converter',
    entry_points = {
        'console_scripts': [
            'metroconv = metroconv.scripts.main:main'
        ]
    }
)
