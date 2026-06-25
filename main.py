from screenshot import take_screenshot


def main():
    print("🚀 Scout is starting...")

    image = take_screenshot()

    print(f"Image saved as: {image}")


if __name__ == "__main__":
    main()