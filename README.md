# WebScraper

The code and jupyter notebook contained within this repository result from a second project during my AI and Data science bootcamp at BeCode (Brussels, Belgium).

## The aim of the project :

1. to create a self-contained development environment (env/conda)
2. to retrieve some information from an API
   - The API returns a list of countries
   - A list of past leaders per country
   - Each leader is described by some biographical data, and a link to their Wikipedia article
3. leveraging the data to scrape a website that does not provide an API
   - Obtaining the first paragraph from each leader
   - Cleaning the text from unexpected characters (e.g. references, phonetic notation, ...) using regex
   - Storing it in their dictionary
5. saving the output for later processing
   - Saving the result in a JSON file

## Files

1. Jupyter notebook - step by step guide to the project
2. Python scripts for the main function, and functions to obtain, clean and store the data
3. Package version of the software, wheel and source distributions

# Environment setup

You can create a virtual environment for the script using venv.
```shell
python -m venv C:\path\to\new\virtual\environment
```

Or using conda.
```shell
conda create --name <my-env>
conda activate <my-env>
```

Included in the repository is a cross-platform environment.yml file, allowing to create a copy of the one used for this project. The environment name is given in the first line of the file.
```shell
conda env create -f environment.yml
conda activate wikipedia_scraper_env
conda env list #verify the environment was installed correctly
```

# Running the scraper

Create a local copy of the repository by cloning and navigate to the directory using CLI. Running the following command runs the main.py script, scraping the web for requested data, and creating or overwriting an output in the results directory named leaders.json

```shell
python main.py
```

## Alternative

Go to the WebScraperPackage/WebScraperPackage directory, run following command in CLI to intall the package

```shell
pip install .
```
Run following commands to run the program

```shell
python 
```
```python
from main import main
main()
```

# Timeline

| Wednesday 06/11                                   | Thursday 07/11                                           |
| ------------------------------------------------- | -------------------------------------------------------- |
| Preparation of repository                         | Final compilation code snippets into functions           |
| Setting up virtual environment                    | Creating save function to export result to JSON          |
| Obtaining data from the API                       | Creating standalone python scripts                       |
| Obtaining and cleaning data from Wikipedia        | Create (small) testing suite                             |
|                                                   | Final adjustments, README, ...                           |
