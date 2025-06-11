from main import app
from fastapi.testclient import TestClient

# Create a test client for the FastAPI app
client = TestClient(app)

def test_classify():
    """
    Test the /api/classify endpoint to ensure it returns a valid response and response_id.
    """
    payload = {
        "question": "wifi in eric building is not working"
    }
    response = client.post("/api/classify", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "response_id" in data

def test_feedback():
    """
    Test the /api/feedback endpoint by first classifying a question,
    then submitting feedback for the response.
    """
    # Classify a sample question
    classify_response = client.post("/api/classify", json={"question": "wifi in eric building is not working"})
    assert classify_response.status_code == 200

    # Extract response_id from classification
    response_id = classify_response.json()["response_id"]

    # Prepare feedback payload
    feedback = {
        "response_id": response_id,
        "correct": True,
        "feedback_text": "This was accurate"
    }
    # Submit feedback
    response = client.post("/api/feedback", json=feedback)
    assert response.status_code == 200
    assert response.json()["message"] == "Feedback saved successfully."

def test_get_feedback():
    """
    Test the /api/feedback/{response_id} endpoint by classifying a question,
    submitting feedback, and then retrieving the feedback.
    """
    # Classify a sample question
    classify_response = client.post("/api/classify", json={"question": "wifi in eric building is not working"})
    assert classify_response.status_code == 200

    # Extract response_id from classification
    response_id = classify_response.json()["response_id"]

    # Prepare and submit feedback
    feedback = {
        "response_id": response_id,
        "correct": True,
        "feedback_text": "This was accurate"
    }
    response = client.post("/api/feedback", json=feedback)
    assert response.status_code == 200

    # Retrieve feedback for the response_id
    get_response = client.get(f"/api/feedback/{response_id}")
    assert get_response.status_code == 200

    feedback_list = get_response.json()
    assert len(feedback_list) >= 1

# Note:
# - No confidential details are present in this test file.
# - All test data is generic and safe for public code.