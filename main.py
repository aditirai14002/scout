import pyautogui
import base64
import tkinter as tk
from google import genai
from google.genai import types
from PIL import Image

API_KEY = None

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")
    return "screen.png"

def ask_gemini(image_path):
    client = genai.Client(api_key=API_KEY)
    
    image = Image.open(image_path)
    
    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=[
            image,
            "You are a coding mentor for a first year CS student. Look at their screen carefully. Tell them: 1) What you can see they are trying to do 2) What the specific problem or next step is 3) One simple action they should take right now. Be brief, specific and encouraging."
        ]
    )
    
    return response.text

def show_popup(message):
    root = tk.Tk()
    root.title("Screenshot Mentor")
    root.geometry("500x300")
    root.configure(bg="#1e1e1e")
    
    label = tk.Label(
        root,
        text=message,
        wraplength=460,
        justify="left",
        padx=15,
        pady=15,
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 13)
    )
    label.pack(expand=True)
    
    button = tk.Button(
        root,
        text="Got it",
        command=root.destroy,
        bg="#007acc",
        fg="white",
        font=("Arial", 12),
        padx=20,
        pady=8,
        border=0
    )
    button.pack(pady=10)
    root.mainloop()

def mentor():
    print("Taking screenshot...")
    image_path = take_screenshot()
    print("Asking Gemini...")
    response = ask_gemini(image_path)
    print("Response received!")
    show_popup(response)

mentor()