# 全自动班级劳动管理系统: Auto Labor Management System
- By Lan_zhijiang
- 开发这个纯属是因为这样管劳动课太麻烦了，既然能自动化，那就来练练手呗

## Introduction
- 本系统简洁明了，人脸识别签到并自动扣分生成报告，语音播报劳动阶段等等，全自动完成劳动课
- 本系统采用Python3开发，结合百度人脸识别和百度TTS以及OPENCV的人脸检测还有自己的人员安排系统完成

## Function
- 功能包括【人员安排生成】和【自动监管系统】两个
- 在自动按照所给的人员表和安排要求生成安排表之后，就可以直接运行监管系统，然后一劳永逸地坐在那里，等着同学按照电脑指示完成全部的劳动
- 劳动完成后将会自动完成未签到的扣分并生成json报告和录像视频
- 更有超简单的UI，同学一看就懂，一看就会用
- 反应速度快，机制完善，有效防止提前签，误签，跑路

## Installation
- 使用非常的简单
- 1、给出班级人员表(json)(参考./data/json/names.json)
- 2、给出安排要求(json)(参考./data/arrangement.json)
- 3、对接好自己的baidu人脸识别app
- 4、对接好自己的baidu TTS app
- 5、安装好摄像头并保证声卡正常
- 6、安装好python3.7运行环境
  - 要求的python库
    - opencv-python
    - pyaudio(windows需通过whl文件安装)
    - requests
    - numpy
- 运行即可
