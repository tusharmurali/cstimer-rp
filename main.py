import json
import pypresence
import time
from pypresence import Presence
from win32gui import GetWindowText, GetForegroundWindow

client_id = '723966115537223721'  # Bot ID
RPC = Presence(client_id)  # Initialize the client class
try:
    RPC.connect()  # Start the handshake loop
except pypresence.exceptions.InvalidPipe:
    print("Please ensure that Discord is running before launching the rich presence")
print("csTimer Rich Presence connected")

with open('tooltips.json') as f:
    tooltips = json.load(f)  # import tooltips from file


def get(index):
    return data[index] if index < len(data) - 3 else "n/a"


while True:  # The presence will stay on as long as the program is running
    data = GetWindowText(GetForegroundWindow()).split()
    if get(0) == "csTimer":
        RPC.update(state="ao5: " + get(10) + ", ao12: " + get(11), details="time: " + get(8) + ", mo3: " + get(9),
                   large_image=get(7).replace(" ", ""), large_text=tooltips[get(7)],
                   small_image="cstimer", small_text="csTimer")
    time.sleep(5)  # Update every 5 seconds
