# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/6
# description: The Main Part

from log import Log
from face_recognization import FaceReg
from arrangement_reader import ArrangementReader
from camera import CameraManager
import threading
from tkinter import *
import time


class Init:

    def __init__(self):

        self.log = Log()
        self.face_reg = FaceReg("file_path", self.log)
        self.arrangement_reader = ArrangementReader(self.log)
        self.camera_manager = CameraManager(self.log)
        self.tts = self.log.tts

        self.is_end = False

        self.sign_result = {
            "扫地": {},
            "拖地": {},
            "杂物间+柜台": {},
            "摆桌椅": {},
            "窗户+窗台": {},
            "图书角+黑板+讲台": {},
            "倒垃圾": {}
        }

        self.now_sign_row_index = 0

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

    def init_sign_window(self):

        """
        初始化签名窗口
        :return:
        """

        # INIT THE SIGN WINDOW
        window = Tk()
        window.title("Sign Window")
        window.geometry('1024x600')

        # SET THE NOTICE LABLE
        notice = Label(window, text="请点击按钮并签到", font=("Helvetica", 20))
        notice.pack(side=TOP)

        # 摆桌椅Frame
        desk_place = Frame(window)
        desc_desk = Label(window, text="摆桌椅签名区", font=("Helvetica", 15))
        desc_desk.pack(TOP)
        row_1_button = Button(matser=desk_place, height=15, width=20, command=lambda : self.sign(1, 1), text="列1")
        row_1_button.pack(RIGHT)
        row_2_button = Button(matser=desk_place, height=15, width=20, command=lambda: self.sign(1, 2), text="列2")
        row_2_button.pack(RIGHT)
        row_3_button = Button(matser=desk_place, height=15, width=20, command=lambda: self.sign(1, 3), text="列3")
        row_3_button.pack(RIGHT)
        row_4_button = Button(matser=desk_place, height=15, width=20, command=lambda: self.sign(1, 4), text="列4")
        row_4_button.pack(RIGHT)
        row_5_button = Button(matser=desk_place, height=15, width=20, command=lambda: self.sign(1, 5), text="列5")
        row_5_button.pack(RIGHT)
        row_6_button = Button(matser=desk_place, height=15, width=20, command=lambda: self.sign(1, 6), text="列6")
        row_6_button.pack(RIGHT)
        row_7_button = Button(matser=desk_place, height=15, width=20, command=lambda: self.sign(1, 7), text="列7")
        row_7_button.pack(RIGHT)
        row_8_button = Button(matser=desk_place, height=15, width=20, command=lambda: self.sign(1, 8), text="列8")
        row_8_button.pack(RIGHT)


        desk_place.pack(TOP)

        # RUN THE WINDOW
        window.mainloop()

    def sign(self, command, row):

        """
        进行签名
        :param command: 签到模式
        :param row: 列数
        :return:
        """
        img = self.camera_manager.capture_image()
        self.camera_manager.show_image(img)

        face_num = self.face_reg.face_detect(self.face_reg.read_img("img.jpg"))["face_num"]
        while True:
            if face_num == 0:
                self.tts.start("没有检测到人脸，请对准摄像头重拍")
            else:
                self.tts.start("Face Detected. Start searching...")
                break

        user_id = self.face_reg.face_search(self.face_reg.read_img("img.jpg"))["user_list"]["user_id"]

        if command == 1:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["摆桌椅"])
            if index + 1 == int(row):
                self.sign_result["摆桌椅"][index] = True

                next_name = self.arrangement_reader.class_arrangement["摆桌椅"][index]
                self.tts.start("请" + next_name + "同学开始扫地")

            else:
                self.tts.start("错误的人脸和对应列数！")
        elif command == 2:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["窗户+窗台"])
            if index + 1 == int(row):
                self.sign_result["窗户+窗台"][index] = True
            else:
                self.tts.start("错误的人脸和对应窗户号！")
        elif command == 3:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["图书角+黑板+讲台"])
            self.sign_result["图书角+黑板+讲台"][index] = True
        elif command == 4:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["扫地"])
            if index + 1 == self.now_sign_row_index:
                self.sign_result["扫地"][index] = True

                next_name = self.arrangement_reader.class_arrangement["扫地"][index]
                self.tts.start("请" + next_name + "同学开始拖地")

            else:
                self.tts.start("错误的人脸和对应列数！")
        elif command == 4:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["拖地"])
            if index + 1 == self.now_sign_row_index:
                self.sign_result["拖地"][index] = True

                next_name = self.arrangement_reader.class_arrangement["拖地"][index]
                self.tts.start("请" + next_name + "同学开始扫地")

            else:
                self.tts.start("错误的人脸和对应列数！")
        elif command == 5:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["扫地"])
            self.sign_result["倒垃圾"][index] = True

    def phase1_start(self):

        """
        run
        :return:
        """
        self.log.add_log("Phase1: now start", 1)
        self.tts.start("现在，开始第一阶段。请以下同学留下，其余同学全部出去或在后面等着")
        table = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["摆桌椅"])
        window = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["窗户+窗台"])
        blackboard = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["图书角+黑板+讲台"])

        self.tts.start(table)
        self.tts.start("这些同学负责摆桌椅，现在开始工作。按照摆完以后请过来选择列数完成签名，")
        self.tts.start("摆桌椅要求：全部拉开，保 证一定距离以方面扫地拖地；椅子要翻上去")

        time.sleep(0.5)
        self.tts.start(window)
        self.tts.start("然后，这些同学负责擦窗台和窗户。按照读的顺序，每人一个窗，从只有窗户的一侧从前往后数，门的一侧也是从前往后数")
        self.tts.start("窗户要求：用抹布擦干以后找报纸弄干，擦的时候要有规律，水不要太多。没有抹布要么等要么去对面借，完成以后过来签名")

        time.sleep(0.5)
        self.tts.start(blackboard)
        self.tts.start("这些同学负责整理黑板、图书柜、讲台")
        self.tts.start("黑板要擦干净，擦完以后一定打开屏幕，不要遮住了。讲台不要有垃圾，粉笔灰擦干净，完成后过来签名")

        video_recorder = threading.Thread(target=self.camera_manager.capture_video, args=("phase1-record1",))
        video_recorder.start()

        self.init_sign_window()

    def run(self):

        """
        启动程序
        :return:
        """
        self.log.add_log("Init: System is now running...", 1)
        self.log.add_log("Init: Initializing...", 1)
        time_count_thread = threading.Thread(target=self.time_count, args=(1200, self.generate_report))
        time_count_thread.start()

        self.tts.start("Hi~ 这里是袁翊闳开发的【自动劳动管理系统】")
        self.tts.start("主人~ 现在，是时候开始劳动了~")

        self.arrangement_reader.read_in()

        self.phase1_start()


if __name__ == "__main__":
    classes = Init()
    classes.run()


