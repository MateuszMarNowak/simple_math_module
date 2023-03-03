from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Simple math module'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="simple_math", 
        version=VERSION,
        author="Wocek",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'simple math'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)