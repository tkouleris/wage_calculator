# Wage Calculator

A Flask-based web application that predicts the monthly income for software professionals using a machine learning model. The calculator considers various factors such as experience, education, location, job roles, and specific technologies to provide an estimated wage.

## Installation Guide

Follow these steps to set up and run the application locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tkouleris/wage_calculator.git
   cd wage_calculator
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:5000/`.

---

# Wage Calculator - Model & Training

This project provides a wage calculator based on a machine learning model that predicts the monthly income for software professionals.

## Model Overview

The prediction engine uses a **Random Forest Regressor**, an ensemble learning method that operates by constructing a multitude of decision trees at training time and outputting the mean prediction of the individual trees.

- **Model Type**: Random Forest Regressor
- **Estimators**: 200 trees
- **Random State**: 42 (for reproducibility)

## Training Process

The model was trained using a dataset (`data.csv`) containing various professional and personal attributes.

### 1. Data Preprocessing
- **Duplicate Removal**: Any duplicate columns in the dataset are removed during loading.
- **Handling Missing Values**: A `SimpleImputer` with a **median** strategy is used to fill in missing values in the feature set.
- **Feature Selection**: The target variable is `Yearly Income`. All other columns are treated as features, including professional experience, education, gender, job roles, and specific technologies.

### 2. Dataset Split
The data was split into training and testing sets to evaluate the model's performance:
- **Training Set**: 80%
- **Testing Set**: 20%

### 3. Evaluation Metrics
The model is evaluated using the following metrics:
- **Mean Absolute Error (MAE)**: Measures the average magnitude of errors in the predictions.
- **R² Score**: Indicates how well the model explains the variability of the target data.

## Features

The model takes into account the following categories of information:
- **Demographics & Location**: Gender, Company HQ location.
- **Company Profile**: Company size.
- **Professional Background**: Years of experience, Education level, Team leadership status.
- **Work Mode**: Remote, On-site, or Hybrid.
- **Job Roles**: Over 40 specific roles (e.g., Backend, Frontend, Data Science, DevOps).
- **Technologies**: Over 50 programming languages and tools (e.g., Python, Java, React, SQL, AWS).

## Prediction & Output

The model predicts the **Yearly Income**. To provide a more relevant figure for the user, the application calculates the **Monthly Wage** by dividing the yearly prediction by **14** (standard practice in many European jurisdictions like Greece, accounting for 12 monthly salaries plus holiday/Christmas bonuses).

## Usage

To retrain the model:
1. Ensure `training/data.csv` is present.
2. Run the training script:
   ```bash
   python training/trainer.py
   ```
This will generate `income_model.pkl` and `imputer.pkl`, which are used by the calculator.
