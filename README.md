# UK Flood Warning System

This repository is a project I did in my first year of engineering, where I used data science (and no pre-built libraries) to predict whether floods are expected near UK rivers in real time.

The system first reads data from the Government of United Kigdom's real time records, and preprocesses the data.

Once the data is in a form that can be worked with, the program uses stochastic gradient descent for all the stations to predict which station is likely to overflow.

Once such a station is found, an automated message is sent to the user to check for validity of the warning manually.
