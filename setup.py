import os
import setuptools

with open('README.md', 'r') as fh:

    long_description = fh.read()

with open('requirements.txt', 'r') as fh:

    requirements = fh.read().splitlines()

setuptools.setup(
    name='litebase',
    version=os.getenv('VERSION'),
    author='Victor Martins',
    author_email='victor.martins.dpaula@gmail.com',
    description='All in one python backend',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'litebase = litebase.cli:main',
        ],
    },
)