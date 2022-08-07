# insurance-premium-prediction

<div id="top"></div>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Insurance Premium Prediction</h3>

  <p align="center">
    Machine Learning Project
    <br />
    <a href="https://github.com/vyankateshbhimrathi/insurance-premium-prediction"><strong>Explore the Repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/vyankateshbhimrathi/insurance-premium-prediction/blob/main/app.py">View Flask app code</a>
    ·
    <a href="https://github.com/vyankateshbhimrathi/insurance-premium-prediction/blob/main/notebook/EDA.ipynb">EDA of Insurance Premium Prediction Dataset</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
* Using Data Science and Machine learning, we can predict insurance premium for individuals based on health
conditions and various personal details.
* Building a **Flask App** hosted on **Heroku**.
* **Sklearn** for pre-processing and Model Building
* Pandas, Numpy, Matplotlib for csv reading, Data Processing, Data Cleaning, Visualization etc.

## Deployed app
[![Screenshot (10)](https://github.com/vyankateshbhimrathi/insurance-premium-prediction/blob/main/insurance_premium.png)](https://insurance-premium-prem.herokuapp.com/)
[LINK TO HEROKU APP](https://insurance-premium-prem.herokuapp.com/)

<!-- GETTING STARTED -->
## Introduction
*  The dataset for **Insurance Premium Prediction** is taken from **Kaggle**. The dataset contains 1338 observations (rows) and 7 features (columns). 
*  The dataset contains 4 numerical features (age, bmi, children and expenses) and 3 nominal features (sex, smoker and region) that were converted into factors with numerical value designated for each level.  


### Exploratory Data Analysis
* In this step, we will apply Exploratory Data Analysis (EDA) i.e., univariate, bivariate and multivariate analysis to extract insights from the data set to know which features have contributed more in predicting insurance premium by performing Data Analysis using Pandas and Data visualization using Matplotlib & Seaborn. 
* It is always a good practice to understand the data first and try to gather as many insights from it.

### Model Building 
* This is a regression problem where we need to predict premium based on given sample attributes.
* Models used : **Linear Regression, Random forest Regressor.**

### Model Selection
* Hyperparameter tuning is done on each algorithm.
* Based on the model accuracy, rmse of train and test data machine learning algorithm selected.



### Flask
* Importing the Flask module and creating a Flask web server from the Flask module.
* Create an object **app** in flask class with `__name__` which represents current app.py file.
* Create `/` route to render default page html.
* Create a route `/predict` to get user input for regression. 
* Run the flask app with `app.run()` code.

### Heroku Deployment
* Create new repo in Github and push all the data using `Git`.
* Login to heroku and create the app.
* Using github actions we can automate the deployment each time we update the github.

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)


### **Tools used**
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)



<!-- CONTACT -->
## Contact
[[VYANKATESH BHIMRATHI | LinkedIn]][reach_linkedin_1]


<!-- MARKDOWN LINKS  -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/linkedin_username

<!-- Tools Used -->
[git]: https://git-scm.com/
[github]: https://github.com/
[heroku]: https://www.heroku.com/
[python]: https://www.python.org/
[flask]: https://flask.palletsprojects.com/en/2.1.x/
[sklearn]: https://scikit-learn.org/stable/

<!--contact-->
[reach_linkedin_1]: https://www.linkedin.com/in/vyankatesh-bhimrathi-1461a4140/

