
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


requires = [
    'websocket-client>=0.53.0', 
    'requests>=2.22.0'

]
test_requirements = ['pytest>=3']


setuptools.setup(
    name='bybit_sdk',  
    version='0.1',
    scripts=['setup'] ,
    author="ApiTrader",
    author_email="printingpresstrader.one@gmail.com",
    description="A library to interact with the Bybit APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ApiTrader/BybitSDK",
    packages=['bybitsdk'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=requires,
    tests_require=test_requirements,
 )

# setup.py sdist bdist_wheel
