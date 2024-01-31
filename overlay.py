import tkinter as tk
from tkinter import ttk
import time
import statistics
import subprocess

class PingConnect:
    CONNECTED = 1
    NOT_CONNECTED = 2

class Pinger:
    def __init__(self, ip_address: str):
        if ':' in ip_address:
            self.ip_address, self.port = ip_address.split(':')
        else:
            self.ip_address = ip_address
            self.port = None

    def get_ping_time(self) -> tuple[PingConnect, int]:
        response = subprocess.run(
            ['ping', '-c', '1', '-W', '1', self.ip_address],
            stdin=subprocess.PIPE,
            capture_output=True,
            encoding='utf-8',
        )
        if response.returncode != 0:
            return PingConnect.NOT_CONNECTED, -1

        for line in response.stdout.splitlines():
            if 'time=' in line:
                time_ms = line.split('time=')[1].split(' ')[0]
                return PingConnect.CONNECTED, int(float(time_ms))

        return PingConnect.NOT_CONNECTED, -1

    def get_packet_loss(self) -> float:
        response = subprocess.run(
            ['ping', '-c', '10', self.ip_address],
            stdin=subprocess.PIPE,
            capture_output=True,
            encoding='utf-8',
        )
        if response.returncode != 0:
            return -1  # Unable to determine packet loss

        for line in response.stdout.splitlines():
            if 'packet loss' in line:
                loss_percentage = line.split('packet loss')[0].split(',')[-1].strip('% ')
                try:
                    return float(loss_percentage)
                except ValueError:
                    return -1  # Unable to convert to float

        return -1  # Unable to determine packet loss

