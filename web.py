from flask import Flask, request, render_template, send_file
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from PIL import Image
from io import BytesIO
import base64
from authtoken import auth_token

# Initialize the Flask app
app = Flask(__name__)

# Load your model
model_id = "CompVis/stable-diffusion-v1-4"
device = "cpu"  # Set device to CPU if CUDA is not available
try:
    sd_model = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=auth_token)
    sd_model.to(device)
except RuntimeError as err:
    print(f"Error loading model: {err}")
    sd_model = None

# Function to generate image from text
def generate_image(prompt):
    if sd_model:
        try:
            with autocast(device):
                output = sd_model(prompt, guidance_scale=8.5)
                print(f"Result keys: {output.keys()}")

                if "images" in output:
                    generated_img = output["images"][0]
                else:
                    print(f"Unexpected result format: {output}")
                    return None

            return generated_img
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
    else:
        print("Model not loaded properly. Check previous error messages for details.")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            generated_img = generate_image(prompt)
            if generated_img:
                buffered = BytesIO()
                generated_img.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                return render_template('index.html', img_data=img_str)
    return render_template('index.html', img_data=None)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
