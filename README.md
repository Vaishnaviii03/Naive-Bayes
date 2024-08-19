# 🍴 Restaurant Review Sentiment Analysis - Naive Bayes Classifier

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg) ![Flask](https://img.shields.io/badge/Flask-2.0.1-lightgrey.svg) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24.2-orange.svg) ![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## 📌 Overview

This project utilizes a Naive Bayes classifier to analyze restaurant reviews and classify them as either positive or negative. The project includes a web application built with Flask, where users can input a restaurant review and receive an immediate sentiment analysis.

## 🚀 Features

- **Sentiment Analysis**: Classifies reviews as positive or negative using a Naive Bayes model.
- **Web Interface**: User-friendly Flask-based web app to input reviews and view results.
- **Pre-trained Model**: The model is pre-trained on a dataset of restaurant reviews for quick and accurate predictions.

## 🛠️ Tools & Libraries

- **Python 3.8+**: Core programming language
- **Flask 2.0.1**: Web framework for building the user interface
- **Scikit-Learn 0.24.2**: Machine learning library for building the Naive Bayes model
- **Pandas 1.2.4**: Data manipulation and analysis
- **BeautifulSoup 4.9.3**: (If applicable for additional scraping tasks)

## 📁 Project Structure

```bash
├── .ipynb_checkpoints/    # Jupyter notebook checkpoints
├── __pycache__/           # Python bytecode cache
├── model/                 # Directory to store machine learning models
│   ├── bnb.pkl            # Trained Naive Bayes model
│   └── vectorizer.pkl     # Fitted CountVectorizer
├── templates/             # HTML templates for Flask
│   └── index.html         # Main page of the web app
├── Naive Bayes.ipynb      # Jupyter notebook for model development
├── Restaurant_Reviews.tsv # Dataset containing restaurant reviews
├── app.py                 # Flask application script
├── requirements.txt       # Python packages required
└── utils.py               # Utility functions for the project
```
## 🔍 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-review-sentiment.git
cd restaurant-review-sentiment
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Web Application

```bash
python app.py
```

### 4. Explore the Jupyter Notebook

The Jupyter notebook `Naive Bayes.ipynb` contains the complete process of data loading, preprocessing, model training, and evaluation. You can explore and modify it as needed.

## 📊 Dataset

The dataset used in this project is `Restaurant_Reviews.tsv`, which contains a collection of restaurant reviews labeled as positive or negative. The model is trained on this data to predict the sentiment of new reviews.

## 🌟 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Acknowledgements

- **Scikit-Learn**: For providing robust machine learning algorithms and tools.
- **Flask**: For enabling rapid development of web applications.
