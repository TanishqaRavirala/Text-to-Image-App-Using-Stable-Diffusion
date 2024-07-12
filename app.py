# Libraries for building GUI
import tkinter as tk
import customtkinter as ctk

# Machine Learning libraries
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Libraries for processing image
from PIL import Image

# private modules
from authtoken import auth_token

# Create app user interface
root = tk.Tk()
root.geometry("532x632")
root.title("Text to Image Generator")
root.configure(bg='black')
ctk.set_appearance_mode("dark")

# Create input box on the user interface
text_entry = ctk.CTkEntry(root, height=40, width=512, text_color="white", fg_color="black")
text_entry.configure(font=("Arial", 15))  # Set the font using 'configure'
text_entry.place(x=10, y=10)

# Create a placeholder to show the generated image
image_display = ctk.CTkLabel(root, height=512, width=512, text="")
image_display.place(x=10, y=110)

# Download stable diffusion model from hugging face
model_id = "CompVis/stable-diffusion-v1-4"
device = "cpu"  # Set device to CPU if CUDA is not available
try:
    sd_model = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=auth_token)
    sd_model.to(device)
except RuntimeError as err:
    print(f"Error loading model: {err}")
    sd_model = None

# Generate image from text
def create_image():
    """ Generate image from text using stable diffusion """
    if sd_model:
        try:
            with autocast(device):
                output = sd_model(text_entry.get(), guidance_scale=8.5)
                print(f"Result keys: {output.keys()}")

                # Check for expected keys in the result
                if "images" in output:
                    generated_img = output["images"][0]
                else:
                    print(f"Unexpected result format: {output}")
                    return

            # Save the generated image
            generated_img.save('output_image.png')

            # Display the generated image on the user interface using CTkImage
            ctk_img = ctk.CTkImage(light_image=Image.open("output_image.png"), size=(512, 512))
            image_display.configure(image=ctk_img)
            image_display.image = ctk_img  # Keep a reference to avoid garbage collection

        except Exception as e:
            print(f"Error generating image: {e}")
    else:
        print("Model not loaded properly. Check previous error messages for details.")

generate_btn = ctk.CTkButton(root, height=40, width=120, text_color="black", fg_color="white", command=create_image)
generate_btn.configure(font=("Arial", 15))  # Set the font using 'configure'
generate_btn.configure(text="Generate")
generate_btn.place(x=206, y=60)

root.mainloop()