class Overlay:
    def __init__(self, server_data):
        self.root = tk.Tk()
        self.root.title("Ping Overlay")

        self.server_names = [entry[0] for entry in server_data]
        self.selected_server = tk.StringVar()
        self.selected_server.set(self.server_names[0])  # Default to the first server

        self.server_dropdown = ttk.Combobox(self.root, textvariable=self.selected_server, values=self.server_names)
        self.server_dropdown.grid(row=0, column=0, padx=10, pady=10)

        self.start_button = tk.Button(self.root, text="Start Ping", command=self.start_ping)
        self.start_button.grid(row=0, column=1, padx=10, pady=10)

        self.ping_info_var = tk.StringVar()
        self.ping_info_label = tk.Label(self.root, textvariable=self.ping_info_var, font=('Consolas', 14))
        self.ping_info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.server_data = {entry[0]: entry[1] for entry in server_data}
        self.pinger_instance = Pinger(self.server_data[self.server_names[0]])  # Default to the first server

        self.ping_info_toplevel = tk.Toplevel(self.root)
        self.ping_info_toplevel.overrideredirect(True)
        self.ping_info_toplevel.geometry("+5+5")
        self.ping_info_toplevel.wm_attributes("-topmost", True)
        self.ping_info_toplevel.wm_attributes("-alpha", 0.6)
        self.ping_info_toplevel.configure(borderwidth=0, highlightthickness=0)
        self.ping_info_toplevel.resizable(False, False)
        self.ping_info_toplevel.wm_attributes("-type", "splash")

        self.ping_info_var_top = tk.StringVar()
        self.ping_info_label_top = tk.Label(self.ping_info_toplevel, textvariable=self.ping_info_var_top, font=('Consolas', 14))
        self.ping_info_label_top.grid(row=0, column=0, padx=10, pady=10)

        self.ping_times = []  # Initialize list for ping times

    def start_ping(self):
        selected_server_name = self.selected_server.get()
        self.pinger_instance = Pinger(self.server_data[selected_server_name])
        self.update_ping()

    def update_ping(self):
        ping_connect, ping_time = self.pinger_instance.get_ping_time()
        packet_loss = self.pinger_instance.get_packet_loss()

        if ping_connect == PingConnect.CONNECTED:
            ping_info = f"Ping: {ping_time} ms"
            if packet_loss != -1:
                ping_info += f" | Packet Loss: {packet_loss}%"

                # Calculate and display min, avg, and max ping
                if ping_time != -1:
                    self.ping_times.append(ping_time)
                    avg_ping = round(statistics.mean(self.ping_times), 2)
                    min_ping = round(min(self.ping_times), 2)
                    max_ping = round(max(self.ping_times), 2)

                    ping_info += f" | Avg: {avg_ping} ms | Min: {min_ping} ms | Max: {max_ping} ms"
        else:
            ping_info = "Ping: Not Connected"

        self.ping_info_var.set(ping_info)
        self.ping_info_var_top.set(ping_info)

        self.root.after(1000, self.update_ping)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    server_data = [
    ("#3 [DvsH] | [Atacama/HM Only] |", "213.168.89.234"),
    ("#1 [DvsH] SP Maps MODS REQUIRED! - INFO->>", "213.168.89.234"),
    ("Alt-F4 Atacama Desert / Laguna Presa", "104.243.43.224"),
    ("USSR HARD RUSH", "185.189.255.152"),
    ("Twisted Heavy Metal 2 - 600 Tickets", "47.189.17.10"),
    ("Off DeathMatch", "216.144.141.92"),
    ("Salty Bawls [US] RUSH NFOservers", "64.74.97.92"),
    ("Vietnam with no Borders", "116.240.79.155"),
    ("GOUROU_BC2_CONQUETE", "90.120.84.190"),
    ("EUROPE - HEAVY METAL - 24/7", "37.114.42.51"),
    ("THB Gaming #1 | CQ (+60%25 wpn damage)", "84.234.163.149"),
    ("THB Gaming #2 | Rush (+60%25 wpn damage)", "84.234.163.149"),
    ("THB Gaming #3 | CQ Infinite Ammo/No Reload", "84.234.163.149"),
    ("THB Gaming #4 | Vietnam CQ (+60%25 wpn damage)", "84.234.163.149"),
    ("Joe's Sniper Heaven", "77.239.42.122"),
    ("H3AVY M3TAL C!NQ N3UF", "88.169.139.160"),
    ("RUSH C!NQ N3UF", "88.169.139.160"),
    ("[T.B.C.]THE BEAVER COMMANDO - BF2 SQDM Home", "69.131.91.70"),
    ("Fire & Frost Reborn - VIETNAM 24/7 + BOTS", "188.127.241.186"),
    ("Test222", "37.139.99.40"),
    ("Alt-F4 AlterEgo", "104.128.58.2"),
    ("TEST", "37.139.99.40"),
    ("CONQUEST without Atacama and Heavy Metal", "45.14.111.157"),
    ("Hardcore - CONQUEST", "45.14.111.157"),
    ("[BraveUA] SQDM without mods", "45.14.111.157"),
    ("Hardcore - Squad Rush", "45.14.111.157"),
    ("[BraveUA] RUSH without mods", "45.14.111.157"),
    ("AWOG Conquest / Rush [2x Tickets][1 RND/Map]", "88.99.153.148"),
    ("SERVER = ARMY OF DEATH =", "185.207.214.41"),
    ("EUROPE - VIETNAM - 24/7", "87.251.76.139"),
    ("[UK] Modded Hardcore | Squad Deathmatch", "185.225.3.14"),
    ("[UK] Conquest | Modded | 32+ Players", "185.225.3.14"),
    ("TEAMCCCP.RU | RUSH | BEST MAPS! NO LAGS!", "194.190.92.29"),
    ("TEAMCCCP.RU | ATACAMA 24/7 | Fast Resp", "194.190.92.29"),
    ("TEAMCCCP.RU | SDM | HARDCORE", "194.190.92.29"),
    ("CLAN GROZNY HC RUSH 24/7 I 60Hz + BOTS", "188.127.241.186"),
    ("Fire & Frost Reborn - Arica Harbor 24/7 + BOTS", "51.195.124.224"),
    ("EZ8 | https://discord.gg/FEUPPMA", "89.74.14.45"),
    ]

    overlay = Overlay(server_data)
    overlay.run()
