# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/5
# description: baidu tts

import requests
import urllib.parse
from player import Player


class BaiduTts:

    def __init__(self):

        self.player = Player()

        self.token = ""
        self.app_id = ""
        self.app_key = ""

        self.get_token()

    def get_token(self):

        """
        获取token
        :return: bool
        """
        print("BaiduTts: getting token...")
        url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + self.app_id +\
              "&client_secret=" + self.app_key

        res = requests.get(url)

        if res.status_code == 200:
            self.token = res.json()["access_token"]
            print("BaiduTts: get success")
            return True
        else:
            print("BaiduTts: meet error when getting token!")
            return False

    def start(self, text):

        """
        开始合成
        :param text: 要合成的文本
        :return: bool
        """
        print("BaiduTts: requesting tts..., text: " + text)

        text = urllib.parse.quote(bytes(text.encode("utf-8"))) # ATTENTION, error may be here

        url = "http://tsn.baidu.com/text2audio"
        param = {
            "tex": text,
            "tok": self.token,
            "cuid": "ALMS",
            "ctp": 1,
            "lan": "zh",
            "per": 4,
            "aue": 6
        }

        res = requests.post(url,
                            body=param)

        if "audio" in res.headers["Content-Type"]:
            print("BaiduTts: tts requested success")
            with open("./data/audio/say.wav", "wb+") as f:
                f.write(res.content)
            self.player.say()
            return True
        else:
            print("BaiduTts: tts requested fail!")
            return False



