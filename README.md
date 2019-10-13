# Robot Uprising 2019

Notes from the Robot Uprising 2019 hackathon.

Codes are in the `pybricks`, `ev3dev2` and `mindstorms_labview`.

Codes were run on a Lego EV3 brick running the Brickman operating system.


## python-ev3dev2

[`python-ev3dev2`](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/) is a Python library for programming the EV3 brick. We were only able to run these codes on the robot brick. The programs were transferred with the [Visual Studio Code](https://code.visualstudio.com) `ev3dev-browser` plugin. This also allowed an SSH connection to the brick, where a Python 3 interpreter could be run as well, with the command

    python3

The files needed to be executable in order to run.


## Pybricks

`pybricks` is a Python library for programming the EV3 brick. It might be faster than `ev3dev2`. We were not able to run this library.

## Mindstorms Labview programs

The Lego Mindstorms educational website offers a [free version of Labview](https://education.lego.com/en-us/downloads/mindstorms-ev3/software) customised for programming EV3. The graphical programs are in the  `mindstorms_labview` folder.

## Extra challenges

Extra challenges were given during the hackathon. These challenges gave points that could be used to buy extra parts for the robot. Solutions in the `extra_challenge` folder.


## Other notes

- the remote control of the robot was done with an infrared controller. This due to  there being too much WiFi and Bluetooth interference. The controller requires proper line of sight to the infrared sensor
- all the finalist robots used continuous tracks instead of wheels. This might have given them more traction to move
