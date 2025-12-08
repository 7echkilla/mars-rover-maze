"""
Main entry point for M.A.R.S. Rover Hackathon
- Handles autonomous maze navigation
- Overrides autonomous control with manual input if needed
"""

import time
from src import rover, driveRover, manualControl, pathFinding

# servo numbers
SERVO_FL = 9
SERVO_RL = 11
SERVO_FR = 15
SERVO_RR = 13
SERVO_MA = 0

# default speed for autonomous driving
DEFAULT_SPEED = 60

# ultrasonic sensor threshold for obstacles
OBSTACLE_DIST_CM = 20

# LED brightness (0-255)
LED_BRIGHTNESS = 50

def autonomous_mode():
    print("[INFO] Starting autonomous mode")
    try:
        pathFinding.wall_following(speed=DEFAULT_SPEED, distance_threshold=OBSTACLE_DIST_CM)
    except KeyboardInterrupt:
        print(f"\033[33m[WARN]\033[0m Autonomous mode interrupted")
        rover.stop()
        rover.cleanup()

def manual_override():
    print("[INFO] Switching to manual control, press Ctrl+C to exit")
    driveRover.__dict__.update({'__name__': '__main__'})  # trick driveRover to run standalone
    import src.driveRover as dr
    pass

if __name__ == "__main__":
    rover.init(LED_BRIGHTNESS)
    try:
        while True:
            mode = input("[INFO] Press 'm' for manual, 'a' for autonomous: ").strip().lower()
            if mode == 'm':
                manual_override()
            elif mode == 'a':
                autonomous_mode()
            else:
                print(f"\033[31m[FAIL]\033[0m Invalid choice. Type 'm' or 'a'.")
    except KeyboardInterrupt:
        print(f"\033[33m[WARN]\033[0m Exiting program")
    finally:
        rover.stop()
        rover.cleanup()
