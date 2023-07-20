# Selenium Web Scraping Project - University Student Exam Results

This repository contains a Python-based web scraping project using Selenium, designed to automate the process of fetching student exam results from my university's results page. The script navigates to the results page, enters the registration number of each student one by one, scrapes their name and grades, and finally exports the data into a CSV file for further analysis.

## Prerequisites

Before running the script, please ensure you have the following dependencies installed:

1. Python 3.x
2. Selenium package
3. Webdriver Manager package

## How to Use

1. Clone this repository to your local machine or download the project files.

2. Install the required packages if you haven't already by running:

```bash
pip install selenium webdriver-manager
```

3. Replace the url variable in the script with the working url for the particular results page you want to scrape. You can also modify the registration number range to suit your needs.

4. Run the script using:

```bash
python main.py
```

5. The script will start navigating to the results page, entering each student's registration number, scraping their name and grades, and storing the data in a list.

6. Once all the data is collected, the script will export it into a CSV file named `student_results.csv` in the same directory.

## Important Note

- Please use this web scraping script responsibly and in compliance with your university's policies and guidelines for web scraping.

- The script is designed to work with my university's results page. If you want to use it for a different website, you will need to modify the script accordingly.

- Be mindful of the website's terms of service and ensure that you are permitted to scrape data from it.

- Scraping multiple pages in quick succession may trigger security mechanisms on the website. Consider adding delays between requests to avoid potential issues.
