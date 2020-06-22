# csTimerRP<br>![build passing](https://img.shields.io/badge/build-passing-brightgreen)

Discord Integration for csTimer. Be sure to select the scramble that corresponds to the event that you are practicing. Make sure that you have "Display currently running game as status message" enabled in User Settings > Game Activity.

###### Chrome Setup
1. Install [this](https://chrome.google.com/webstore/detail/run-javascript/lmilalhkkdhfieeienjbiicclobibjao) Chrome extension
2. Visit [csTimer.net](https://cstimer.net/)
3. Click on the extension's icon, and paste the code from [update.js](update.js)
4. Check "Enable on cstimer.net" in the top right and click Save & Run
5. Click off of the window and refresh csTimer

###### Python Setup
1. Install [Python](https://www.python.org/downloads/) and check "Add to PATH" during setup
2. Download or clone this repository
3. Shift + Right Click inside of the folder and open a powershell or command prompt
4. Run `pip install -r requirements.txt` to install dependencies
5. Ensure that you have Discord open
6. From now on, all you need to do is run `py main.py` in the folder to start the Rich Presence
7. The presence will update every 5 seconds provided you are on the csTimer window
