"""
Basic maze navigation algorithms for autonomous mode
Uses sensors and motor functions from rover.py
"""

from src import rover, gyro
import time

# simple wall-following algorithm
def wall_following(speed=50, distance_threshold=20):
    """
    Simple left-wall-following logic:
    - Move forward if clear
    - Turn right if obstacle in front
    - Keep left wall distance ~distance_threshold
    """
    try:
        while True:
            distance = rover.getDistance()
            if distance < distance_threshold:
                # obstacle detected
                rover.stop()
                time.sleep(0.2)
                rover.spinLeft(speed)
                time.sleep(0.5)  # spin for a short duration
                rover.stop()
            else:
                rover.forward(speed)
            time.sleep(0.05)
    except KeyboardInterrupt:
        rover.stop()
