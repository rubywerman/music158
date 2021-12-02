import json

# OSC part
from pythonosc import udp_client

# windows encoding stuff
import sys
import codecs
import time

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

# Open Sound Control Client, used to send messages to max
client = udp_client.SimpleUDPClient("127.0.0.1", 7777)

def send_message(message):
    while True:
        client.send_message("/message", message)
        time.sleep(5)

if __name__ == "__main__":
    send_message("hello")


