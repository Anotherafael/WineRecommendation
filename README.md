## Wine Recommendation

This project was developed as part of the [Intelligent Recommendation System Course](https://drive.google.com/file/d/17K87LtU9j7mQbs0Mdq08r84zq6Y0kNEk/view?usp=sharing) at Univesidade Federal do Tocantins. It aims to create a personalized wine recommendation system using the [XWines](https://www.kaggle.com/datasets/rogerioxavier/x-wines-slim-version) dataset. The system employs collaborative filtering and content-based recommendation techniques to suggest wines based on user preferences.

The project draws inspiration from the work of [salimkilinc](https://github.com/salimkilinc), whose code on GitHub served as a reference for implementing the recommendation models.

## Summary

- [Which recommendations were used?](#which-recommendations-were-used)
- [Technologies](#technologies)
- [How to Install](#how-to-install)

## Which recommendations were used?

**Collaborative Filtering:** This model utilizes user-item interactions to recommend wines based on similar users' preferences. By identifying patterns in user behavior, personalized recommendations can be generated for each user.

**Content-based:** In contrast to collaborative filtering, this model focuses on wine attributes such as grape variety, region, and vintage. By understanding each wine's characteristics, we can recommend similar wines based on content similarity.

## Technologies

* **Python:** A versatile programming language widely used in data science, web development, and automation.
* **Numpy and Pandas:** Used for data preprocessing, feature engineering, and data manipulation.
* **Jupyter Notebook and VSCode:** Commonly used development environments for Python coding, with Jupyter Notebook focusing on interactive data analysis and VSCode being a general-purpose code editor.
* **Scikit-learn:** A machine learning library offering a variety of algorithms and tools for data analysis.
    * **TfidfVectorizer:** sklearn class that transforms text into numerical representations using the TF-IDF technique.
    * **linear_kernel:** function that calculates linear similarity between two datasets.
    * **cosine_similarity:** function to calculate vector similarity using the cosine measure.
    * **euclidean_distances:** function to calculate Euclidean distance between points in an n-dimensional space.

## How to Install

1. Clone the repository
```
git clone https://github.com/Anotherafael/STUDY_WineRecommendation.git
```
2. Install [Python](https://www.python.org/) or copy the project to [Google Collab](https://colab.google/)
3. Install the dependencies
```
pip install -r requirements.txt
```
or
```
%pip install -r requirements.txt
```
4. Have fun! 😊
