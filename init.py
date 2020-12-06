# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/6
# description: The Main Part

from log import Log
from reporter import Reporter
import threading
import time


class Init:

    def __init__(self):

        self.log = Log()
        self.tts = self.log.tts
        self.reporter = Reporter(self.log)

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
        self.log.add_log("Init: System now running...", 1)
        time_count_thread = threading.Thread(target=self.time_count, args=(1200, self.reporter.start))
        time_count_thread.start()


if __name__ == "__main__":
    classes = Init()
    classes.run()


