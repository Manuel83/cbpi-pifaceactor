# -*- coding: utf-8 -*-
import time

from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property

try:
    import pifacedigitalio as piface

except Exception as e:
    cbpi.notify("Initialize PiFace failed", "Please make sure to run: sudo apt-get install python-pifacedigitalio", type="danger", timeout=None)
    pass


@cbpi.actor
class PiFace(ActorBase):

    relay = Property.Select("PiFace Relay", options=[0,1,2,3,4,5,6,7])
    @classmethod
    def init_global(cls):
        try:
            piface.init()
        except Exception as e:
            pass

    def on(self, power=0):
        self.api.app.logger.info("SWITCH ON")
        piface.digital_write(int(self.relay), 1)
        self.api.app.logger.info("SWITCH ON DONE")

    def off(self):
        self.api.app.logger.info("SWITCH OFF")
        piface.digital_write(int(self.relay), 0)
        self.api.app.logger.info("SWITCH OFF DONE")


