# Vertex AI FastAPI Classifier

This project is a FastAPI-based web service that uses Google Vertex AI for text classification. It provides endpoints to classify questions, store responses, and collect user feedback. The backend uses SQLAlchemy for database operations.

## Features

- **/api/classify**: Classifies a question using a Vertex AI model.
- **/api/feedback**: Allows users to submit feedback on the classification.
- **/api/feedback/{response_id}**: Retrieves feedback for a specific response.
- Stores all questions, responses, and feedback in a SQL database.

## Project Structure
```text
vertex-ai-fastAPI/
├── classify.py                 # Vertex AI classification logic
├── main.py                     # FastAPI app and API endpoints
├── db.py                       # Database models and session setup
├── test.py                     # API endpoint tests
├── requirements.txt            # Python dependencies
├── service-account-key.json    # (GCP credentials — should be in .gitignore)
```


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
  - Place your  `service-account-key.json` in the project root.
  - Important: Do NOT commit this file to GitHub.

5. **Set up your database**
  - Update DATABASE_URL in `db.py` with your actual database credentials.

6. **Run the FastAPI server**
   ```sh
   uvicorn main:app --reload
   
7. **Test the API**
   -Use the included `test.py` or tools like Postman or curl

   
      ```sh
      # Test
      /api/classify endpoint curl -X POST http://127.0.0.1:8000/api/classify \ -H "Content-Type: application/json" \ -d '{"question": "Wifi issues at mc nair?"}'
      # Test
      /api/feedback endpoint curl -X POST http://127.0.0.1:8000/api/feedback \ -H "Content-Type: application/json" \ -d '{"response_id": 1, "feedback": "Accurate classification"}' 
      # Test
      /api/feedback/{response_id} endpoint curl http://127.0.0.1:8000/api/feedback/1
      ```
   

       
