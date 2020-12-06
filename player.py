# coding=utf-8
# author: Lan_zhijiang
# description: player
# date: 2020/10/1

import pyaudio
import wave


class Player():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting

        self.p = pyaudio.PyAudio()

    def play(self, fp):

        """
        基本play
        :param fp: 文件路径
        :return:
        """
        try:
            wf = wave.open(fp)
        except wave.Error:
            print("Player: Cannot open the file")
            return

        stream = self.p.open(
            format=self.p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(1024)
        while data != "":
            stream.write(data)
            data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()
        self.p.terminate()

    def say(self):

        """
        播放say.wav
        :return:
        """
        print("Player: Now playing say.wav")
        self.play(r"./data/audio/say.wav")
