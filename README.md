# Turkey Inflation Rate Analysis Project

## Introduction

This project aims to investigate the inflation rates in Turkey and compare them with the percentage increase in prices for young generations' daily purchases. The project involves web scraping, data cleaning, analysis, visualization and ML.

## Requirements

- Python 3.8 or later.
- The following Python libraries installed:
  Pandas: For data handling and manipulation
  NumPy: For numerical calculations
  Matplotlib: For plotting and visualisation
  Seaborn: For advanced plotting and visualisation
  Plotly: For creating interactive plots
  Scikit-Learn: For machine learning tasks like clustering
  SciPy: For scientific computations such as distance calculation

- Selenium and ChromeDriver:
  Selenium is used for automating web applications for testing purposes. You should have Google Chrome installed and ChromeDriver configured for Selenium to work. You can download ChromeDriver from the official site.

## Files

- `cimriScript.py`: A script that uses Selenium to extract the required data from the target website. (www.cimri.com)
- `cimriScript.py`: A script that uses Selenium to extract the required data from the target website. (www.cimri.com)
- `data_analysis.py`: A script that imports, cleans, analyzes, and visualizes the data.
- `cimriProducts.csv`: CSV file containing the product data gathered from the target website. (www.cimri.com)
- `akakceProducts.csv`: CSV file containing the product data gathered from the target website. (www.akakce.com)
- `cimriLinks.txt`: Text file containing the relative URLs of the products to be scraped from the target website. (www.cimri.com)
- `akakceLinks.txt`: Text file containing the relative URLs of the products to be scraped from the target website. (www.akakce.com)
- `requirements.txt`: A text file that contains the neccessary pip install versions.
- `chromedriver.exe`: An executable file for selenium dynamic web scraping to work.

## How to Run

1. Clone the repository.

   ```bash
   git clone https://github.com/aydinaydemir/CS210_Project.git
   ```

2. Install the necessary Python packages.

   ```bash
   pip install -r requirements.txt
   ```

3. Run the data collection script to gather data. This will update `akakceProducts.csv` and `cimriProducts.csv` with the latest product data.

   ```bash
   python akakceScript.py
   ```

   ```bash
   python cimriScript.py
   ```

4. Run the data analysis script to analyze and visualize the gathered data.
   ```bash
   python data_analysis.py
   ```

## Project Details

The project starts with data collection using Selenium to scrape product data, including product name, category, old and current prices, and the date of the price check from a given website. The scraped data is stored in a CSV file.

The data is then cleaned and analyzed. This process involves handling missing values, duplicated rows, and type conversions. A detailed exploratory data analysis is carried out to gain insights from the data, which is followed by data visualization.

The goal is to assess the inflation rates by looking at the price changes of daily purchases and comparing them with the official inflation rates in Turkey.

## Contributors

<center>
Aydın Aydemir<br>
İrem Kök<br>
Baran Pekkolay<br>
Göktuğ Korkulu<br>
Yağız Ay<br>
Doğa Anık<br>
</center>
