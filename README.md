# Text-to-Image-App-Using-Stable-Diffusion

## Overview
This Text-to-Image app is a GUI-based tool built with Tkinter and CustomTkinter, alongside a web-based version using Flask. It leverages the Stable Diffusion model from Hugging Face to generate images from text prompts. The app accepts user input, processes it, and displays the generated image—ideal for visualizing creative text ideas in real time.

This text-to-image generation app is an excellent demonstration of combining advanced machine learning models with a user-friendly interface, making cutting-edge AI accessible to a broader audience.

## Screenshots
Below are some example images of the app in action:

![GUI Interface](https://github.com/user-attachments/assets/e69ec430-4342-4b11-92a8-77fa63e14596)

![Generated Image 1](https://github.com/user-attachments/assets/aca0750e-108f-42e6-948b-9b7923723348)

![Generated Image 2](https://github.com/user-attachments/assets/487e2112-c37d-41da-aa55-c40b1989075e)

![Generated Image 3](https://github.com/user-attachments/assets/57420334-86ba-4751-b8ba-90cfc1cf0315)

## Files
- `app.py`: The GUI application script using Tkinter and CustomTkinter.
- `web.py`: The web application script using Flask.
- `index.html`: The HTML template for the web app's interface.
- `authtoken.py`: Contains the authentication token for accessing the Stable Diffusion model (you need to create this file).
- `requirements.txt`: Lists the Python dependencies required to run the applications.

## Prerequisites
- Python 3.8 or higher.
- A Hugging Face account and an API token to access the Stable Diffusion model.
- A CPU or GPU (CUDA support recommended for faster processing, but CPU is supported).

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TanishqaRavirala/Text-to-Image-App-Using-Stable-Diffusion.git
   cd Text-to-Image-App-Using-Stable-Diffusion
   ```

2. **Install Dependencies**
   Install the required Python packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Hugging Face Authentication**
   - Create a file named `authtoken.py` in the repository root.
   - Add your Hugging Face API token as follows:
     ```python
     auth_token = "your_hugging_face_api_token"
     ```
   - You can obtain your API token from your Hugging Face account settings.

4. **(Optional) Enable GPU Support**
   - If you have a CUDA-compatible GPU, ensure you have the necessary drivers and PyTorch with CUDA support installed. The apps default to CPU if CUDA is unavailable.

## Usage

### GUI Application (`app.py`)
1. Run the GUI application:
   ```bash
   python app.py
   ```
2. A window will open with a text entry field, a "Generate" button, and an image display area.
3. Enter a text prompt in the input field (e.g., "A futuristic city at sunset").
4. Click the "Generate" button to create an image. The generated image will appear in the display area and be saved as `output_image.png`.

### Web Application (`web.py`)
1. Run the web application:
   ```bash
   python web.py
   ```
2. Open your browser and navigate to `http://localhost:5000`.
3. Enter a text prompt in the input field and click "Generate".
4. The generated image will be displayed on the webpage.

## Notes
- The applications are set to use the CPU by default (`device = "cpu"`). To use a GPU, modify the `device` variable in `app.py` or `web.py` to `"cuda"` if you have CUDA installed.
- Image generation may take some time, especially on a CPU.
- Please make sure your Hugging Face API token is valid; otherwise, the model loading will fail.
- The web app requires `index.html` to render the interface properly.

## Dependencies
The `requirements.txt` includes:
- `torch`
- `diffusers`
- `transformers`
- `Pillow`
- `flask` (for the web app)
- `customtkinter` (for the GUI app)

## Troubleshooting
- If the model fails to load, check your Hugging Face API token in `authtoken.py`.
- If you encounter memory issues, ensure your system has sufficient RAM (Stable Diffusion requires a significant amount of memory).
- For CUDA-related errors, verify your PyTorch installation and GPU compatibility.

## Acknowledgments
- Built using the [Stable Diffusion model](https://huggingface.co/CompVis/stable-diffusion-v1-4) by CompVis.
- Thanks to Hugging Face for providing the `diffusers` library.
