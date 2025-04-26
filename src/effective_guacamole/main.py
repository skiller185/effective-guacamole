import os
from google import genai

# Retrieve the API key from the environment variable
# The bash script passes this variable into the container
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

# Check if the API key was found
if not api_key:
    print("Error: GOOGLE_GENAI_API_KEY environment variable not set.")
    print("Please ensure the environment variable is passed to the container.")
    exit(1) # Exit the script if the API key is not available

# Initialize the GenAI client with the API key from the environment
client = genai.Client(api_key=api_key)

try:
    # Generate content using the specified model and prompt
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain how AI works in a few words",
    )

    # Print the generated text
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")

