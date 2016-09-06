# CITS5503/5506 Project

## About
Joint project for CITS5503 (Cloud Computing) and CITS5506 (Ubiquitous Computing) units.

## Task
Yet to be formally specified but essentially, automated driving of remote bluetooth toy cars around a track that is identified and mapped by an IP camera.

### Functional Requirements

#### Dashboard
* Create a virtual representation of a map drawn on a flat surface (i.e. table top)
* Provide browser-based dashboard to show a representation of the course and the current location of cars on it.
* Provide history/logs of car position and actions communicated to the car (turn, stop, start etc).

#### Application
* Send instructions to bluetooth RC cars to drive around the map.
* Send instructions to dashboard for visualisation/logging.
* Ensure cars cover all roads in both directions (roads are bi-directional).
* Cars must avoid collisions.

### Non-functional Requirements
* Handle up to 15 cars on the course at any one time.
* Optionally support running on cloud resources, *yet to be defined/fleshed out*.
* Project must make use of Raspberry Pi units and cloud resources in some form.

## Software
* Python 3
* [OpenCV](http://docs.opencv.org/3.1.0/d6/d00/tutorial_py_root.html)

## Hardware
* Raspberry Pi 3
* [ZenWheels Micro Cars](http://zenwheels.com/)
* IP Camera (brand/model currently unknown)

## Tools
* AWS (specifics TBD)
