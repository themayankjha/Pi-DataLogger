## Raspberry Pi Web-Server based Data Logger and Graph Plotter
---
#### Overview
Built for Raspberry Pi using Python.
All the steps mentioned below assumes that you ahave a Raspberry Pi running linux and have Python installed.

---
#### Functionality
- This application senses if an ultrasonic sensor connected to defined pins  with Trigger on 2 and Echo on 3 reads distance less than 35 cm for 10 seconds and then logs the current time in the format Hour.Minute to a text file.
- Then the generated text file is worked upon and a histogram is plotted. The histogram is then saved as a PNG file with its name as the current date in a folder
- A webserver running on port 8081 displays the same PNG File so that it can be accessed by any device on local network.

---
#### Usage
 This acts as a basic wireframe to get started with connecting a sensor to Raspberry Pi, collecting data from it and modifying data such as to present in a simpler form.You can extend this code to allow multiple sensors gather and display data all at once. 

---
#### Running

```sh
$ git clone https://github.com/themayankjha/RaspberryPi-WebBased-DataLogger.git
$ cd RaspberryPi-WebBased-DataLogger
$ cd bin
$ pip install -r requirements.txt
$ python sensor.py&
$ gunicorn __init__:app -b localhost:8081
```
Open your web browser and goto :- https://localhost:8081/

![Screenshot](screenshot/screenshot.png?raw=true "screenshot")

 ---
#### Copyright

Copyright (c) 2021 [Mayank Jha](https://github.com/themayankjha)
License - [MIT](License.md)

---