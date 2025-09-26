EDA Assignment – Sales Data Analysis
This project is part of DS Assignment 4 for Exploratory Data Analysis (EDA). The goal is to extract, clean, and analyze sales data to identify business insights, trends, and patterns.

Project Structure

DSassignment4/

EDA - Module 3 (1).zip → Contains problem statement and dataset.
main.py → Python script with full analysis.
Outputs → Console prints & visualizations (Matplotlib).


Features Implemented

Extract Problem Statement
Reads .docx problem statement from a .zip archive.


Load and Explore Data
Extracts and loads Excel file (DS Internship - EDA - Data.xlsx) using pandas.
Displays first few rows for quick inspection.


Sales Analysis

Total Sales by Year (bar chart).
Total Sales by Super Division (bar chart).
Total Sales by State (top 3 states for new stores).
Sales Trend by Month (line chart).
Store Lifecycle Analysis
Stores opened in 1991.
Number of remodelled stores.
Number of closed vs active stores.
Closures grouped by Outlet Type (bar chart).
Correlation Analysis
Relationship between Sales and Store Size (Sq. Ft.) (scatter plot).
Store Size Analysis
Average Sq. Ft. by Super Division (bar chart).
Identify division with largest average store size.



Insights Generated

Best-performing years, months, and states.
Most profitable Super Division.
Trends in store openings, remodels, and closures.
Impact of store size on sales.



Key opportunities for expansion and optimization.

Technologies Used

Python
pandas → Data manipulation
matplotlib → Visualizations


zipfile & python-docx → Extracting problem statement



How to Run

Clone the repository:

git clone https://github.com/shishita01/EDAassignment.git
cd EDAassignment


Install dependencies:

pip install pandas matplotlib python-docx openpyxl



Results

The analysis provides insights into:
Top-performing states for expansion.
Best months for launching new stores.
Store lifecycle (openings, remodels, closures).
Relationship between sales and store size.
