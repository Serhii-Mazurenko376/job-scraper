# Job Scraper - RemoteOK

This Python script scrapes remote job listings from [RemoteOK](https://remoteok.com/) and saves them into a CSV file.

## Features

- Extracts:
  - Job Title
  - Company
  - Location
  - Job Link
- Saves all results to `jobs.csv`
- Uses `requests`, `BeautifulSoup`, and `csv`

## How to Run

1. Make sure you have Python 3 installed.
2. Install dependencies (if needed):

   ```bash
   pip install requests beautifulsoup4
   ```
3.	Run the script:
    ```bash
    python remoteok_scraper.py
    ```
4.	Check the jobs.csv file in the same folder.
## Built With
	- Python 3
	- BeautifulSoup
	- RemoteOK

## License

Free to use for educational and portfolio purposes.
