"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
# Added activities: 2 sports, 2 artistic, 2 intellectual
# Sports
# - Soccer Team
# - Basketball Team
# Artistic
# - Drama Club
# - Art Workshop
# Intellectual
# - Math Olympiad
# - Science Club
# New activity: Photography Club
# Artistic
activities = {
    "Soccer Team": {
        "description": "Join the school soccer team and compete in local tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["alex@mergington.edu", "lucas@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and play basketball games with the school team",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["mia@mergington.edu", "liam@mergington.edu"]
    },
    "Drama Club": {
        "description": "Participate in school plays and improve your acting skills",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["ava@mergington.edu", "noah@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Explore painting, drawing, and sculpture in a creative environment",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu", "ethan@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and challenge your problem-solving skills",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["oliver@mergington.edu", "charlotte@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["amelia@mergington.edu", "benjamin@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and participate in photo walks",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 10,
        "participants": ["grace@mergington.edu", "jack@mergington.edu"]
    },



@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
