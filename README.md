# Autonomous M.A.R.S Rover Navigation
This project focuses on developing an autonomous navigation system for the [**4tronix M.A.R.S. Rover Robot**](https://4tronix.co.uk/blog/?p=2112) for **Raspberry Pi Zero**. The rover will autonomously navigate through a maze, with the possibility for manual control using a keypad, although the use of manual control is forowned upon and penalised.

## 🚀 Objective
The goal is to create an autonomous maze-solving system for the M.A.R.S. Rover, using sensors and algorithms to detect the environment and navigate through the maze without human intervention. Manual control is only allowed as a fallback.

## 🛠️ Requirements
- Hardware:
  - [4tronix M.A.R.S. Rover](https://core-electronics.com.au/4tronix-m-a-r-s-rover-robot-for-raspberry-pi-zero.html)
  - [Raspberry Pi Zero](https://core-electronics.com.au/raspberry-pi-zero-wh.html) (or any compatible Raspberry Pi)
  - Maze environment (physical setup)
- Software:
  - [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/)
  - Python 3.x
  - Required Python libraries (e.g., RPi.GPIO, time, numpy, opencv, etc.)
  - Git for version control

## ⚙️ Setup
1. To get started, clone this repository to your local machine or Raspberry Pi.
    ```bash
    git clone https://github.com/7echkilla/mars-rover-maze.git
    cd mars-rover-maze
    ```
2. Ensure you have all the necessary dependencies installed. You can install them using `pip install -r requirements.txt`. *Make sure your Raspberry Pi is connected to the internet and has access to the necessary libraries.*
---
3. Hardware Setup
- Connect the 4tronix M.A.R.S. Rover to the Raspberry Pi.
- Adjust the hardware configurations by modifying the `config.py` file. 

## 🤖 Navigation Algorithm
The rover will use a combination of sensors to navigate autonomously. Some of the key algorithms include:
- Obstacle detection: Using ultrasonic or infrared sensors to detect walls or obstacles.
- Pathfinding: A maze-solving algorithm like A*(A-star), breadth-first search (BFS), or depth-first search (DFS) will be used to find the shortest path through the maze.
- Motor control: The rover will use the Raspberry Pi's GPIO pins to control motors and actuators based on the algorithm's instructions.
### Key features:
- Autonomous mode: The rover will move on its own, avoiding obstacles and finding the best path through the maze.
- Manual control (penalized): Manual control through a keypad can be used if necessary, though it will result in penalties.
---

## 📂 Project Structure
/mars-rover-maze\
│\
├── config.py            # Configuration file for hardware setup\
├── rover.py             # Main control script for the rover\
├── pathfinding.py       # Algorithms for navigating through the maze\
├── sensors.py           # Code for interacting with sensors\
├── motor_control.py     # Motor control functions\
├── manual_control.py    # Code for manual control using the keypad\
├── requirements.txt     # List of required Python packages\
├── [README.md](./README.md)            # Project documentation\
└── /docs                # Additional documentation (if needed)\

## 🧑‍💻 Running the Project
To run the rover in autonomous mode: `python main.py`
This will start the rover and the algorithm will begin navigating the maze autonomously.
