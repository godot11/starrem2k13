from setuptools import setup, find_packages

setup(
    name='starrem2k13',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'starrem2k13': ['weights/*'],
    },
    install_requires=[
        'tensorflow',
        'numpy',
        'pillow',
        'tqdm',
        'tensorflowjs',
        'pyinstaller'
    ],
    author='Ashish Patil',
    # author_email='your.email@example.com',
    description='A ML based tool to remove stars from astronomical images.',
    url='https://github.com/code2k13/starrem2k13',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)