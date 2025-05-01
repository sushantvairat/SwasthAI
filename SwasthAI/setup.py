from setuptools import setup, find_packages

setup(
    name="SwasthAI",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "speechrecognition==3.10.0",
        "pyttsx3==2.90",
    ],
    entry_points={
        "console_scripts": [
            "swasthai=swasthai.cli.cli:main",
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered healthcare platform for rural environments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SwasthAI",
    license="MIT",
)