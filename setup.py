from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="SIEM-Simulator",
    version="0.1.0",  # Update the version number for new releases
    author="olof nuggets",
    description="A simple SIEM (Security Information and Event Management) data simulator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olofnuggts/logie",
    packages=find_packages(),
    install_requires=[
        "pymongo",  # Add other dependencies as needed
        "faker",  # Assuming Faker is used for generating log data
        "numpy",
        "joblib",
        "scikit-learn",
        # Add other dependencies as required by your project
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",  # Minimum version requirement of the python
)
f.close()
