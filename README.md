# NeoStats-UseCase

## Overview

NeoStats-UseCase is a retail data engineering and analytics project. It demonstrates how to ingest and clean transactional retail data, enrich it with product metadata, compute revenue KPIs, and build visualizations for business insights.

## Repository Structure

- Jupyter-Python.py - Main Python script for data ingestion, cleaning, enrichment, revenue calculation, and export of curated results.
- UseCase-neoStats.ipynb - Jupyter notebook with interactive analysis, visualization, and exploratory data work.
- NeoStats_dashboard.pbix - Power BI dashboard file for visualizing KPI results from the processed data.
- ABC_Retail_Data_Engineering_Report.docx - Supporting report document describing the retail data engineering use case.

## What the script does

Jupyter-Python.py includes the following processing steps:

1. Loads raw retail transaction data from 
etail_data1.csv, 
etail_data2.csv, and product_details.csv.
2. Combines transactions into a single dataset.
3. Filters for successful payments and removes duplicate transaction IDs.
4. Fills missing price values using the product master file.
5. Standardizes product categories, product names, cities, payment methods, and customer names.
6. Removes invalid rows where quantity <= 0.
7. Hashes customer email and phone data using SHA-256 for privacy.
8. Calculates transaction revenue and rounds numeric values.
9. Merges standardized product metadata and exports curated datasets.
10. Computes summary KPIs by category and city.

## Output files

The script saves the following outputs when it runs successfully:

- curated_retail_data.csv - cleaned and enriched retail transactions.
- kpi_by_category.csv - total revenue grouped by product category.
- kpi_by_city.csv - total revenue grouped by customer city.

## Visualizations

The notebook and script produce visualizations for:

- Revenue by product category
- Revenue by city
- Monthly revenue trend

## Requirements

- Python 3.8+ (or compatible 3.x version)
- pandas
- matplotlib
- seaborn

## Setup and usage

1. Install dependencies:

`powershell
pip install pandas matplotlib seaborn
`

2. Run the main preprocessing script from the project folder:

`powershell
python Jupyter-Python.py
`

3. Open UseCase-neoStats.ipynb in Jupyter Notebook or JupyterLab to explore the analysis interactively.

4. Open NeoStats_dashboard.pbix in Power BI Desktop for dashboard visualization.

## Notes

- Raw data files must be present in the same folder as Jupyter-Python.py for the script to run.
- The script expects columns such as 	ransaction_id, product_id, price, quantity, discount, payment_status, 	ransaction_date, category, city, email, and phone.
- If you want to extend the pipeline, update the script to include additional data quality checks, label mapping, or KPI exports.

## Contact

For improvements or questions, update the notebook or add more analysis in the Python script.
