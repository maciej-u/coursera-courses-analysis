# Data Visualization with Python: Project

## Overview

This project is a comprehensive analysis of the Coursera Course Dataset. The analysis includes data cleaning, exploratory data analysis (EDA), and visualisation to uncover insights about courses offered on Coursera. The primary tools used are Python, Pandas, Matplotlib, and Seaborn.

## Objectives

1. **Data Cleaning**: Preparing the dataset for analysis by removing unnecessary columns, handling missing values, and converting data types.
2. **EDA and Visualisation**: Gaining insights into the dataset by performing descriptive statistics, visualising data distributions, and analysing correlations.

## Repository Structure
```
├── .gitignore                         # Git ignore file
├── 00_Data_Cleaning.ipynb             # Jupyter notebook for data cleaning
├── 01_EDA_and_Visualisations.ipynb    # Jupyter notebook for exploratory data analysis and visualisations
├── DA_PY_3_5.ipynb                    # Project description and requirements
├── README.md                          # Project overview and documentation
├── convert_num_function.py            # Custom function for numeric conversion
├── coursea_data.csv                   # Original dataset
├── coursea_data_cleaned.csv           # Cleaned dataset ready for analysis
├── outliers_function.py               # Custom function for handling outliers
```

## Datasets

- `coursea_data.csv`: The original Coursera Course Dataset.
- `coursea_data_cleaned.csv`: The cleaned dataset after performing data cleaning steps.

## Notebooks

### `00_Data_Cleaning.ipynb`

This notebook covers the initial phase of the project, where the dataset is prepared for analysis:
- Loading the dataset
- Inspecting the dataset
- Removing unnecessary columns
- Converting data types
- Handling missing values
- Saving the cleaned dataset

### `01_EDA_and_Visualisations.ipynb`

This notebook performs exploratory data analysis and visualisations on the cleaned dataset:
- Importing the cleaned dataset
- Performing initial inspections
- Generating descriptive statistics
- Creating visualisations for categorical and numerical variables
- Analysing correlations between numerical variables
- Summarising key insights

## Scripts

### `convert_num_function.py`

This script contains custom functions used for numeric conversion in the data cleaning process.

### `outliers_function.py`

This script contains custom functions used for handling outliers in the exploratory data analysis and visualisation process.

## Key Findings

1. **Course Organization**: The dataset includes a diverse set of course providers, with top contributors accounting for a significant portion of course offerings.
2. **Certificate Types**: The most common certificate type is "COURSE".
3. **Course Difficulty**: "Beginner" courses are the most common, followed by "Intermediate" and "Mixed".
4. **Course Ratings**: Course ratings are generally high, with a median rating of 4.7 out of 5.
5. **Student Enrollments**: There is a wide range of enrollments, with most courses having relatively lower enrollments and a few courses having exceptionally high enrollments.

## Requirements

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Libraries and Versions
- pandas == 2.2.2
- matplotlib == 3.9.0
- seaborn == 0.13.2

## Acknowledgements

- The dataset used in this project is from [Kaggle: Coursera Course Dataset](https://www.kaggle.com/datasets/siddharthm1698/coursera-course-dataset).
