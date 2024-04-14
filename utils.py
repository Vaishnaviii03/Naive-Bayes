import pickle
import sklearn
cv = pickle.load(open("model/vectorizer.pkl", 'rb'))
clf = pickle.load(open("model/bnb.pkl", 'rb'))

def model_predict(review):
    if review == "":
        return ""
    tokenized_review = cv.transform([review]) # X 
    prediction = clf.predict(tokenized_review)
    # If the email is spam prediction should be 1
    prediction = 1 if prediction == 1 else -1
    return prediction