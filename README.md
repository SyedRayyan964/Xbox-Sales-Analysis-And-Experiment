# Xbox 2026 Sales Analysis & Prediction

## Project Overview
This project analyzes Xbox sales data for 2026 using Python, Pandas, Matplotlib, and Scikit-learn. It explores monthly revenue, losses, units sold, unsold units, and traffic trends through data visualization. It also uses a **Linear Regression model** to predict sales-related outcomes based on the number of promotions, game releases, and month.

## Features
- **Data Analysis:** Explore monthly sales, revenue, losses, and unsold units.
- **Data Visualization:** Create line charts, bar charts, scatter plots, and pie charts using Matplotlib.
- **Machine Learning:** Train a Multi-Output Linear Regression model to predict multiple sales-related values.
- **Train-Test Split:** Evaluate the model on a held-out test set.
- **Experimental Predictions:** Test different promotion and game-release scenarios to explore possible changes in sales.
- **Data Comparison:** Visualize historical values alongside model-generated predictions.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn
- Linear Regression
- Label Encoding
- Train-Test Split

## How It Works
1. Load the sales dataset using Pandas.
2. Visualize historical monthly sales and revenue trends.
3. Encode the month column into numerical values.
4. Use promotions, game releases, and month as input features.
5. Train a Linear Regression model to predict loss, revenue, total units sold, and unsold units.
6. Compare model predictions with actual test values.
7. Experiment with different input scenarios and visualize the predicted outcomes.

## Project Goal
The goal is to practice data analysis, visualization, and introductory machine learning while exploring how promotions and game releases may relate to sales performance.

## Important Note
This is an educational project using a sample sales dataset. Predictions are estimates, not guaranteed business outcomes. The model does not establish that promotions or game releases cause changes in sales. More historical data and proper validation would be needed for reliable business forecasting.
