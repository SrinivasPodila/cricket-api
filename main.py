from fastapi import FastAPI
from scraper import get_live_scores

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Cricbuzz Live Score API"}

@app.get("/live-scores")
def live_scores():
    scores = get_live_scores()
    return {"matches": scores}
