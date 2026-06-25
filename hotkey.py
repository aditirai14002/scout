from pynput import keyboard

pressed = set()


def on_press(key):
    pressed.add(key)

    try:
        if (
            keyboard.Key.cmd in pressed
            and keyboard.Key.shift in pressed
            and key.char.lower() == "s"
        ):
            print("\n🔥 Scout activated!\n")
    except AttributeError:
        pass


def on_release(key):
    pressed.discard(key)


def start_hotkey_listener():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
    )
    listener.start()
    return listener