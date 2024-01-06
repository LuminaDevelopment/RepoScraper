# Repository Scraper Tool 📜

This tool is designed to scrape and combine the text from all files in a GitHub repository into a single text file. It supports both cloning a repository directly from GitHub (Online Version) and processing a repository that has already been downloaded to your local machine (Offline Version).

### Prerequisites 📋

- Git must be installed on your system.
- Python 🐍 must be installed on your system.
- Ensure you have internet access and the necessary permissions to clone the target repository.

### Usage [online]🌐

1. Open `online-scraper.py` in your python development software (such as PyCharm)
2. Replace `https://github.com/GithubName/RepoName.git` with the URL of the GitHub repository you want to scrape.
3. Run the script: `python online-scraper.py`
4. The script will clone the repository and combine the contents of all files into `scraped.txt`.

### Usage [offline]🔍

1. download the repo that you want to scrape
2. Open `offline-scraper.py` in your python development software (such as PyCharm)
3. Replace `C:\Users\SomeRandomAssFolder\Downloads\YourDownloadedRepoFolder` with the path to the repo you want to scrape.
4. Run the script: `python offline-scraper.py`
5. all your shit should be scraped into a file called `scraped.txt` that is located in the same directory as the python script
