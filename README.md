# Autonomous M.A.R.S Rover Navigation
This project focuses on developing an **autonomous navigation system** for the [**4tronix M.A.R.S. Rover Robot**](https://4tronix.co.uk/blog/?p=2112) for **Raspberry Pi Zero**. The rover can navigate a maze autonomously and supports manual control via keyboard input, though manual overrides are penalised during [competition](https://www.facebook.com/events/1138916136930478?ref=newsfeed).

<p align="center">
  <img src="./media/Rover_Action.gif" alt="M.A.R.S. Rover in action" />
</p>

## 🚀 Objective
The goal is to create an autonomous maze-solving system for the M.A.R.S. Rover, using sensors and algorithms to detect the environment and navigate through the maze without human intervention. Manual control is only allowed as a fallback.

## 🛠️ Requirements
- Hardware:
  - [4tronix M.A.R.S. Rover](https://core-electronics.com.au/4tronix-m-a-r-s-rover-robot-for-raspberry-pi-zero.html)
  - [Raspberry Pi Zero](https://core-electronics.com.au/raspberry-pi-zero-wh.html) (or any compatible Raspberry Pi)
  - Physical maze setup for testing
- Software:
  - [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/) (or compatible)
  - Python 3.x
  - Required Python libraries (listed under [requirements.txt](./requirements.txt))
  - Git for version control

## ⚙️ Setup
1. To get started, clone this repository to your local machine or Raspberry Pi.
    ```bash
    git clone https://github.com/7echkilla/mars-rover-maze.git
    cd mars-rover-maze
    ```
2. Ensure you have all the necessary dependencies installed. You can install them using `pip install -r requirements.txt`.
3. Hardware Setup
    - Connect the 4tronix M.A.R.S. Rover to the Raspberry Pi.
    - Servo and motor configuration is handled in [main.py](./main.py). Adjust values if needed.

## 🤖 Navigation Algorithm
The rover uses sensors and algorithms to navigate autonomously:
- Obstacle detection: Using ultrasonic or infrared sensors to detect walls or obstacles.
- Pathfinding: A maze-solving algorithm like A*(A-star), breadth-first search (BFS), or depth-first search (DFS) can be used to find the shortest path through the maze.
- Motor control: The rover will use the Raspberry Pi's GPIO pins to control motors and actuators based on the algorithm's instructions.

### Key features:
- Autonomous mode: The rover will move on its own using a simple wall-following algorithm.
- Manual override: Keyboard control is available via [driveRover.py](./src/driveRover.py) for emergency or testing purposes.

## 📂 Project Structure
mars-rover-maze/\
│\
├── src/\
│   ├── [\_\_init\_\_.py](./src/__init__.py)            # Python package initialiser\
│   ├── [calibrateServos.py](./src/calibrateServos.py)  # Setup and calibration routines for servos\
│   ├── [driveRover.py](./src/driveRover.py)            # Manual drive mode controlled via keyboard\
│   ├── [gyro.py](./src/gyro.py)                        # Gyroscope management functions\
│   ├── [keypad.py](./src/keypad.py)                    # Keypad input handling\
│   ├── [ledTest.py](./src/ledTest.py)                  # Functions to test LEDs on the robot\
│   ├── [manualControl.py](./src/manualControl.py)      # Manual control wrapper (used by main.py)\
│   ├── [motorTest.py](./src/motorTest.py)              # Test motor functions on the robot\
│   ├── [pathFinding.py](./src/pathFinding.py)            # Autonomous drive function\
│   ├── [pca9685.py](./src/pca9685.py)                  # Interface for the PCA9685 servo driver\
│   ├── [rover.py](./src/rover.py)                      # Core robot functions: movement, servo control, cleanu\
│   ├── [servoTest.py](./src/servoTest.py)              # Test servo movements\
│   └── [sonarTest.py](./src/sonarTest.py)              # Test ultrasonic sensor readings\
│\
├── [main.py](./main.py)                                # Entry point: initialises rover and runs autonomous/manual mode\
├── [requirements.txt](./requirements.txt)              # Python dependencies\
├── [LICENSE](./LICENSE)                                # Project license (MIT)\
├── [media/](./media/)                                  # Photos, videos and presentation for event documentation\
└── [README.md](./README.md)                            # Project documentation

## 🧑‍💻 Running the Project
1. Run the project using `python main.py`
2. When prompted, press `a` for autonomous navigation or `m` for manual override. Keyboard controls are handled by [driveRover.py](./src/driveRover.py), press Ctrl+C to exit manual mode and return to main program.
