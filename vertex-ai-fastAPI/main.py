import os
from langchain_google_vertexai import VertexAI
from google.cloud import aiplatform
from google import genai
from google.genai import types
import base64

# Set Google Cloud credentials (masked for security)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account-key.json"

# Initialize Vertex AI platform (project and location masked)
aiplatform.init(project="your-project-id", location="your-region")

# Initialize VertexAI model (model name masked)
tuned_model = VertexAI(
    model_name="projects/********/locations/your-region/models/********@1",
    temperature=0.7,
    max_output_tokens=100,
)

def generate(question):
    """
    Generates a classification for the given question using a Vertex AI endpoint.

    Args:
        question (str): The input text to classify.

    Returns:
        str: The classification result.
    """
    # Initialize the generative AI client (project and location masked)
    client = genai.Client(
        vertexai=True,
        project="your-project-number",
        location="your-region",
    )

    # System instruction for the model to classify into specific categories
    si_text1 = (
        "You are a Classifier responsible to classify into CTS, CTS Campus, "
        "Classroom Support, Print Team (External)."
    )

    # Vertex AI endpoint for the model (masked)
    model = "projects/********/locations/your-region/endpoints/********"
    
    # Prepare the user input as content for the model
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=question)  # Pass the actual question text
            ]
        ),
    ]

    # Configuration for content generation, including safety settings and system instructions
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        max_output_tokens=8192,
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="OFF"
            )
        ],
        system_instruction=[types.Part.from_text(text=si_text1)],
    )

    # Generate content using the model and return the first chunk of text
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        return chunk.text