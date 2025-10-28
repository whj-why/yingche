# -*- encoding=utf8 -*-
__author__ = "王瀚鋆"
__title__ = "千年之旅UI自动化"
__desc__ = """
正式服冒烟测试
"""

from airtest.core.api import *
from airtest.core.android.recorder import *
from airtest.core.android.adb import *
from airtest.report.report import simple_report, LogToHtml
import traceback

from server_qywx import sendmessage

auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:16512"])
sender = sendmessage(key="22a6a656-0fea-4ff4-b697-2fdd08729d49")
export_dir = r"H:\Millennium Journey_Automation\ch_smoke.air\ch_smoke.log"
html_file = os.path.join(export_dir, "test.html")
change_name = ''.join(random.choice('ab4defghijkl1opqr9341tuvwxyz') for _ in range(8))
qianming = ''.join(random.choice('我拍你') for _ in range(120))

#循环跳过下一个
#连接设备
def connect_emulator(host="127.0.0.1", port="16512"):
    # 方法1：用 subprocess
    subprocess.run(f"adb connect {host}:{port}", shell=True)
    # 等待连接
    time.sleep(2)
    # 连接 Airtest 设备
    dev = connect_device(f"Android://{host}:{port}")
    return dev

#异常处理
def erro_pass():
    cmd = [
        "am", "force-stop", "com.yingche.qnzl"
    ]
    dev.shell(cmd)
def cross_stage_new():
    while exists(Template(r"tpl1757575255706.png", record_pos=(0.314, -0.26), resolution=(1600, 900))):
        touch((1227,390))
        sleep(1)
        if exists(Template(r"tpl1761537483728.png", record_pos=(0.429, -0.121), resolution=(1600, 900))):
            sleep(1)
            touch(Template(r"tpl1757574621581.png", record_pos=(0.359, 0.241), resolution=(1600, 900)))
            try:
                wait(Template(r"tpl1757574551409.png", threshold=0.85, record_pos=(0.231, -0.201), resolution=(1600, 900)),timeout=100)
                sleep(2)
            except TargetNotFoundError:
                print("失败")
            if exists(Template(r"tpl1757576653515.png", record_pos=(0.009, -0.052), resolution=(1600, 900))):
                sleep(1)
                touch(Template(r"tpl1757576664709.png", record_pos=(-0.008, 0.124), resolution=(1600, 900)))
                sleep(1)
            else:
                pass
            sleep(1)
            if exists(Template(r"tpl1757574648855.png", record_pos=(-0.307, 0.228), resolution=(1600, 900))):
                sleep(2)
                touch(Template(r"tpl1757574648855.png", record_pos=(-0.307, 0.228), resolution=(1600, 900)))
                sleep(2)
            else:
                pass
        else:
            touch(Template(r"tpl1757574669706.png", record_pos=(0.333, -0.098), resolution=(1600, 900)))
            sleep(1)
            if exists(Template(r"tpl1757574688413.png", record_pos=(-0.002, -0.121), resolution=(1600, 900))):
                touch((232,144))
                sleep(1)
            else:
                raise("闯关失败")
#闯关
def cross_stage():
    while exists(Template(r"tpl1757575255706.png", record_pos=(0.314, -0.26), resolution=(1600, 900))):
        if exists(Template(r"tpl1757574854634.png", record_pos=(0.211, -0.05), resolution=(1600, 900))):
            sleep(1)
            touch(Template(r"tpl1757574614508.png", record_pos=(0.224, -0.043), resolution=(1600, 900)))
            sleep(2)
            touch(Template(r"tpl1757574621581.png", record_pos=(0.359, 0.241), resolution=(1600, 900)))
            try:
                wait(Template(r"tpl1757574551409.png", threshold=0.85, record_pos=(0.231, -0.201), resolution=(1600, 900)),timeout=100)
                sleep(2)
            except TargetNotFoundError:
                print("失败")
            if exists(Template(r"tpl1757576653515.png", record_pos=(0.009, -0.052), resolution=(1600, 900))):
                sleep(1)
                touch(Template(r"tpl1757576664709.png", record_pos=(-0.008, 0.124), resolution=(1600, 900)))
                sleep(1)
            else:
                pass
            sleep(1)
            if exists(Template(r"tpl1757574648855.png", record_pos=(-0.307, 0.228), resolution=(1600, 900))):
                sleep(2)
                touch(Template(r"tpl1757574648855.png", record_pos=(-0.307, 0.228), resolution=(1600, 900)))
                sleep(2)
            else:
                pass
        else:

            touch(Template(r"tpl1757574669706.png", record_pos=(0.333, -0.098), resolution=(1600, 900)))
            sleep(1)
            if exists(Template(r"tpl1757574688413.png", record_pos=(-0.002, -0.121), resolution=(1600, 900))):
                touch((232,144))
                sleep(1)
            else:
                raise("闯关失败")
