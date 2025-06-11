from fastapi import FastAPI
from pydantic import BaseModel
import classify
from typing import Optional, List
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Import your SQLAlchemy session and base from your db module (ensure confidential details are masked in db.py)
from db import SessionLocal, engine, Base

app = FastAPI()

# Database model for storing question and response logs
class Responselog(Base):
    __tablename__ = "response_log"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    response = Column(Text)
    feedbacks = relationship("Feedback", back_populates="response")

# Database model for storing feedback on responses
class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    response_id = Column(Integer, ForeignKey("response_log.id"))
    feedback_text = Column(Text)
    correct = Column(Boolean)
    response = relationship("Responselog", back_populates="feedbacks")

# Create tables in the database (if not already present)
Base.metadata.create_all(bind=engine)

# Request model for classify endpoint
class ClassifyRequest(BaseModel):
    question: str

# Response model for classify endpoint
class ClassifyResponse(BaseModel):
    response: str
    response_id: int

# Request model for feedback submission
class FeedbackRequest(BaseModel):
    response_id: int
    correct: bool 
    feedback_text: Optional[str] = None

# Response model for feedback submission
class FeedbackResponse(BaseModel):
    message: str

# Output model for feedback retrieval
class FeedbackOut(BaseModel):
    id: int
    response_id: int
    feedback_text: Optional[str]
    correct: bool

    class Config:
        orm_mode = True

# Save a question and its response to the database, return the response log ID
def save_question_response(question: str, response: str) -> int:
    db = SessionLocal()
    db_entry = Responselog(question=question, response=response)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    db.close()
    return db_entry.id

# Save feedback for a given response
def save_feedback(response_id: int, correct: bool, feedback_text: Optional[str] = None):
    db = SessionLocal()
    entry = Feedback(response_id=response_id, correct=correct, feedback_text=feedback_text)
    db.add(entry)
    db.commit()
    db.close()

# Endpoint to classify a question and log the response
@app.post("/api/classify", response_model=ClassifyResponse)
async def classify_endpoint(request: ClassifyRequest):
    result = classify.generate(request.question)
    response_id = save_question_response(request.question, result)
    return {"response": result, "response_id": response_id}

# Endpoint to submit feedback for a response
@app.post("/api/feedback", response_model=FeedbackResponse)
async def submit_feedback(request: FeedbackRequest):
    save_feedback(request.response_id, request.correct, request.feedback_text)
    return {"message": "Feedback saved successfully."}

# Endpoint to retrieve feedback for a specific response
@app.get("/api/feedback/{response_id}", response_model=List[FeedbackOut])
def get_feedback(response_id: int):
    db = SessionLocal()
    feedbacks = db.query(Feedback).filter(Feedback.response_id == response_id).all()
    db.close()
    return feedbacks

