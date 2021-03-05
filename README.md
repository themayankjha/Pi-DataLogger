## Raspberry Pi Web-Server based Data Logger and Graph Plotter
---
#### Overview
Built for Raspberry Pi in Python.


---
#### Functionality
- This application senses if an ultrasonic sensor connected to defined pins  with Trigger on 2 and Echo on 3 reads distance less than 35 cm for 10 seconds and then logs the current time in the format Hour.Minute to a text file.
- Then the generated text file is worked upon and a histogram is plotted. The histogram is then saved as a PNG file with its name as the current date in a folder
- A webserver running on port 8081 displays the same PNG File so that it can be accessed by any device on local network.

---
 #### Running

 ```sh
 $ git clone <Repository Name>
 $ pip install -r requirements.txt
 $ gunicorn app:__init__.py
 ```
 Open your web browser and goto :- https://localhost:8081/

 ---
 #### Copyright
Copyright (c) 2021 [Mayank Jha](https://github.com/themayankjha)
License - [MIT](License.md)