def maoyan():
    try:
        if exists(Template(r"tpl1756871444686.png", record_pos=(-0.451, -0.241), resolution=(1600, 900))):
            print("正常进入冒烟步骤")
            touch(Template(r"tpl1756871444686.png", record_pos=(-0.451, -0.241), resolution=(1600, 900)))
        else:
            raise Exception("因为新手教程未过导致无法进入冒烟")
        sleep(2)
        touch((979, 132))
        touch(Template(r"tpl1756871476424.png", record_pos=(-0.124, -0.099), resolution=(1600, 900)))
        touch(Template(r"tpl1756871483351.png", record_pos=(0.294, 0.197), resolution=(1600, 900)))
        if exists(Template(r"tpl1756872502657.png", record_pos=(0.294, 0.186), resolution=(1600, 900))):
            touch(Template(r"tpl1756871573562.png", record_pos=(0.178, -0.205), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception("无法更改头像")
        if exists(Template(r"tpl1756871748592.png", record_pos=(0.294, 0.037), resolution=(1600, 900))):
            touch(Template(r"tpl1756871760451.png", record_pos=(0.323, -0.201), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception("无法切换头像框")
        if exists(Template(r"tpl1756871829848.png", record_pos=(0.301, -0.066), resolution=(1600, 900))):
            touch(Template(r"tpl1756871841003.png", record_pos=(0.297, 0.194), resolution=(1600, 900)))
        else:
            raise Exception("无法切换称号")

        if exists(Template(r"tpl1756872568438.png", record_pos=(0.282, 0.189), resolution=(1600, 900))):
            touch(Template(r"tpl1756871968502.png", record_pos=(-0.456, 0.069), resolution=(1600, 900)))
        else:
            raise Exception("无法更改称号")
        touch((1527, 57))
        sleep(1)
        if exists(Template(r"tpl1756872681931.png", record_pos=(0.013, -0.126), resolution=(1600, 900))):
            touch(Template(r"tpl1756872688015.png", record_pos=(0.011, -0.021), resolution=(1600, 900)))

            text(f"{change_name}")
            touch(Template(r"tpl1756872796998.png", record_pos=(0.455, 0.251), resolution=(1600, 900)))
            touch(Template(r"tpl1756872801285.png", record_pos=(0.16, 0.081), resolution=(1600, 900)))
        else:
            raise Exception("无法打开修改名称界面")
        if exists(Template(r"tpl1756873262185.png", record_pos=(0.191, -0.247), resolution=(1600, 900))):
            print("昵称修改成功")
            touch((1497, 168))

            touch(Template(r"tpl1756873356858.png", record_pos=(0.039, -0.036), resolution=(1600, 900)))
            text(f"{qianming}")
            touch(Template(r"tpl1756872796998.png", record_pos=(0.455, 0.251), resolution=(1600, 900)))
            touch(Template(r"tpl1756872801285.png", record_pos=(0.16, 0.081), resolution=(1600, 900)))
        else:
            raise Exception(f"昵称修改失败,错误的昵称是:{change_name}")
        if exists(Template(r"tpl1756873650314.png", record_pos=(0.03, 0.068), resolution=(1600, 900))):
            touch(Template(r"tpl1756873650314.png", record_pos=(0.03, 0.068), resolution=(1600, 900)))
            sleep(2)
        else:
            raise Exception(f"签名修改失败,错误的签名是:{qianming}")
        if exists(Template(r"tpl1756873668066.png", record_pos=(0.414, 0.246), resolution=(1600, 900))):
            print("可以打开支援星痕界面")
            touch((219, 162))
            touch((262, 280))
            touch((231, 433))
            touch(Template(r"tpl1756873766837.png", record_pos=(0.412, 0.246), resolution=(1600, 900)))
        else:
            raise Exception("无法打开支援星痕")
        if exists(Template(r"tpl1756873854619.png", record_pos=(0.424, 0.053), resolution=(1600, 900))):
            print("支援星痕上阵成功")
            touch(Template(r"tpl1756880331039.png", record_pos=(-0.26, 0.223), resolution=(1600, 900)))
            sleep(5)
        else:
            raise Exception("返回界面错误")
        if exists(Template(r"tpl1756880386080.png", record_pos=(0.006, -0.004), resolution=(1600, 900))):
            print("进入收藏册界面")
            touch(Template(r"tpl1756880419884.png", record_pos=(-0.151, 0.087), resolution=(1600, 900)))
            touch(Template(r"tpl1756880431268.png", record_pos=(-0.458, -0.122), resolution=(1600, 900)))

            touch(Template(r"tpl1756880436039.png", record_pos=(-0.452, -0.056), resolution=(1600, 900)))
            touch(Template(r"tpl1756889661108.png", record_pos=(-0.463, -0.255), resolution=(1600, 900)))

        else:
            raise Exception("无法进入收藏册页面")
        if exists(Template(r"tpl1756873854619.png", record_pos=(0.424, 0.053), resolution=(1600, 900))):
            print("从收藏册页面正常返回")
            touch(Template(r"tpl1756880513938.png", record_pos=(-0.451, -0.261), resolution=(1600, 900)))
        else:
            raise Exception("无法从收藏册页面返回")
        if exists(Template(r"tpl1756880628095.png", record_pos=(0.401, -0.191), resolution=(1600, 900))):
            print("从个人主页进入主界面")
        else:
            raise Exception("从个人主页进入主界面")
        touch(Template(r"tpl1756880657900.png", record_pos=(-0.454, -0.172), resolution=(1600, 900)))
        if exists(Template(r"tpl1756880851065.png", record_pos=(-0.405, -0.208), resolution=(1600, 900))):
            print("进入邮箱")
            touch(Template(r"tpl1756880761950.png", record_pos=(-0.356, 0.201), resolution=(1600, 900)))
        else:
            raise Exception("无法进入邮箱")
        if exists(Template(r"tpl1756880908872.png", record_pos=(0.003, -0.118), resolution=(1600, 900))):
            print("邮箱领取奖励正常")
            touch(Template(r"tpl1756880923803.png", record_pos=(0.35, 0.198), resolution=(1600, 900)))
            touch(Template(r"tpl1756880960168.png", record_pos=(-0.451, 0.199), resolution=(1600, 900)))
        else:
            raise Exception("无法领取邮箱奖励")
        sleep(1)
        touch(Template(r"tpl1758272862398.png", record_pos=(0.117, 0.073), resolution=(3220, 1440)))
        if exists(Template(r"tpl1756881006397.png", record_pos=(-0.387, 0.004), resolution=(1600, 900))):
            print("删除邮件功能正常")
            touch(Template(r"tpl1756881083323.png", record_pos=(0.471, -0.219), resolution=(1600, 900)))
            print("关闭邮箱")
        else:
            raise Exception("删除邮箱失败")

        if exists(Template(r"tpl1756880628095.png", record_pos=(0.401, -0.191), resolution=(1600, 900))):
            print("从邮箱回到主界面")
        else:
            raise Exception("无法从邮箱回到主界面")
        touch(Template(r"tpl1756881174411.png", record_pos=(-0.401, -0.171), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1756881191929.png", record_pos=(0.319, -0.184), resolution=(1600, 900))):
            print("小闪百抽活动正常")
            touch(Template(r"tpl1756881222609.png", record_pos=(-0.214, 0.016), resolution=(1600, 900)))
            touch((951, 740))
        else:
            raise Exception("小闪活动无法进入")
        if exists(Template(r"tpl1756881335332.png", record_pos=(-0.214, 0.021), resolution=(1600, 900))):
            print("领取小闪活动奖励正常")
            touch(Template(r"tpl1756881367887.png", record_pos=(-0.406, -0.107), resolution=(1600, 900)))
            sleep(3)
            if exists(Template(r"tpl1756881421985.png", record_pos=(0.214, -0.146), resolution=(1600, 900))):
                print("小闪活动皮肤正常")
                touch(Template(r"tpl1756881476844.png", record_pos=(0.47, -0.015), resolution=(1600, 900)))
                sleep(2)
                if exists(Template(r"tpl1756881492839.png", record_pos=(0.443, 0.121), resolution=(1600, 900))):
                    print("小闪皮肤预览正常")
                else:
                    raise Exception("小闪皮肤预览错误")
            else:
                raise Exception("小闪活动皮肤异常")
        else:
            raise Exception("无法领取小闪奖励")
        touch(Template(r"tpl1756881844614.png", record_pos=(-0.448, -0.258), resolution=(1600, 900)))
        touch(Template(r"tpl1756881854300.png", record_pos=(-0.448, -0.254), resolution=(1600, 900)))
        if exists(Template(r"tpl1756880628095.png", record_pos=(0.401, -0.191), resolution=(1600, 900))):
            print("从小闪活动主界面")
        else:
            raise Exception("无法从小闪活动回到主界面")
        touch(Template(r"tpl1756881890769.png", record_pos=(-0.45, 0.007), resolution=(1600, 900)))
        if exists(Template(r"tpl1756881905824.png", record_pos=(-0.122, 0.251), resolution=(1600, 900))):
            print("正常进入仓库界面")
            touch(Template(r"tpl1756881990781.png", record_pos=(0.025, 0.255), resolution=(1600, 900)))
            touch(Template(r"tpl1756881993568.png", record_pos=(0.156, 0.251), resolution=(1600, 900)))
            touch(Template(r"tpl1756881996330.png", record_pos=(0.301, 0.255), resolution=(1600, 900)))
            touch(Template(r"tpl1756881999823.png", record_pos=(0.439, 0.254), resolution=(1600, 900)))
            touch(Template(r"tpl1756882036613.png", record_pos=(-0.126, 0.257), resolution=(1600, 900)))
            touch(Template(r"tpl1756882051051.png", record_pos=(-0.022, -0.024), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1756882060045.png", record_pos=(0.141, 0.126), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1756882430810.png", record_pos=(-0.096, -0.075), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1756882438894.png", record_pos=(0.154, 0.11), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception("无法进入仓库页面")
        if exists(Template(r"tpl1756882502421.png", record_pos=(-0.006, -0.121), resolution=(1600, 900))):
            print("初级体力药水使用正常")
            touch((1039, 645))

        else:
            raise Exception("无法使用初级体力药水")
        touch(Template(r"tpl1756882615016.png", record_pos=(0.121, -0.081), resolution=(1600, 900)))
        touch(Template(r"tpl1756882621384.png", record_pos=(0.153, 0.112), resolution=(1600, 900)))
        if exists(Template(r"tpl1756882502421.png", record_pos=(-0.006, -0.121), resolution=(1600, 900))):
            print("中级体力药水使用正常")
            touch((1039, 645))

        else:
            raise Exception("无法使用中级体力药水")
        touch(Template(r"tpl1756882680919.png", record_pos=(-0.196, -0.079), resolution=(1600, 900)))
        touch(Template(r"tpl1756882690246.png", record_pos=(0.161, 0.111), resolution=(1600, 900)))
        if exists(Template(r"tpl1756882502421.png", record_pos=(-0.006, -0.121), resolution=(1600, 900))):
            print("使用代币购买体力正常")
            touch((1039, 645))

        else:
            raise Exception("无法使用代币购买体力")
        touch(Template(r"tpl1756882832768.png", record_pos=(-0.159, 0.111), resolution=(1600, 900)))
        touch(Template(r"tpl1756882858913.png", record_pos=(-0.234, -0.142), resolution=(1600, 900)))
        touch(Template(r"tpl1756882865737.png", record_pos=(0.146, 0.117), resolution=(1600, 900)))
        touch(Template(r"tpl1756882872397.png", record_pos=(-0.015, -0.064), resolution=(1600, 900)))
        touch(Template(r"tpl1756882881021.png", record_pos=(0.11, 0.117), resolution=(1600, 900)))
        touch(Template(r"tpl1756882884367.png", record_pos=(0.191, 0.166), resolution=(1600, 900)))
        if exists(Template(r"tpl1756882502421.png", record_pos=(-0.006, -0.121), resolution=(1600, 900))):
            print("高级礼物自选道具使用正常")
            touch((1039, 645))

        else:
            raise Exception("无法使用高级礼物自选道具")
        touch(Template(r"tpl1756882936177.png", record_pos=(-0.461, -0.258), resolution=(1600, 900)))
        if exists(Template(r"tpl1756880628095.png", record_pos=(0.401, -0.191), resolution=(1600, 900))):
            print("从仓库回到主界面")
        else:
            raise Exception("无法回到主界面")
        touch(Template(r"tpl1756883066231.png", record_pos=(-0.431, 0.213), resolution=(1600, 900)))
        touch(Template(r"tpl1756883080857.png", record_pos=(0.166, 0.217), resolution=(1600, 900)))
        if exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(6)
        else:
            raise Exception("单抽缺少跳过按钮")
        if exists(Template(r"tpl1756951431929.png", record_pos=(-0.399, -0.179), resolution=(1600, 900))):
            sleep(2)
            touch((314, 268))
            sleep(1)
            touch((282, 168))
        else:
            touch((314, 268))
            sleep(1)
            touch((282, 168))
            print("人物已拥有")
        if exists(Template(r"tpl1756883254633.png", record_pos=(0.305, -0.136), resolution=(1600, 900))):
            print("新手卡池单抽正常")
        else:
            raise Exception("新手卡池单抽有问题")
        # 十连
        touch((1420, 808))
        while exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(0.5)
        # 关闭十连弹窗
        touch((1495, 438))
        sleep(1)
        # 关闭获得奖励弹窗
        touch((241, 201))
        sleep(4)
        # 关闭获得奖励弹窗
        touch((314, 268))
        if exists(Template(r"tpl1756883254633.png", record_pos=(0.305, -0.136), resolution=(1600, 900))):
            print("新手卡池十连抽正常")
        else:
            raise Exception("新手卡池十连抽抽有问题")
        # 切换限定卡池1
        touch((396, 818))
        sleep(1)
        if exists(Template(r"tpl1756890668627.png", record_pos=(-0.434, -0.2), resolution=(1600, 900))):
            print("切换卡池成功")
        else:
            raise Exception("缺少阵容推荐按钮")
        touch(Template(r"tpl1756883080857.png", record_pos=(0.166, 0.217), resolution=(1600, 900)))
        if exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(6)
        else:
            raise Exception("单抽缺少跳过按钮")
        if exists(Template(r"tpl1756951431929.png", threshold=0.9, record_pos=(-0.399, -0.179), resolution=(1600, 900))):
            sleep(2)
            touch((314, 268))
            sleep(1)
            touch((282, 168))
        else:
            touch((314, 268))
            sleep(1)
            touch((282, 168))
            print("人物已拥有")

        if exists(Template(r"tpl1756908635514.png", record_pos=(0.392, -0.012), resolution=(1600, 900))):
            print("限定卡池单抽正常")
        else:
            raise Exception("限定卡池单抽有问题")
        touch((1420, 808))
        while exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(0.5)

        touch((1495, 438))
        sleep(1)
        touch((241, 201))
        sleep(4)
        # 关闭获得奖励弹窗
        touch((314, 268))
        if exists(Template(r"tpl1756908635514.png", record_pos=(0.392, -0.012), resolution=(1600, 900))):
            print("限定卡池十连抽正常")
        else:
            raise Exception("限定卡池十连抽抽有问题")
        # 切换限定卡池2
        touch((625, 806))
        sleep(1)
        if exists(Template(r"tpl1756890668627.png", record_pos=(-0.434, -0.2), resolution=(1600, 900))):
            print("切换卡池成功")

            touch(Template(r"tpl1756883080857.png", record_pos=(0.166, 0.217), resolution=(1600, 900)))
        
        if exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(6)
        else:
            raise Exception("单抽缺少跳过按钮")
        if exists(Template(r"tpl1756951431929.png", threshold=0.9, record_pos=(-0.399, -0.179), resolution=(1600, 900))):
            sleep(2)
            touch((314, 268))
            sleep(1)
            touch((282, 168))
        else:
            touch((314, 268))
            sleep(1)
            touch((282, 168))
            print("人物已拥有")

        if exists(Template(r"tpl1756908635514.png", record_pos=(0.392, -0.012), resolution=(1600, 900))):
            print("限定卡池单抽正常")
        else:
            raise Exception("限定卡池单抽有问题")
        touch((1420, 808))
        while exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(0.5)
        touch((1495, 438))
        sleep(1)
        touch((241, 201))
        sleep(4)
        # 关闭获得奖励弹窗
        touch((314, 268))
        if exists(Template(r"tpl1756908635514.png", record_pos=(0.392, -0.012), resolution=(1600, 900))):
            print("限定卡池十连抽正常")
        else:
            raise Exception("限定卡池十连抽抽有问题")
    # 切换常规卡池1
        touch((816, 806))
        sleep(1)
        if exists(Template(r"tpl1756890668627.png", record_pos=(-0.434, -0.2), resolution=(1600, 900))):
            print("切换卡池成功")
        else:
            raise Exception("切换卡池失败")
        touch(Template(r"tpl1756883080857.png", record_pos=(0.166, 0.217), resolution=(1600, 900)))
        if exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(6)
        else:
            raise Exception("单抽缺少跳过按钮")
        if exists(Template(r"tpl1756951431929.png", threshold=0.9, record_pos=(-0.399, -0.179), resolution=(1600, 900))):
            sleep(2)
            touch((314, 268))
            sleep(1)
            touch((282, 168))
        else:
            touch((314, 268))
            sleep(1)
            touch((282, 168))
            print("人物已拥有")

        if exists(Template(r"tpl1756891106494.png", record_pos=(0.339, 0.003), resolution=(1600, 900))):
            print("常规卡池单抽正常")
        else:
            raise Exception("常规卡池单抽有问题")
        touch((1420, 808))
        while exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(0.5)

        touch((1495, 438))
        sleep(1)
        touch((241, 201))
        sleep(4)
        # 关闭获得奖励弹窗
        touch((314, 268))
        if exists(Template(r"tpl1756891106494.png", record_pos=(0.339, 0.003), resolution=(1600, 900))):
            print("常规卡池十连抽正常")
        else:
            raise Exception("常规卡池十连抽抽有问题")

        touch(Template(r"tpl1756891627240.png", record_pos=(-0.446, -0.257), resolution=(1600, 900)))
        if exists(Template(r"tpl1756880628095.png", record_pos=(0.401, -0.191), resolution=(1600, 900))):
            print("从招募回到主界面")
        else:
            raise Exception("无法从招募回到主界面")
        touch(Template(r"tpl1756891703102.png", record_pos=(-0.331, 0.212), resolution=(1600, 900)))
        sleep(1)
        print("进入魔女界面")
        touch(Template(r"tpl1756891749639.png", record_pos=(-0.459, -0.129), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756891753791.png", record_pos=(-0.456, -0.067), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756891759598.png", record_pos=(0.313, -0.176), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756891801490.png", record_pos=(0.071, -0.069), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756891833161.png", record_pos=(0.402, 0.238), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1756891867413.png", record_pos=(-0.36, -0.049), resolution=(1600, 900))):
            print("魔女升级成功")
            touch(Template(r"tpl1756891891928.png", record_pos=(-0.253, -0.254), resolution=(1600, 900)))
        else:
            raise Exception("魔女升级失败")
        if exists(Template(r"tpl1756891927610.png", record_pos=(0.048, -0.142), resolution=(1600, 900))):
            print("魔女技能界面顶部快捷入口正常拉起")
        else:
            raise Exception("魔女技能界面快捷入口失效")
        touch(Template(r"tpl1756891965009.png", record_pos=(-0.329, -0.155), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1756892093865.png", record_pos=(0.457, 0.199), resolution=(1600, 900))):
            print("顶部切换魔女按钮成功")
            touch(Template(r"tpl1756892212722.png", record_pos=(-0.261, -0.256), resolution=(1600, 900)))
            sleep(2)

        else:
            raise Exception("顶部按钮切换魔女失效")

        if exists(Template(r"tpl1756891927610.png", record_pos=(0.048, -0.142), resolution=(1600, 900))):
            print("魔女主界面顶部快捷入口正常拉起")
            touch(Template(r"tpl1756892243613.png", record_pos=(-0.233, -0.155), resolution=(1600, 900)))

        else:
            raise Exception("魔女主界面快捷入口失效")
        sleep(1)
        if exists(Template(r"tpl1756892314247.png", record_pos=(0.342, -0.243), resolution=(1600, 900))):
            print("切换星痕快捷键正常使用")
            touch((249, 193))
            sleep(1)
        else:
            raise Exception("顶部快捷入口无法切换星痕界面")
        if exists(Template(r"tpl1756892513301.png", record_pos=(0.448, 0.119), resolution=(1600, 900))):
            print("星痕界面正常进入")
            touch((259, 816))
            sleep(1)
            touch(Template(r"tpl1756892605439.png", record_pos=(0.453, 0.214), resolution=(1600, 900)))
            touch(Template(r"tpl1756892613661.png", record_pos=(0.312, 0.216), resolution=(1600, 900)))
            sleep(1)
            touch((293, 120))
        else:
            raise Exception("无法进入星痕界面")
        if exists(Template(r"tpl1756892707385.png", record_pos=(0.122, -0.176), resolution=(1600, 900))):
            print("升级成功")
        else:
            raise Exception("无法升级")
        touch(Template(r"tpl1757304054670.png", record_pos=(-0.456, -0.261), resolution=(1600, 900)))
        touch(Template(r"tpl1757304102862.png", record_pos=(-0.219, 0.232), resolution=(1600, 900)))
        while exists(Template(r"tpl1757304137809.png", threshold=0.8, rgb=True, record_pos=(0.348, 0.211),
                              resolution=(1600, 900))):
            print("该星痕可觉醒")
            touch(Template(r"tpl1757304115890.png", record_pos=(0.346, 0.212), resolution=(1600, 900)))
            sleep(0.5)
        touch(Template(r"tpl1757304380431.png", record_pos=(-0.446, -0.258), resolution=(1600, 900)))
        touch(Template(r"tpl1757304453403.png", record_pos=(-0.074, 0.231), resolution=(1600, 900)))
        if exists(Template(r"tpl1757304494385.png", record_pos=(0.343, 0.212), resolution=(1600, 900))):
            print("该星痕可突破")
            touch(Template(r"tpl1757304494385.png", record_pos=(0.343, 0.212), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1757304521134.png", record_pos=(0.193, 0.163), resolution=(1600, 900)))
        else:
            print("该星痕无法突破")
            pass
        touch(Template(r"tpl1757304586818.png", record_pos=(-0.457, -0.258), resolution=(1600, 900)))
        touch(Template(r"tpl1757304632803.png", record_pos=(0.034, 0.199), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757304658271.png", record_pos=(0.429, -0.151), resolution=(1600, 900))):
            print("主线关卡未达到")
            touch(Template(r"tpl1757304658271.png", record_pos=(0.429, -0.151), resolution=(1600, 900)))
        else:
            raise Exception("技能功能被提前解锁")
        touch(Template(r"tpl1757304766863.png", record_pos=(-0.452, -0.258), resolution=(1600, 900)))
        touch(Template(r"tpl1757304784624.png", record_pos=(0.367, 0.227), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757304847938.png", rgb=True, record_pos=(-0.409, -0.178), resolution=(1600, 900))):
            print("正常进入信物界面")
            touch(Template(r"tpl1757304807787.png", record_pos=(-0.403, -0.106), resolution=(1600, 900)))
            touch(Template(r"tpl1757304811023.png", record_pos=(-0.399, -0.026), resolution=(1600, 900)))
            touch(Template(r"tpl1757304813883.png", record_pos=(-0.407, 0.038), resolution=(1600, 900)))
        else:
            raise Exception("无法进入信物界面，或者定位页签错误")
        touch(Template(r"tpl1757304957431.png", record_pos=(-0.449, -0.258), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757304969784.png", record_pos=(0.04, -0.257), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1757326915202.png", record_pos=(0.034, -0.257), resolution=(1600, 900))):
            print("收藏功能正常")
        else:
            raise Exception("星痕收藏功能异常")
        touch(Template(r"tpl1757305084904.png", record_pos=(0.119, -0.256), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757305113539.png", record_pos=(-0.001, -0.244), resolution=(1600, 900))):
            print("星痕重置界面正常打开")
            touch(Template(r"tpl1757305191625.png", record_pos=(0.007, 0.237), resolution=(1600, 900)))
            sleep(2)
        else:
            raise Exception("星痕重置界面有问题")
        if exists(Template(r"tpl1757305261394.png", record_pos=(0.007, 0.007), resolution=(1600, 900))):
            print("星痕重置弹窗正常打开")
            touch(Template(r"tpl1757305279764.png", record_pos=(0.154, 0.171), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception("星痕重置弹窗有问题")
        if exists(Template(r"tpl1757305599281.png", record_pos=(0.009, -0.122), resolution=(1600, 900))):
            print("星痕重置功能正常")
            touch((354, 197))
            sleep(1)
        else:
            raise Exception("星痕无法被正常重置")

        touch(Template(r"tpl1757305750713.png", record_pos=(0.113, -0.261), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757305841970.png", record_pos=(0.04, -0.253), resolution=(1600, 900))):
            print("未培养星痕无法重置tosta正常")
        else:
            raise Exception("未培养星痕无法重置toste异常")
        touch(Template(r"tpl1757312320545.png", record_pos=(0.217, -0.258), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1757312336913.png", record_pos=(-0.328, -0.217), resolution=(1600, 900))):
            print("皮肤界面正常打开")
        else:
            raise Exception("皮肤界面有问题")
        touch(Template(r"tpl1757312443163.png", record_pos=(-0.323, -0.217), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757312465480.png", threshold=0.5, record_pos=(0.453, 0.118), resolution=(1600, 900))):
            print("切换2d皮肤成功")
        else:
            raise Exception("2d皮肤丢失")
        touch(Template(r"tpl1757312557989.png", record_pos=(-0.253, -0.219), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757312573972.png", threshold=0.5, record_pos=(0.449, 0.123), resolution=(1600, 900))):
            print("切换3d皮肤成功")
        else:
            pass
        touch(Template(r"tpl1757312829471.png", record_pos=(-0.455, -0.257), resolution=(1600, 900)))
        touch(Template(r"tpl1757312856501.png", record_pos=(0.336, -0.257), resolution=(1600, 900)))
        if exists(Template(r"tpl1757312867369.png", record_pos=(0.416, 0.021), resolution=(1600, 900))):
            print("切换展示功能成功")
            touch(Template(r"tpl1757312867369.png", record_pos=(0.416, 0.021), resolution=(1600, 900)))
        else:
            raise Exception("切换皮肤功能失效")
        touch(Template(r"tpl1757313013956.png", record_pos=(0.431, -0.253), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757313032864.png", record_pos=(0.211, 0.254), resolution=(1600, 900))):
            print("切换档案成功")
            touch(Template(r"tpl1757313056248.png", record_pos=(0.409, 0.253), resolution=(1600, 900)))
        else:
            raise Exception("无法查看档案")
        if exists(Template(r"tpl1757313102120.png", record_pos=(0.406, -0.228), resolution=(1600, 900))):
            print("切换语音成功")
            touch(Template(r"tpl1757313128061.png", record_pos=(-0.455, -0.261), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception("无法打开语音界面")
        touch(Template(r"tpl1757313210870.png", record_pos=(-0.159, -0.258), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1757313225122.png", record_pos=(-0.095, -0.084), resolution=(1600, 900))):
            print("星痕帮助按钮正常打开")
            touch((370, 219))
            exists(Template(r"tpl1757313262451.png", record_pos=(-0.092, -0.087), resolution=(1600, 900)))
            touch((370, 219))
            exists(Template(r"tpl1757313284182.png", record_pos=(0.042, -0.004), resolution=(1600, 900)))
            touch((370, 219))
            exists(Template(r"tpl1757313328526.png", record_pos=(-0.207, 0.096), resolution=(1600, 900)))
            touch((370, 219))
            exists(Template(r"tpl1757313338759.png", record_pos=(0.021, 0.095), resolution=(1600, 900)))
            touch((370, 219))
            exists(Template(r"tpl1757313343524.png", record_pos=(-0.058, 0.089), resolution=(1600, 900)))
            touch((370, 219))
            exists(Template(r"tpl1757313348353.png", record_pos=(-0.307, 0.093), resolution=(1600, 900)))
            touch((370, 219))
            exists(Template(r"tpl1757313352216.png", record_pos=(-0.101, 0.087), resolution=(1600, 900)))
            touch((370, 219))
            exists(Template(r"tpl1757313357520.png", record_pos=(0.09, -0.039), resolution=(1600, 900)))
            touch((370, 219))
        else:
            raise Exception("星痕界面帮助引导丢失")
        touch(Template(r"tpl1757313550427.png", record_pos=(-0.461, -0.259), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757313558323.png", record_pos=(-0.455, -0.254), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757398919484.png", record_pos=(-0.449, -0.259), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757313567976.png", record_pos=(-0.1, 0.212), resolution=(1600, 900)))
        if exists(Template(r"tpl1757313589050.png", record_pos=(-0.085, -0.168), resolution=(1600, 900))):
            print("正常打开专武卡池")
            touch(Template(r"tpl1757313610395.png", record_pos=(0.177, 0.224), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1757313621390.png", record_pos=(-0.053, 0.176), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1757313694161.png", record_pos=(0.136, 0.106), resolution=(1600, 900)))
            while exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
                touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
                sleep(0.5)
        if exists(Template(r"tpl1756951431929.png", record_pos=(-0.399, -0.179), resolution=(1600, 900))):
            sleep(2)
            touch((314, 268))
            sleep(2)
            touch((282, 168))
        else:
            touch((314, 268))
            sleep(2)
            touch((282, 168))
            print("武器已拥有")
        if exists(Template(r"tpl1757314684741.png", record_pos=(-0.077, -0.165), resolution=(1600, 900))):
                print("换物卡池单抽正常")
        else:
            raise Exception("换物卡池单抽有问题")
        touch((1420, 808))
        while exists(Template(r"tpl1756890236926.png", record_pos=(0.431, -0.247), resolution=(1600, 900))):
            touch(Template(r"tpl1756890277892.png", record_pos=(0.434, -0.247), resolution=(1600, 900)))
            sleep(0.5)

        touch((1495, 438))
        sleep(1)
        touch((241, 201))
        sleep(4)
        # 关闭获得奖励弹窗
        touch((314, 268))
        if exists(Template(r"tpl1757314684741.png", record_pos=(-0.077, -0.165), resolution=(1600, 900))):
            print("换物卡池十连抽抽正常")
        else:
            raise Exception("换物卡池十连抽有问题")
        touch(Template(r"tpl1757314778044.png", record_pos=(-0.096, -0.258), resolution=(1600, 900)))
        if exists(Template(r"tpl1757314788444.png", record_pos=(-0.319, -0.128), resolution=(1600, 900))):
            print("历史记录页面正常打开")
            touch(Template(r"tpl1757314845355.png", record_pos=(0.405, -0.203), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception("唤物历史记录打开失败")

        touch(Template(r"tpl1757314863221.png", record_pos=(0.461, 0.025), resolution=(1600, 900)))
        if exists(Template(r"tpl1757315237605.png", record_pos=(-0.308, -0.065), resolution=(1600, 900))):
            print("正常打开")
        else:
            raise Exception("专武召唤详情无法打开")
        touch(Template(r"tpl1757315298500.png", record_pos=(-0.467, -0.182), resolution=(1600, 900)))
        touch(Template(r"tpl1757315490742.png", record_pos=(0.455, 0.108), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1757315504559.png", record_pos=(0.108, 0.26), resolution=(1600, 900))):
            print("跳转正常")
        else:
            raise Exception("专武卡池无法跳转到商店")
        touch(Template(r"tpl1757314752127.png", record_pos=(-0.456, -0.259), resolution=(1600, 900)))
        touch(Template(r"tpl1757314752127.png", record_pos=(-0.456, -0.259), resolution=(1600, 900)))
        if exists(Template(r"tpl1757315616816.png", record_pos=(0.376, -0.197), resolution=(1600, 900))):
            print("跳转正常")
        else:
            raise Exception("无法从专武卡池回到主界面")
        touch(Template(r"tpl1757315679809.png", record_pos=(0.247, 0.207), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1757315504559.png", record_pos=(0.108, 0.26), resolution=(1600, 900))):
            print("跳转正常")
        else:
            raise Exception("主界面无法跳转到商店")
        if exists(Template(r"tpl1757316541857.png", record_pos=(-0.387, -0.213), resolution=(1600, 900))):
            print("默认进入商店是推荐商店")
        else:
            raise Exception("商店默认页面有问题")
        touch(Template(r"tpl1757316612714.png", record_pos=(0.196, 0.164), resolution=(1600, 900)))
        if exists(Template(r"tpl1757316625168.png", record_pos=(-0.406, -0.211), resolution=(1600, 900))):
            print("推荐商店页面跳转正常")
        else:
            raise Exception("推荐商店页面跳转有问题")
        touch(Template(r"tpl1757317861516.png", record_pos=(-0.055, 0.259), resolution=(1600, 900)))
        if exists(Template(r"tpl1757317873525.png", record_pos=(-0.369, -0.212), resolution=(1600, 900))):
            print("结晶商店正常开启")
        else:
            raise Exception("结晶商店无法跳转")
        touch(Template(r"tpl1757317946801.png", record_pos=(0.092, 0.254), resolution=(1600, 900)))
        if exists(Template(r"tpl1757316625168.png", record_pos=(-0.406, -0.211), resolution=(1600, 900))):
            print("礼包商店页面跳转正常")
        else:
            raise Exception("推荐商店页面跳转有问题")
        touch(Template(r"tpl1757318351768.png", record_pos=(-0.4, -0.094), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757319521471.png", record_pos=(-0.234, -0.084), resolution=(1600, 900))):

            print("荒野行商界面正常打开")
        else:
            raise Exception("荒野行商界面跳转有问题")
        touch(Template(r"tpl1757318359409.png", record_pos=(-0.406, -0.028), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757319429262.png", record_pos=(-0.052, -0.01), resolution=(1600, 900))):
            print("星海秘宝界面正常打开")
        else:
            raise Exception("星海秘宝界面无法打开")
        touch(Template(r"tpl1757318369402.png", record_pos=(-0.393, 0.036), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757318611017.png", record_pos=(0.357, 0.167), resolution=(1600, 900))):
            print("月卡界面正常打开")
        else:
            raise Exception("无法打开月卡购买界面")
        touch(Template(r"tpl1757318374225.png", record_pos=(-0.404, 0.101), resolution=(1600, 900)))
        if exists(Template(r"tpl1757318517252.png", record_pos=(-0.234, 0.108), resolution=(1600, 900))):
            print("等级礼包跳转正常")
        else:
            raise Exception("等级礼包页面跳转失败")
        touch(Template(r"tpl1757319600832.png", threshold=0.8, record_pos=(0.258, 0.261), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1757320095297.png", threshold=0.7, record_pos=(0.029, 0.011), resolution=(1600, 900))):
            print("热卖装扮正常打开")
        else:
            raise Exception('装扮商店缺少页签')
        touch(Template(r"tpl1757320198480.png", record_pos=(-0.404, -0.094), resolution=(1600, 900)))
        if exists(Template(r"tpl1757320231742.png", record_pos=(0.36, -0.256), resolution=(1600, 900))):
            print("梦幻装扮商店正常打开")
        else:
            raise Exception("梦幻装扮商店无法打开")
        touch(Template(r"tpl1757320478816.png", record_pos=(-0.414, -0.026), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757320489770.png", record_pos=(-0.397, 0.037), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757320495778.png", record_pos=(-0.404, 0.104), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757320499136.png", record_pos=(-0.402, 0.169), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757320530048.png", record_pos=(0.412, 0.256), resolution=(1600, 900)))
        sleep(1)
        if exists(
                Template(r"tpl1757320550111.png", threshold=0.9, rgb=True, record_pos=(-0.409, 0.003), resolution=(1600, 900))):
            print("兑换商店全部存在")
        else:
            raise Exception("兑换商店缺少页签")
        touch(Template(r"tpl1757320630124.png", record_pos=(-0.453, -0.258), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757572441910.png", record_pos=(0.372, 0.174), resolution=(1600, 900)))
        touch(Template(r"tpl1757572452345.png", record_pos=(-0.122, 0.253), resolution=(1600, 900)))
        touch(Template(r"tpl1757572461549.png", record_pos=(0.119, -0.007), resolution=(1600, 900)))
        touch(Template(r"tpl1757572468050.png", record_pos=(-0.217, -0.077), resolution=(1600, 900)))
        touch(Template(r"tpl1757572476615.png", record_pos=(0.117, 0.241), resolution=(1600, 900)))
        touch(Template(r"tpl1757572487840.png", record_pos=(0.386, 0.151), resolution=(1600, 900)))
        while exists(Template(r"tpl1757572856450.png", record_pos=(0.249, 0.137), resolution=(1600, 900))):
            touch(Template(r"tpl1757572527672.png", record_pos=(0.275, 0.239), resolution=(1600, 900)))
            if exists(Template(r"tpl1757573477922.png", record_pos=(0.001, -0.164), resolution=(1600, 900))):
                touch(Template(r"tpl1757574121399.png", record_pos=(0.117, -0.082), resolution=(1600, 900)))
                touch(Template(r"tpl1757574133924.png", record_pos=(0.117, 0.041), resolution=(1600, 900)))
                touch(Template(r"tpl1757574139915.png", record_pos=(0.154, 0.113), resolution=(1600, 900)))
                sleep(2)
                touch((267,166))
                touch(Template(r"tpl1757574192097.png", record_pos=(-0.155, 0.111), resolution=(1600, 900)))
                touch((244,467))
                touch(Template(r"tpl1757573751797.png", record_pos=(-0.265, -0.259), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573775958.png", record_pos=(-0.326, -0.152), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573781926.png", record_pos=(0.309, -0.18), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573795763.png", record_pos=(0.042, -0.029), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573803214.png", record_pos=(0.359, 0.071), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573813851.png", record_pos=(0.397, 0.233), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573820662.png", record_pos=(0.106, 0.046), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573826111.png", record_pos=(0.158, 0.131), resolution=(1600, 900)))
                sleep(1)
                touch(Template(r"tpl1757573884136.png", record_pos=(-0.37, -0.264), resolution=(1600, 900)))
                sleep(1)
            else:
                if exists(Template(r"tpl1757572711090.png", record_pos=(0.0, -0.115), resolution=(1600, 900))):
                    touch((362,174))
                    touch(Template(r"tpl1757572690884.png", record_pos=(0.003, 0.218), resolution=(1600, 900)))
                    if exists(Template(r"tpl1757573137934.png", record_pos=(0.007, -0.054), resolution=(1600, 900))):
                        touch(Template(r"tpl1757572698106.png", record_pos=(-0.004, 0.134), resolution=(1600, 900)))
                    else:
                        pass
                else:
                    touch(Template(r"tpl1757572690884.png", record_pos=(0.003, 0.218), resolution=(1600, 900)))
                    sleep(2)
                    if exists(Template(r"tpl1757573137934.png", record_pos=(0.007, -0.054), resolution=(1600, 900))):
                        touch(Template(r"tpl1757572698106.png", record_pos=(-0.004, 0.134), resolution=(1600, 900)))
                    else:
                        pass
                    touch((362,174))
        sleep(1)
        touch(Template(r"tpl1757575902332.png", record_pos=(0.349, -0.193), resolution=(1600, 900)))
        touch(Template(r"tpl1757574258730.png", record_pos=(0.416, -0.089), resolution=(1600, 900)))
        touch(Template(r"tpl1757574266746.png", record_pos=(0.22, -0.045), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757574288683.png", record_pos=(-0.092, -0.096), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757574304300.png", record_pos=(-0.129, -0.116), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757574311377.png", record_pos=(0.409, 0.247), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1757574335386.png", record_pos=(0.399, 0.245), resolution=(1600, 900)))
        sleep(8)
        if exists(Template(r"tpl1757574358922.png", record_pos=(0.448, -0.255), resolution=(1600, 900))):
            touch(Template(r"tpl1757574358922.png", record_pos=(0.448, -0.255), resolution=(1600, 900)),times=3)
            sleep(2)
            touch(Template(r"tpl1757574398863.png", record_pos=(-0.076, 0.064), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1757574412403.png", record_pos=(0.284, 0.117), resolution=(1600, 900)))
        else:
            print("没有引导")
        wait(Template(r"tpl1757574551409.png", record_pos=(0.231, -0.201), resolution=(1600, 900)),timeout=60)
        sleep(2)
        touch(Template(r"tpl1757574603173.png", record_pos=(-0.156, 0.227), resolution=(1600, 900)))
        sleep(2)
        cross_stage()
        if exists(Template(r"tpl1757575462513.png", record_pos=(0.001, -0.074), resolution=(1600, 900))):
            print("已达成第1-17章，解锁任务关卡")
            touch((615,711))
            sleep(1)
        else:
            raise Exception("无法正常解锁第1-17章节，任务功能")
        if exists(Template(r"tpl1757575662898.png", record_pos=(0.008, -0.088), resolution=(1600, 900))):
            print("已达成第1-17章，解锁星痕记忆")
            touch((615,711))
            sleep(1)
        else:
            raise Exception("无法正常解锁第1-17章节，星痕记忆功能")
        touch(Template(r"tpl1757576893663.png", record_pos=(-0.431, 0.225), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1757576910538.png", record_pos=(-0.371, -0.134), resolution=(1600, 900))):
            print("任务引导正常弹出")
            touch(Template(r"tpl1757576945295.png", record_pos=(-0.456, -0.174), resolution=(1600, 900)))
            if exists(Template(r"tpl1757576910538.png", record_pos=(-0.371, -0.134), resolution=(1600, 900))):
                print("任务引导2正常")
                touch(Template(r"tpl1757577058179.png", record_pos=(-0.285, 0.196), resolution=(1600, 900)))
                if exists(Template(r"tpl1757576910538.png", record_pos=(-0.371, -0.134), resolution=(1600, 900))):
                    print("任务引导3正常")
                    touch(Template(r"tpl1757577084325.png", record_pos=(-0.338, -0.165), resolution=(1600, 900)))
                    if exists(Template(r"tpl1757576910538.png", record_pos=(-0.371, -0.134), resolution=(1600, 900))):
                        print("任务引导4正常")
                        touch(Template(r"tpl1757577109564.png", record_pos=(0.413, 0.182), resolution=(1600, 900)))
                        sleep(4)
                        if exists(Template(r"tpl1757577124925.png", record_pos=(-0.003, -0.116), resolution=(1600, 900))):
                            touch((333,162))
                            if exists(Template(r"tpl1757576910538.png", record_pos=(-0.371, -0.134), resolution=(1600, 900))):
                                print("任务引导5正常")
                                touch(Template(r"tpl1757577186117.png", record_pos=(0.417, 0.051), resolution=(1600, 900)))
                                sleep(2)
                                if exists(Template(r"tpl1757577124925.png", record_pos=(-0.003, -0.116), resolution=(1600, 900))):
                                    touch((333,162))
                                else:
                                    raise Exception("一键挑战引导奖励弹窗丢失")
                            else:
                                raise Exception("一键挑战引导引导丢失")
                        else:
                            raise Exception("进行一次攻击奖励弹窗丢失")
                    else:
                        raise Exception("进行一次攻击引导丢失")
                else:
                    raise Exception("战斗力引导丢失")
            else:
                raise Exception("任务说明引导丢失")
        else:
            raise Exception("任务引导缺失")
        touch(Template(r"tpl1757577598056.png", record_pos=(-0.458, -0.255), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757577864434.png", record_pos=(0.359, -0.191), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757577872247.png", record_pos=(0.416, -0.088), resolution=(1600, 900)))
        sleep(1)
        cross_stage()
        if not exists(Template(r"tpl1757578301817.png", record_pos=(0.039, -0.086), resolution=(1600, 900))):
            raise Exception("勋章弹窗丢失")
        touch((164,399))
        sleep(1)
        if not exists(Template(r"tpl1757578411808.png", record_pos=(0.004, -0.099), resolution=(1600, 900))):
            raise Exception("困难模式弹窗丢失")
        touch((164,399))
        if not exists(Template(r"tpl1757578485311.png", record_pos=(0.02, -0.095), resolution=(1600, 900))):
            raise Exception("神谕司弹窗丢失")
        touch((164,399))
        touch(Template(r"tpl1757578568492.png", record_pos=(-0.429, 0.226), resolution=(1600, 900)))
        sleep(2)
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
            raise Exception("神谕司引导丢失")
        touch(Template(r"tpl1757578616227.png", record_pos=(0.116, 0.212), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
            raise Exception("神谕司委任引导丢失")
        touch(Template(r"tpl1757578641315.png", record_pos=(-0.412, -0.058), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
            raise Exception("神谕司一键委任引导丢失")

        touch(Template(r"tpl1757578674492.png", record_pos=(0.374, 0.241), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
            raise Exception("神谕司委任奖励引导丢失")
        touch(Template(r"tpl1757578835697.png", record_pos=(-0.092, 0.179), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
            raise Exception("神谕司结束引导丢失")
        touch(Template(r"tpl1757578849869.png", record_pos=(-0.361, -0.256), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1757578871628.png", record_pos=(-0.362, 0.002), resolution=(1600, 900)))

        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章引导丢失")
        touch(Template(r"tpl1757578922324.png", record_pos=(-0.2, 0.016), resolution=(1600, 900)))

        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章奖励获取引导丢失")
        touch(Template(r"tpl1757578939749.png", record_pos=(-0.086, -0.172), resolution=(1600, 900)))
        sleep(1)
        touch((620,102))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章统计引导丢失")
                
        touch(Template(r"tpl1757579005252.png", record_pos=(-0.212, 0.253), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章统计界面引导丢失")
        touch((1185,207))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章结束引导丢失")
        touch(Template(r"tpl1757579109735.png", record_pos=(-0.366, -0.256), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("玩家档案引导丢失")
        touch(Template(r"tpl1757579134591.png", record_pos=(-0.438, -0.239), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章槽引导丢失")
        touch(Template(r"tpl1757579161229.png", record_pos=(-0.092, 0.159), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("首次激活勋章引导丢失")
        touch(Template(r"tpl1757579201551.png", record_pos=(-0.437, -0.172), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章保存设定引导丢失")
        touch(Template(r"tpl1757579538924.png", record_pos=(-0.359, 0.164), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
             raise Exception("勋章墙结束引导丢失")
        touch(Template(r"tpl1757579575054.png", record_pos=(-0.453, -0.259), resolution=(1600, 900)))
        if not exists(Template(r"tpl1757578590222.png", record_pos=(-0.346, 0.117), resolution=(1600, 900))):
            raise Exception("勋章保存设定引导丢失")
        touch(Template(r"tpl1757579605481.png", record_pos=(-0.451, -0.259), resolution=(1600, 900)))
        touch(Template(r"tpl1757579605481.png", record_pos=(-0.451, -0.259), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1761289339050.png", record_pos=(0.378, 0.182), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1761289351840.png", record_pos=(0.147, -0.014), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1761289368965.png", record_pos=(0.421, -0.083), resolution=(1600, 900)))
        sleep(1)
        cross_stage_new()
        if not exists(Template(r"tpl1761208353291.png", record_pos=(0.009, -0.1), resolution=(1600, 900))):
            raise Exception("公会弹窗丢失")
        touch((164,399))
        touch(Template(r"tpl1761208457080.png", record_pos=(-0.307, 0.224), resolution=(1600, 900)))
        touch(Template(r"tpl1761208669654.png", record_pos=(-0.369, -0.258), resolution=(1600, 900)))
    except Exception as e:
        erro_pass()
        raise
if __name__ == '__main__':
    script_path = __file__
    script_name, _ = os.path.splitext(os.path.basename(__file__))
    for i in range(1):
        start_time = time.time()
        serialno = "127.0.0.1:16512"
        # ✅ 2. 连接设备并执行一些操作（确保生成日志）
        dev = ADB(serialno="127.0.0.1:16512")
        model = subprocess.check_output(["adb", "-s", serialno, "shell", "getprop", "ro.product.model"]).decode(
            "utf-8").strip()
        brand = subprocess.check_output(["adb", "-s", serialno, "shell", "getprop", "ro.product.brand"]).decode(
            "utf-8").strip()
        phone = f"{brand}-{model} "
        file = script_name
        result = "SUCCESS"
        from pathlib import Path

        # 指定目录路径
        directory = Path(r"H:\Millennium Journey_Automation\ch_smoke.air\log")

        # 遍历目录中所有 .png 文件（不包括子目录）
        for png_file in directory.glob("*.jpg"):
            if png_file.is_file():  # 确保是文件
                png_file.unlink()  # 删除文件
                print(f"已删除: {png_file}")
        Recorder(dev).start_recording(max_time=6000)
        try:
            maoyan()
        except Exception as e:
            print(f"脚本执行异常: {e}")
            erro_message = traceback.format_exc()
            print(erro_message)
            result = "FAIL"
        finally:
            Recorder(dev).stop_recording(output="test.mp4")
            LogToHtml(__file__,
                      export_dir=r"H:\Millennium Journey_Automation\ch_smoke.air",
                      lang="zh",
                      ).report(output_file=r"test.html")
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            video_html = f'''
            <div style="
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 400px;
                height: 225px;
                background: #000;
                z-index: 9999;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            ">
              <video id="myVideo" width="100%" height="100%" 
                     controls 
                     preload="metadata" 
                     style="object-fit: cover; background:#000;">
                <source src="test.mp4" type="video/mp4">
                您的浏览器不支持视频播放。
              </video>
            </div>
            '''

            # 插入到 <body> 之后
            content = content.replace('<body>', '<body>\n' + video_html)

            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已将录屏嵌入报告: {html_file}")
            duration = time.time() - start_time
            report_html = r"http://192.168.30.148:8000/ch_smoke.air/ch_smoke.log/test.html"
            print(f"脚本执行完成，耗时: {duration:.2f}秒")
        if result == "SUCCESS":
            sender.send_markdown_message(
                f"**执行结果**: <font color='info'>{result}</font>\n"
                f"**设备名称**: {phone}\n"
                f"**用户昵称**: {change_name}\n"
                f"**脚本文件**: {file}\n"
                f"**耗时**: {duration:.2f}秒\n"
                f"**报告地址**:[{report_html}]({report_html})"

            )
        else:
            sender.send_markdown_message(
                f"**执行结果**: <font color='warning'>{result}</font>\n"
                f"**设备名称**: {phone}\n"
                f"**用户昵称**: {change_name}\n"
                f"**脚本文件**: {file}\n"
                f"**耗时**: {duration:.2f}秒\n"
                f"**报告地址**:[{report_html}]({report_html})\n"
                f"**错误信息**: \n```\n{erro_message}\n```"
            )







