import joblib
from utils.preprocess import clean_text

def load_model_and_vectorizer():
    model = joblib.load("models/tmodel.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    return model, vectorizer

def predict_emotion(model, vectorizer, text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return prediction
