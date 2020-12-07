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













