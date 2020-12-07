# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/7
# description: the core of this system

import threading


class Phase1:

    def __init__(self, log, sign_manager, tts, arrangement_reader, camera_manager, face_reg):

        self.log = log
        self.tts = tts
        self.sign_manager = sign_manager
        self.arrangement_reader = arrangement_reader
        self.camera_manager = camera_manager
        self.face_reg = face_reg()

        self.is_end = False

    def start_sign(self):

        """
        开始签名
        :return:
        """
        print("""
            输入规则
            扫地： 1 + 扫地列数
            窗户+窗台： 2 + 窗户号
            黑板等： 3 即可
        """)
        while self.is_end:
            command = input("Command输入： ")
            if command[0] == "1":
                self.camera_manager.capture_image()
                user_id = self.face_reg.face_search(self.face_reg.read_img("img.jpg"))["user_list"]["user_id"]
                self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)), self.arrangement_reader.get_sweep_list())
                



    def start(self):

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

        self.sign_manager.phase_run()

        video_recorder = threading.Thread(target=self.camera_manager.capture_video, args=("phase1-record1",))
        video_recorder.start()

        self.start_sign()










