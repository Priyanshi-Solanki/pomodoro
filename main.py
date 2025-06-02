from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

app = FastAPI()

# Enable CORS so the frontend can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_timer_response(minutes: int):
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(minutes=minutes)
    return {
        "session": f"{minutes}-minute session",
        "start_utc": start_time.isoformat() + "Z",
        "end_utc": end_time.isoformat() + "Z"
    }

@app.get("/")
def root():
    return {"message": "Pomodoro API is alive and focused 🔥🍅"}

@app.get("/start")
def start_work():
    return get_timer_response(25)

@app.get("/break")
def start_break():
    return get_timer_response(5)

@app.get("/longbreak")
def start_long_break():
    return get_timer_response(15)
