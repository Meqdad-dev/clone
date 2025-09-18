from setuptools import setup, find_packages

setup(
    name="asciicat",
    version="1.0.0",
    description="Random ASCII Art Cat Generator",
    author="ASCIICAT Project",
    py_modules=['asciicat'],
    entry_points={
        'console_scripts': [
            'asciicat=asciicat:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)