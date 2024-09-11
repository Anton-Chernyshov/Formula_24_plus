# F24
This is made to keep track of the F24+ telemetery project since this is going to be fairly complicated. Instructions for setting it up / operating the program are provided below should it go wrong and i am not there.

# Versons
The program isnt finished yet, but this will be updated when i have finished with a basic implementation of it.

# How it works
The basic idea is that the program uses Flask to host a web server and website that displays information from the cars sensors on a simple website. However this can only work over WiFi, so this will be used for close range testing and for the phone on the car's steering wheel. The program will also log sensor data into files and will graph them when the logging session has ended. The program will also be able to send these sensor readings over long range ( 1Mi+ ) radio antenna to a ground station that can collect and display the data to be seen when the car is being driven. This will allow for both the ground crew and the driver to see the data whilst the car is being driven.

It will use a Raspberry Pi 4B+ as the controller for the server, which may be overkill but it has good power efficiency for processing power, and will consume less power running the same code as the Pi 3B+ ( The cheaper alternative ).

# How to setup / Fix
 
## setup

## Bugfix

# Known issues
