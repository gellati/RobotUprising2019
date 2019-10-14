# Robot Uprising 2019

Notes from the Robot Uprising 2019 hackathon.

Codes are in the `pybricks`, `ev3dev2` and `mindstorms_labview`.

Codes were run on a Lego EV3 brick running the Brickman operating system.

## python-ev3dev2

[`python-ev3dev2`](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/) is a Python library for programming the EV3 brick. We were only able to run these codes on the robot brick. The programs were transferred with the [Visual Studio Code](https://code.visualstudio.com) `ev3dev-browser` plugin. This also allowed an SSH connection to the brick, where a Python 3 interpreter could be run as well, with the command

    python3

The files needed to be executable in order to run.

The folder contains an incomplete conversion of the `pybricks/main.py` program from using the `pybricks` library to use `ev3dev2` library.

## Pybricks

`pybricks` is a Python library for programming the EV3 brick. It might be faster than `ev3dev2`. We were not able to run scripts using this library.

The folder contains a script from the documentation at this [page](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3). It has not been tried out.

## Mindstorms Labview programs

The Lego Mindstorms educational website offers a [free version of Labview](https://education.lego.com/en-us/downloads/mindstorms-ev3/software) customised for programming EV3. The graphical programs are in the  `mindstorms_labview` folder.

## Extra challenges

Extra challenges were given during the hackathon. These challenges gave points that could be used to buy extra parts for the robot. Solutions in the `extra_challenge` folder.

## Other notes

- The remote control of the robot was done with an infrared controller. This due to  there being too much WiFi and Bluetooth interference. The controller requires proper line of sight to the infrared sensor.
- All the finalist robots used continuous tracks instead of wheels. This might have given them more traction to move.
- Better to start with making sure the manual steering works, then start with automated solutions.
- Smaller robot is faster and more agile in the maze, while a bigger robot is better in combat. As the combat is only at the end of the track, a small robot might be preferable.
- Programs can be made separate for each challenge. No need to make one big for all of them.
- Labview's graphical programming environment is more powerful than it initially appears.
