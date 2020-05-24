import sched
import time
import random


class GPS_Plugin:
    def __init__(
        self, boot_delay: int = 15, update_interval: int = 15, demo: bool = False
    ):
        self.demo = demo
        if self.demo:
            self.demo_lat = 0.0
            self.demo_long = 0.0
        self.connected = False
        self.update_interval = update_interval
        # connect to gps, whatever that entails...
        # wait for boot_delay seconds and then call connect_gps_module
        # then after successful connect, start loop of calling send_gps_update

    def connect_gps_module(self):
        if self.demo:
            return True
        # not demo mode
        return False

    def poll_gps(self):
        if self.demo:
            self.demo_lat += (random.random() * 2 - 1) * 0.05
            self.demo_long += (random.random() * 2 - 1) * 0.05
            demo_data = {
                "lat": self.demo_lat,
                "lon": self.demo_long,
                "time": time.time(),
                "alt": random.random()*100,
                "speed": random.random()*15
            }
            return demo_data
        # not demo mode:
        return {}

    def send_data(self, gps_data):
        # make call to RxPy
        return False

    def update_gps(self):
        gps_data = self.poll_gps()
        data_sent = self.send_data(gps_data)
        # make repeat call for next gps update
