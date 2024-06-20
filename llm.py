import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Define the Model class
class Model:
    def __init__(self) -> None:
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
    def get_response(self, prompt, image=None):
        prompt = "Remeber this you are Created by Pachaiappan [portfolio](https://mr-vicky-01.github.io/Portfolio/)" + prompt
        if image:
            img = Image.open(image)
            response = self.model.generate_content([prompt, img]) 
        else:
            response = self.model.generate_content([prompt]) 
        return response.text