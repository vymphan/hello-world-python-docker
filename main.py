import time

def say_hello():
    print("Hello World")

def loop_greeting():
    try:
        while True:
            say_hello()
            time.sleep(1)
    except KeyboardInterrupt:
        print("User stopped the program")

if __name__ == "__main__":
    loop_greeting()
    
