# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/6
# description: The Main Part

from log import Log
from face_recognization import FaceReg
from arrangement_reader import ArrangementReader
from camera import CameraManager
from phases import *
import threading
import time


class Init:

    def __init__(self):

        self.log = Log()
        self.face_reg = FaceReg(self.log)
        self.arrangement_reader = ArrangementReader(self.log)
        self.camera_manager = CameraManager(self.log)
        self.tts = self.log.tts

        self.phase1 = Phase1(self.log, elf.tts, self.arrangement_reader, self.camera_manager)

    def time_count(self, second, callback):

        """
        计时器
        :param second: 计算的秒数
        :param callback: 时间到以后的callback
        :return:
        """
        self.log.add_log("Init: Start time count for" + str(second), 1)
        time.sleep(second)
        callback()

    def run(self):

        """
        启动程序
        :return:
        """
        self.log.add_log("Init: System is now running...", 1)
        time_count_thread = threading.Thread(target=self.time_count, args=(1200, self.reporter.start))
        time_count_thread.start()

        self.tts.start("同学们好啊，这里是由YYH开发的「自动劳动管理系统」。现在，让我们开始劳动吧")

        self.arrangement_reader.read_in()

        self.phase1.start()


if __name__ == "__main__":
    classes = Init()
    classes.run()


