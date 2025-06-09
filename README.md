# Vertex AI FastAPI Classifier

This project is a FastAPI-based web service that uses Google Vertex AI for text classification. It provides endpoints to classify questions, store responses, and collect user feedback. The backend uses SQLAlchemy for database operations.

## Features

- **/api/classify**: Classifies a question using a Vertex AI model.
- **/api/feedback**: Allows users to submit feedback on the classification.
- **/api/feedback/{response_id}**: Retrieves feedback for a specific response.
- Stores all questions, responses, and feedback in a SQL database.

## Project Structure
vertex-ai-fastAPI/
├── classify.py
# Vertex AI classification logic 
├── main.py 
# FastAPI app and API endpoints
├── db.py 
# Database models and session setup 
├── test.py
# API endpoint tests 
├── requirement.txt 
# Python dependencies
├── service-account-key.json
# (GCP credentials, should be in .gitignore)


