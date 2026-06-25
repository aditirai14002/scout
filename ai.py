import ollama


def ask_ai(image_path):
    """
    Sends an image to Gemma through Ollama and returns the response.
    """

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": (
                    "Look at this screenshot carefully. "
                    "Explain what is visible on the screen in simple language."
                ),
                "images": [image_path],
            }
        ],
    )

    return response["message"]["content"]