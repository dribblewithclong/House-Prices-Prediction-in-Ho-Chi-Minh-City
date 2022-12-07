# HO CHI MINH CITY HOUSE PRICE PREDICTION PROJECT

## Introduction
- In this project, I will build a web app for predicting the house price in Ho Chi Minh City based on the datasets scraped at website [Propzy](propzy.vn).
- App: https://hcmhouseprice.herokuapp.com/
### Preview
![web_layout](https://github.com/123olala/HCM-House/blob/main/assets/web_app.png)

## Workflow
### 0. Structures
```
├───assets  (containing file for web layout design)
│       style.css
├───data chunk (containing separated data for each district)
│
├───data  (containing data for processing)
│
├── app.py        
├── crawl_data.ipynb
├── eda_cleaning.ipynb
├── feature_engineering_selection.ipynb
├── model.ipynb
├── final_model.sav
├── Procfile           
└── requirements.txt
```
### 1. Data Scraping
- For scraping, I using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to collect data from website [Propzy](propzy.vn).
### 2. Data Cleaning
- Drop duplicated values
- Extracted and create new information from text desription of each house.
- Correct wrong price and numeric value of observations
- Correct missing values
### 3. Data Exploratory Analysis
- Examine missing values
- Analyze numerical variables and their distribution
- Analyze categorical variables and their cardinality 
- Detect outliers
- Analyze relationship between all the features of house and the house price
### 4. Feature Engineering
- Remove outliers
- Complete missing values
- Transform numerical variables due to its skew distribution
- Encode categorical variables for model building
- Create new feature from heading title
- Oversampling data
- Cluster and PCA
### 5. Feature Selection
- Drop redundant features
- Remove highly correlated features
- Examine features importance
- Remove anomaly observations
### 6. Model Bulding and Tuning
- Perform K-fold cross validation
- Use Random Forest, XGB and LightGBM algorithm for training datasets
- Perform RandomizedSearchCV for optimizing score
### 7. Web App Deployment
- For app deployment, I using [Dash](https://dash.plotly.com/) to design and represent. I also using [Heroku](https://heroku.com/) for hosting web app. 
## Conclusion
- This project aims to help people to somewhat determine a price for their real estate to sell as well as to be able to determine if the houses they intend to buy are being sold for a reasonable price. However, above all, the main purpose of this project is to have a fun time when playing with machine learning.
