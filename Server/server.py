import socket

import threading

import sys



print("""




  ____  _  _   _____  _   _  _   _____ 
 |  _ \| || | |  __ \| | | || | / ____|
 | |_) | || |_| |__) | | | || || (___  
 |  _ <|__   _|  _  /| | |__   _\___ \ 
 | |_) |  | | | | \ \| |____| | ____) |
 |____/   |_| |_|  \_\______|_||_____/ 
                                       
                                       

                                            

""")



SERVER_ADDRESS = "your_IP"

SERVER_PORT = 4444



def logger(prefix: str, message: str) -> None:

    print(f"{prefix}: {message}", end="", flush=True)



def handle_client(conn, addr) -> None:

    logger("INFO", f"Connection from {addr}")

    while True:

        try:

            data = conn.recv(1024)

        except OSError:

            break

        else:

            if not data:

                break

            else:

                received_data = data.decode()

                print(received_data, end="", flush=True)  # Tüm veriyi yan yana yazdırma

    logger("INFO", f"Disconnection from {addr}")

    conn.close()



def main(host: str, port: int) -> None:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.bind((host, port))

        sock.listen()

        logger("INFO", f"Listening on {sock.getsockname()}")

        while True:

            conn, addr = sock.accept()

            threading.Thread(target=handle_client, args=(conn, addr)).start()



if __name__ == "__main__":

    try:

        main(SERVER_ADDRESS, SERVER_PORT)

    except AttributeError as error:

        logger("ERROR", error)

