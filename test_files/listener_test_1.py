from pynput.keyboard import Listener, Key

def on_press(key):
    print('{0} pressed'.format(key))

def on_release(key):
    if key == Key.esc:
        return False

def main():
    with Listener(on_press=on_press, on_release=on_release, supress=True) as listener:
        listener.join()
        print("after join")
    print("end of main")


if __name__ == "__main__":
    main()
