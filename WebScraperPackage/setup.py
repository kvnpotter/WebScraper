from setuptools import setup, find_packages

setup(
    author="Kevin Potter",
    description="A package to scrape some data and save it",
    name="WebScraperPackage",
    version="0.1.0",
    packages=find_packages(include=["WebScraperPackage", "WebScraperPackage.*"]),
    install_requires=["requests", "beautifulsoup4", "pytest", "ipykernel"],
)
