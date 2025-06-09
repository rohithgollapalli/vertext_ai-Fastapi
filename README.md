# Vertex AI FastAPI Classifier

This project is a FastAPI-based web service that uses Google Vertex AI for text classification. It provides endpoints to classify questions, store responses, and collect user feedback. The backend uses SQLAlchemy for database operations.

## Features

- **/api/classify**: Classifies a question using a Vertex AI model.
- **/api/feedback**: Allows users to submit feedback on the classification.
- **/api/feedback/{response_id}**: Retrieves feedback for a specific response.
- Stores all questions, responses, and feedback in a SQL database.

## Project Structure
vertex-ai-fastAPI/
├── classify.py # Vertex AI classification logic 
├── main.py  # FastAPI app and API endpoints
├── db.py # Database models and session setup 
├── test.py # API endpoint tests 
├── requirement.txt # Python dependencies
├── service-account-key.json # (GCP credentials, should be in .gitignore)


## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/<your-username>/<repo-name>.git
   cd vertex-ai-fastAPI
   

2. **Create and activate a virtual environment**
   ```sh
    python -m venv venv
    venv\Scripts\activate   # On Windows
    # source venv/bin/activate   # On Linux/Mac
3. **Install dependencies**
   ```sh
   pip install -r requirement.txt

4. **Configure Google Cloud credentials**
  - Place your ```sh service-account-key.json in the project root.
Important: Do NOT commit this file to GitHub. Add it to your .gitignore.
