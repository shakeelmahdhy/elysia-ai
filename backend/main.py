from fastapi import FastAPI
from schemas import EmotionRequest, EmotionResponse
from utils.predict import load_model_and_vectorizer, predict_emotion

app = FastAPI(title="Elysia AI - Emotion Detection")

model, vectorizer = load_model_and_vectorizer()

@app.post("/predict", response_model=EmotionResponse)
async def get_emotion(data: EmotionRequest):
    result = predict_emotion(model, vectorizer, data.text)
    return EmotionResponse(emotions=result)
