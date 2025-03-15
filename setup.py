from setuptools import setup, find_packages

setup(
    name="malware-detector",
    version="0.1.0",
    description="A CLI tool to detect malware in files.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "python-magic",
        "oletools",
        "yara-python",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "malware-detector=malware_detector.cli:main",
        ],
    },
)