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
        self.face_reg = FaceReg("file_path", self.log)
        self.arrangement_reader = ArrangementReader(self.log)
        self.camera_manager = CameraManager(self.log)
        self.tts = self.log.tts

        self.is_end = [
            False,
            False,
            False,
            False
        ]

        self.sign_result = {
            "扫地": {},
            "拖地": {},
            "杂物间+柜台": {},
            "摆桌椅": {},
            "窗户+窗台": {},
            "图书角+黑板+讲台": {},
            "倒垃圾": {}
        }

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

    def generate_report(self):

        """
        开始生成报告
        :return:
        """

    def run(self):

        """
        启动程序
        :return:
        """
        self.log.add_log("Init: System is now running...", 1)
        self.log.add_log("Init: Initializing...", 1)
        time_count_thread = threading.Thread(target=self.time_count, args=(1200, self.generate_report))
        time_count_thread.start()

        self.tts.start("同学们好啊，这里是由YYH开发的「自动劳动管理系统」。现在，让我们开始劳动吧")

        self.arrangement_reader.read_in()

        self.phase1_start()

    def phase1_sign(self):

        """
        开始签名
        :return:
        """
        print("""
            输入规则
            摆桌椅： 1 + 你摆的桌椅列数
            窗户+窗台： 2 + 窗户号
            黑板等： 3 即可
        """)
        while self.is_end:
            command = input("Command输入： ")
            self.camera_manager.capture_image()

            face_num = self.face_reg.face_detect(self.face_reg.read_img("img.jpg"))["face_num"]
            if face_num == 0:
                self.tts.start("没有检测到人脸，请对准摄像头重拍")
            else:
                self.tts.start("Face Detected. Start searching...")
            user_id = self.face_reg.face_search(self.face_reg.read_img("img.jpg"))["user_list"]["user_id"]

            if command[0] == "1":
                index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                          self.arrangement_reader.class_arrangement["摆桌椅"])
                self.sign_result["摆桌椅"][index] = True
            elif command[0] == "2":
               index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                         self.arrangement_reader.class_arrangement["窗户+窗台"])
               self.sign_result["窗户+窗台"][index] = True
            else:
                index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                          self.arrangement_reader.class_arrangement["图书角+黑板+讲台"])
                self.sign_result["图书角+黑板+讲台"][index] = True

    def phase1_start(self):

        """
        run
        :return:
        """
        self.log.add_log("Phase1: now start", 1)
        self.tts.start("现在，开始第一阶段。请以下同学留下，其余同学全部出去或在后面等着")
        table = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["摆座椅"])
        window = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["窗户+窗台"])
        blackboard = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["图书角+黑板+讲台"])

        self.tts.start("以下同学负责摆桌椅，现在开始工作。按照摆完以后请过来选择列数完成签名，")
        self.tts.start(table)
        self.tts.start("摆桌椅要求：全部拉开，保证一定距离以方面扫地拖地；椅子要翻上去")

        self.tts.start("以下同学负责擦窗台和窗户。按照读的顺序，每人一个窗，从只有窗户的一侧从前往后数，门的一侧也是从前往后数")
        self.tts.start(window)
        self.tts.start("窗户要求：用抹布擦干以后找报纸弄干，擦的时候要有规律，水不要太多。没有抹布要么等要么去对面借，完成以后过来签名")

        self.tts.start("以下同学负责整理黑板、图书柜、讲台")
        self.tts.start(blackboard)
        self.tts.start("黑板请擦干净，擦完以后一定打开屏幕，不要遮住了。讲台不要有垃圾，粉笔灰擦干净，完成后过来签名")

        video_recorder = threading.Thread(target=self.camera_manager.capture_video, args=("phase1-record1",))
        video_recorder.start()

        self.phase1_sign()


if __name__ == "__main__":
    classes = Init()
    classes.run()


