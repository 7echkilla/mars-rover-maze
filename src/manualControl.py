"""
Manual control entry point
Uses driveRover.py to control the rover via keypad/arrow keys
"""

from driveRover import *

if __name__ == "__main__":
    try:
        while True:
            pass  # driveRover.py already handles the loop
    except KeyboardInterrupt:
        rover.cleanup()
        print("[INFO] Manual control ended.")
