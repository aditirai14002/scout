from hotkey import start_hotkey_listener


def main():

    print("=" * 40)
    print("🛰️  Scout is running...")
    print("Press Command + Shift + S")
    print("Press Ctrl + C to quit")
    print("=" * 40)

    listener = start_hotkey_listener()

    listener.join()


if __name__ == "__main__":
    main()