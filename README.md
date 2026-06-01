# NeoStats-UseCase

## Overview

This repository contains an end-to-end data engineering and analytics pipeline for ABC Retail. The project demonstrates the complete data lifecycle: extracting raw sales data, transforming and curating it via Python (Jupyter Notebooks), generating Key Performance Indicators (KPIs), and visualizing the insights through an interactive Power BI dashboard.

## Repository Structure

- `Jupyter-Python.py` - Python scripts for data ingestion, cleaning, enrichment, revenue calculation, and export of curated results.
- `UseCase-neoStats.ipynb` - Jupyter notebook version of the analysis for interactive exploration and visualization.
- `NeoStats_dashboard.pbix` - Power BI dashboard file for visualizing KPI results from the processed data.
- `ABC_Retail_Data_Engineering_Report.docx` - Supporting report document for the retail data engineering use case.

## What the script does

`Jupyter-Python.py` performs the following steps:

1. Loads raw retail transaction datasets: `retail_data1.csv`, `retail_data2.csv`, and `product_details.csv`.
2. Combines transaction data into a single dataset.
3. Filters only successful payments and removes duplicate transactions.
4. Fills missing prices using the product master file.
5. Standardizes category names, product names, cities, payment methods, and customer names.
6. Removes invalid quantity records (quantity <= 0).
7. Masks customer email and phone values for privacy using SHA-256 hashing.
8. Calculates revenue per transaction and rounds currency values.
9. Joins standardized product metadata and exports curated results.
10. Generates summary KPIs and writes output CSV files:
   - `curated_retail_data.csv`
   - `kpi_by_category.csv`
   - `kpi_by_city.csv`

## Output files

The script saves the following outputs when it runs successfully:

- curated_retail_data.csv - cleaned and enriched retail transactions.
- kpi_by_category.csv - total revenue grouped by product category.
- kpi_by_city.csv - total revenue grouped by customer city.


## Visualizations

The notebook and script also include charting for:

- Revenue by product category
- Revenue by city
- Monthly revenue trend

## Tools Used

-  Python 3.x
- `pandas`
- `matplotlib`
- `seaborn`
-  powerBI


