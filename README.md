# BFBC2-Network-Overlay
![asset](https://github.com/S3nouy/BFBC2-Ping-Overlay/assets/77050462/0228ef2a-5eac-4560-976f-6e05764fc5e4)


# Credits
-Senouy
# Overview
This custom made Network Overlay is a Python script designed to provide real-time ping statistics for Battlefield: Bad Company 2 game servers. It uses the Tkinter library to create a simple graphical user interface (GUI) overlay that displays ping information for a selected game server. The overlay updates the ping information at regular intervals (faster that default ingame one), allowing you to monitor the stability of your connection to the chosen server.

`For Downloading you can find the linux binary in the Releases` 
# How does it all work
![edited diagram](https://github.com/S3nouy/BFBC2-Ping-Overlay/assets/77050462/41d2692e-f78a-4050-a58c-0b7cc02b4f7a)

The figure to the left shows how your machine communicates to the game server, and also retreives ping statistics. what you see is your network traffic goes all the way to the Nexus Backend Server then it gets routed to the game server you are playing on. That adds an additional 20ms to say the least to your ping which is shown in the scoreboard.

Unlike when using the Overlay, you get real ping time directly from the game server without the need for your traffic to go all the way to the Nexus server, plus it updates faster than the regular one in the scoreboard. Giving you faster insights on how your network speed is performing and also helps stabilize the connection between you and the game server. Something I found out when testing it for hours.
# How to Use
Server Selection: Choose a game server from the dropdown menu.

Start : Click the "Start" button to initiate the ping process.

Ping Information: The overlay displays real-time ping information, including ping time, packet loss (if available), and additional statistics.

Continuous Updates: The overlay continuously updates the ping information at one-second intervals.

![list](https://github.com/S3nouy/BFBC2-Ping-Overlay/assets/77050462/df99466c-916c-4445-b245-2c4d8fc4c882)
# Work in Progress
This project is still under development, and there are numerous features I am planning to add in the next version.

Feel free to reach out if you have any questions, feedback, or would like to show support.

Contact me on Discord: CptYounes#1716.

/See you on the Battlefield! 
