from setuptools import setup, find_packages

setup(
    name="cli_tools",
    version="1.0.0",
    author="Tim Perdue",
    author_email="timaperduejr@gmail.com",
    description="A collection of Python scripts that function as utility command-line tools",
    url="https://github.com/yourusername/unix-tools",
    packages=find_packages(),  # Automatically find packages in the project
    py_modules=["tools.tree"],  # Specify standalone modules if tools are not in packages
    install_requires=[],  # List dependencies here if required (e.g., argparse, etc.)
    entry_points={
        "console_scripts": [
            "treey=tools.treey:main",  # Command `tree` runs the `main` function in `tools/tree.py`
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify minimum Python version
)
