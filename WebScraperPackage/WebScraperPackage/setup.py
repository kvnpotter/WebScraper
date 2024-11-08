from setuptools import setup, find_packages

with open("App/README.md", "r") as f:
    long_description = f.read()

setup(author= "Kevin Potter",
      author_email= "kvn.potter@outlook.com",
      url= "https://github.com/kvnpotter/WebScraper",
      license= "MIT",
      description= "A package to scrape some data and save it",
      long_description= long_description,
      long_description_content_type="text/markdown",
      name= "WebScraperPackage",
      version= "0.1.0",
      package_dir={"": "app"},
      packages=find_packages(where="app"),
      install_requires=['requests >= 2.27.1', 'beautifulsoup4 >= 4.12.3','ipykernel >= 6.29.5'],
      extras_require= {
          "dev": [ 'pytest >= 7.4'],
      },
      python_requires= ">=3.13")