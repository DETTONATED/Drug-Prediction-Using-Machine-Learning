## Project Overview
This project predicts the most suitable drug for a patient based on medical attributes such as Age, Sex, Blood Pressure (BP), Cholesterol Level, and Sodium-to-Potassium Ratio (Na_to_K). The objective is to build a classification model that can recommend the appropriate drug category for a patient.

## Dataset
The project uses the Drug200 Dataset containing patient information and prescribed drug labels.

### Features
- Age
- Sex
- BP (Blood Pressure)
- Cholesterol
- Na_to_K (Sodium-to-Potassium Ratio)
- Drug (Target Variable)

## Exploratory Data Analysis (EDA)
Performed:
- Dataset Information Analysis
- Missing Value Check
- Statistical Summary
- Duplicate Record Detection
- Drug Distribution Visualization
- Correlation Heatmap
- Outlier Detection using Boxplots

## Data Preprocessing
- Label Encoding for categorical variables
- Feature Selection
- Train-Test Split (80:20)

## Machine Learning Model
### Decision Tree Classifier

Workflow:
1. Data Loading
2. Data Cleaning
3. Data Preprocessing
4. Label Encoding
5. Train-Test Split
6. Model Training
7. Prediction
8. Evaluation

## Model Evaluation

Metric Used:
- Accuracy Score

Result:
- Accuracy: **100%**

The model successfully classified all testing samples correctly.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Google Colab

## Project Structure

Drug-Prediction/
│
├── Drug.ipynb
├── drug200.csv
├── README.md
└── requirements.txt

## Key Visualizations
- Drug Distribution Count Plot
- Correlation Heatmap
- Boxplots for Outlier Detection
- Confusion Matrix
  
## Results
The Decision Tree model achieved excellent performance on the Drug200 dataset with 100% accuracy on the test data.

## Author
**Badal Raj**

Aspiring Data Analyst & Machine Learning Enthusiast

### Skills
- Python
- SQL
- Power BI
- Machine Learning
- Data Analytics

## Repository Description
Machine Learning project that predicts suitable drugs for patients using medical attributes such as Age, Blood Pressure, Cholesterol, and Na_to_K ratio. Built with Python, Scikit-Learn, and Decision Tree Classification.

## GitHub Topics
machine-learning, drug-prediction, classification, decision-tree, python, scikit-learn, data-science, healthcare-analytics, eda, jupyter-notebook
