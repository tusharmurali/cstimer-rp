from pypresence import Presence
from win32gui import GetWindowText, GetForegroundWindow
import time

client_id = '723966115537223721'  # Bot ID
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop

print("csTimer Rich Presence connected")

tooltips = {
    "3x3x3": "3x3x3 Cube",
    "2x2x2": "2x2x2 Cube",
    "4x4x4": "4x4x4 Cube",
    "5x5x5": "5x5x5 Cube",
    "6x6x6": "6x6x6 Cube",
    "7x7x7": "7x7x7 Cube",
    "3x3 bld": "3x3x3 Blindfolded",
    "3x3 fm": "3x3x3 Fewest Moves",
    "3x3 oh": "3x3x3 One Handed",
    "clock": "Clock",
    "megaminx": "Megaminx",
    "pyraminx": "Pyraminx",
    "skewb": "Skewb",
    "sq1": "Square-1",
    "4x4 bld": "4x4x4 Blindfolded",
    "5x5 bld": "5x5x5 Blindfolded",
    "3x3 mbld": "3x3x3 Multi-Blind"
}

while True:  # The presence will stay on as long as the program is running
    data = GetWindowText(GetForegroundWindow()).split()
    if data[0] == "csTimer":
        RPC.update(state="ao5: " + data[10] + ", ao12: " + data[11], details="time: " + data[8] + ", mo3: " + data[9],
                   large_image=data[7].replace(" ", ""), large_text=tooltips[data[7]],
                   small_image="cstimer", small_text="csTimer")
    time.sleep(5)  # Update every 5 seconds
