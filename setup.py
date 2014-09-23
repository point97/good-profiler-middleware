import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme: 
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='good-profiler-middleware',
    version='0.0.1',
    packages=['good'],
    include_package_data=True,
    license='TBD',
    description='Good Profiler Middleware for Django',
    long_description=README,
    author='Seth Hill',
    author_email='sethrh@gmail.com',
    classifiers=[
        'Environment :: Web Development',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: TBD',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
