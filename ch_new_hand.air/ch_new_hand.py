# -*- encoding=utf8 -*-
__author__ = "王瀚鋆"
__title__ = "千年之旅UI自动化"
__desc__ = """
正式服新手引导
"""

from datetime import datetime
from pathlib import Path

from airtest.core.api import *
from airtest.core.android.recorder import *
from airtest.core.android.adb import *
from airtest.report.report import simple_report, LogToHtml
import traceback

from server_qywx import sendmessage

auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:16512"])
sender = sendmessage(key="22a6a656-0fea-4ff4-b697-2fdd08729d49")
timestamp = datetime.now().strftime("%Y%m%d%H%M")
root = timestamp
export_dir = r"H:\Millennium Journey_Automation\ch_new_hand.air\ch_new_hand.log"
html_file = os.path.join(export_dir, "test.html")


def auto_tap_continue(max_taps=1000, interval=1):
    BTN_CONTINUE = Template(r"tpl1754535194424.png", record_pos=(0.344, 0.253), resolution=(1600, 900))
    for i in range(max_taps):
        try:
            # 尝试查找图标
            pos = wait(BTN_CONTINUE, timeout=30)  # 设置较短的timeout值

            # 如果找到了图标，则点击
            touch(pos)
            print(f"第 {i + 1} 次点击: 成功找到并点击图标")
            # 等待一段时间后继续下一次循环
            sleep(interval)
        except TargetNotFoundError:
            # 如果没有找到图标，说明可能已经到达了需要用户操作的新界面或者剧情已经推进到不需要再点击此图标的步骤
            print("图标未找到，可能是剧情已经推进或者进入新界面。停止点击。")
            break


def connect_emulator(host="127.0.0.1", port="16512"):
    # 方法1：用 subprocess
    subprocess.run(f"adb connect {host}:{port}", shell=True)
    # 等待连接
    time.sleep(2)

    # 连接 Airtest 设备
    dev = connect_device(f"Android://{host}:{port}")
    return dev


def erro_pass():
    cmd = [
        "am", "force-stop", "com.yingche.qnzl"
    ]
    dev.shell(cmd)

def open_app():
    cmd = [
        "am", "start", "-S",
        "-n", "com.yingche.qnzl/com.inchigame.elf.sdk.SplashActivity"
    ]
    dev.shell(cmd)

def main_process():
    try:
        sleep(20)
        if exists(Template(r"tpl1757055392792.png", record_pos=(0.001, 0.144), resolution=(1600, 900))):
            touch((1382, 734))
            print("拉到热更资源")
        else:
            pass
        if exists(Template(r"tpl1758770504264.png", record_pos=(0.471, -0.217), resolution=(1600, 900))):
            touch(Template(r"tpl1758770504264.png", record_pos=(0.471, -0.217), resolution=(1600, 900)))
        else:
            pass
        touch(Template(r"tpl1756693147581.png", record_pos=(0.464, 0.0), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756693158632.png", record_pos=(0.23, 0.079), resolution=(1600, 900)))
        touch(wait(Template(r"tpl1754548084036.png", record_pos=(0.093, 0.145), resolution=(1600, 900)), timeout=60))
        sleep(2)
        touch(Template(r"tpl1756695747373.png", record_pos=(0.126, -0.06), resolution=(1600, 900)))
        if exists(Template(r"tpl1756886266039.png", record_pos=(0.124, -0.062), resolution=(1600, 900))):
            touch(Template(r"tpl1756695747373.png", record_pos=(0.126, -0.06), resolution=(1600, 900)))
        else:
            pass
        touch((748, 422))
        sleep(1)
        touch(Template(r"tpl1757039151646.png", record_pos=(-0.082, 0.0), resolution=(1600, 900)))
        sleep(1)
        if not exists(Template(r"tpl1757039160211.png", record_pos=(-0.029, -0.059), resolution=(1600, 900))):
            raise Exception("删除旧帐号失败")
        touch(Template(r"tpl1757039160211.png", record_pos=(-0.029, -0.059), resolution=(1600, 900)))
        keyevent("112")
        text(f"{root}")
        touch(Template(r"tpl1756434533904.png", record_pos=(0.066, 0.062), resolution=(2480, 1148)))
        touch(wait(Template(r"tpl1756693258397.png", record_pos=(0.456, -0.252), resolution=(1600, 900)),timeout=60))
        touch(wait(Template(r"tpl1756693301248.png", record_pos=(0.332, 0.118), resolution=(1600, 900))))
        auto_tap_continue(max_taps=1000, interval=1)
        touch(Template(r"tpl1754535820833.png", record_pos=(-0.431, 0.096), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1758781835897.png", record_pos=(-0.432, 0.09), resolution=(1600, 900)))
        auto_tap_continue(max_taps=1000, interval=1)
        touch(Template(r"tpl1754535873015.png", record_pos=(0.329, 0.217), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754535883215.png", record_pos=(0.444, -0.103), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754535890583.png", record_pos=(0.446, -0.093), resolution=(1600, 900)))
        sleep(10)
        auto_tap_continue(max_taps=1000, interval=1)
        touch(Template(r"tpl1754535905337.png", record_pos=(-0.16, -0.069), resolution=(1600, 900)))
        sleep(2)
        auto_tap_continue(max_taps=1000, interval=1)
        sleep(2)
        touch(Template(r"tpl1754536125316.png", record_pos=(0.329, 0.217), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754536130684.png", record_pos=(-0.441, 0.2), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754536136314.png", record_pos=(0.446, -0.099), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754536140186.png", record_pos=(0.445, -0.093), resolution=(1600, 900)))
        sleep(30)
        auto_tap_continue(max_taps=1000, interval=1)
        sleep(2)
        touch(Template(r"tpl1754536197705.png", record_pos=(-0.43, 0.204), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754536203131.png", record_pos=(0.326, 0.209), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754536212154.png", record_pos=(0.425, -0.003), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754536216044.png", record_pos=(0.44, -0.007), resolution=(1600, 900)))
        sleep(2)
        touch(wait(Template(r"tpl1754536238158.png", record_pos=(-0.432, 0.089), resolution=(1600, 900))))
        sleep(1)
        touch(Template(r"tpl1758782698762.png", record_pos=(-0.431, 0.093), resolution=(1600, 900)))
        sleep(15)
        touch(wait(Template(r"tpl1754536275449.png", record_pos=(-0.158, -0.026), resolution=(1600, 900))))
        sleep(2)
        auto_tap_continue(max_taps=1000, interval=1)
        touch(wait(Template(r"tpl1754536275449.png", record_pos=(-0.158, -0.026), resolution=(1600, 900))))
        auto_tap_continue(max_taps=1000, interval=1)
        sleep(2)
        touch(Template(r"tpl1754536344337.png", record_pos=(0.2, 0.015), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754536347050.png", record_pos=(-0.438, 0.194), resolution=(1600, 900)))
            sleep(2)
        else:
            raise Exception("The expected template does not exist.")
        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754536349931.png", record_pos=(-0.438, 0.194), resolution=(1600, 900)))
            sleep(2)
        else:
            raise Exception("The expected template does not exist.")
        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754536352530.png", record_pos=(-0.438, 0.194), resolution=(1600, 900)))
            sleep(2)
        else:
            raise Exception("The expected template does not exist.")
        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754536361633.png", record_pos=(-0.431, 0.086), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1758784640941.png", record_pos=(-0.436, 0.094), resolution=(1600, 900)))
            sleep(20)
        else:
            raise Exception("The expected template does not exist.")
        auto_tap_continue(max_taps=1000, interval=1)
        touch(Template(r"tpl1756435617829.png", record_pos=(-0.125, -0.05), resolution=(2480, 1148)))
        sleep(2)
        touch(wait(Template(r"tpl1756693647588.png", record_pos=(0.451, -0.251), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1756693656572.png", threshold=0.9, rgb=True, record_pos=(0.292, 0.119),
                            resolution=(1600, 900))))
        sleep(2)
        touch(wait(Template(r"tpl1756693678912.png", threshold=0.8, rgb=False, record_pos=(0.451, -0.252),
                            resolution=(1600, 900))))
        touch(wait(Template(r"tpl1756693684172.png", record_pos=(0.292, 0.118), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1754468386708.png", record_pos=(0.134, 0.104))))
        sleep(2)
        name = random.randint(100000, 999999)
        text(f"{name}")
        touch(Template(r"tpl1754468414653.png", record_pos=(0.444, 0.246)))
        touch(Template(r"tpl1754530753913.png", record_pos=(0.377, 0.151)))
        sleep(10)
        if exists(Template(r"tpl1756964491695.png", record_pos=(0.062, -0.124), resolution=(1600, 900))):

            print("进入第一章")
            touch(Template(r"tpl1756964502426.png", record_pos=(-0.388, -0.234), resolution=(1600, 900)))
            touch(Template(r"tpl1754468482626.png", record_pos=(-0.438, 0.087)))
            touch(Template(r"tpl1754468485179.png", record_pos=(-0.428, 0.203)))

            touch(Template(r"tpl1754468487171.png", record_pos=(0.335, 0.228)))
        else:
            raise Exception("无法进入第一章节")

        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754468489051.png", record_pos=(0.349, 0.228)))
            sleep(2)
        else:
            raise Exception("第一章引导丢失")
        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754468491296.png", record_pos=(0.446, -0.089)))

            sleep(1)
        else:
            raise Exception("第一章引导丢失")
        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754468493433.png", record_pos=(0.454, -0.1)))
            sleep(1)
        else:
            raise Exception("The expected template does not exist.")
        touch(Template(r"tpl1754468503516.png", record_pos=(0.348, 0.225)))
        sleep(2)
        touch(Template(r"tpl1754468505608.png", record_pos=(-0.432, 0.094)))

        touch(Template(r"tpl1754530858082.png", record_pos=(-0.431, 0.113)))

        sleep(8)
        touch(wait(Template(r"tpl1756693804966.png", record_pos=(0.453, -0.251), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1756693819538.png", record_pos=(0.287, 0.117), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1754538815134.png", record_pos=(0.007, 0.142))))

        sleep(3)
        touch(Template(r"tpl1754538821150.png", record_pos=(-0.231, -0.182)))

        sleep(5)
        touch(wait(Template(r"tpl1756693853676.png", record_pos=(0.452, -0.252), resolution=(1600, 900))))
        touch(Template(r"tpl1754468570439.png", record_pos=(0.058, 0.051), resolution=(1600, 900)))
        wait(Template(r"tpl1754468598477.png", record_pos=(0.011, -0.174), resolution=(1600, 900)), timeout=20)
        sleep(2)
        touch((1084,241))
        touch(wait(Template(r"tpl1756693902112.png", record_pos=(0.456, -0.246), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1756693905472.png", record_pos=(0.295, 0.111), resolution=(1600, 900))))
        sleep(5)
        touch(Template(r"tpl1754468608651.png", record_pos=(-0.247, -0.081), resolution=(1600, 900)))
        touch(Template(r"tpl1754468612055.png", record_pos=(-0.246, -0.154), resolution=(1600, 900)))
        touch(Template(r"tpl1754531008332.png", record_pos=(0.003, -0.182), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468620861.png", record_pos=(-0.092, -0.065), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468624052.png", record_pos=(-0.101, -0.031), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754531053956.png", record_pos=(0.46, 0.252), resolution=(1600, 900)))
        sleep(2)

        touch(Template(r"tpl1754468630056.png", record_pos=(0.053, -0.156), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754531086228.png", record_pos=(0.059, -0.186), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468637694.png", record_pos=(0.457, 0.248), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468641212.png", record_pos=(-0.164, 0.022), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468643795.png", record_pos=(0.213, -0.089), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754468647760.png", record_pos=(0.146, -0.123), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468650790.png", record_pos=(0.464, 0.251), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754540581042.png", record_pos=(0.339, 0.246), resolution=(1600, 900)))
        sleep(2)
        touch(wait(Template(r"tpl1756693985605.png", record_pos=(0.455, -0.25), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1756693989325.png", record_pos=(0.276, 0.119), resolution=(1600, 900))))
        sleep(6)

        if exists(Template(r"tpl1756710617494.png", record_pos=(-0.234, -0.048), resolution=(1600, 900))):
            touch(Template(r"tpl1754468707575.png", record_pos=(-0.153, -0.086), resolution=(1600, 900)))
            sleep(2)
        else:
            raise Exception("引导丢失")
        touch(Template(r"tpl1754468709771.png", record_pos=(0.336, 0.214), resolution=(1600, 900)))
        sleep(3)
        touch(Template(r"tpl1754468711845.png", record_pos=(0.453, -0.099), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468714167.png", record_pos=(0.456, -0.104), resolution=(1600, 900)))

        sleep(3)
        if exists(Template(r"tpl1756710617494.png", record_pos=(-0.234, -0.048), resolution=(1600, 900))):
            touch(Template(r"tpl1754531286820.png", record_pos=(-0.157, -0.096), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception("引导丢失")
        touch(Template(r"tpl1754468722374.png", record_pos=(-0.434, 0.094), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754531305402.png", record_pos=(-0.429, 0.074), resolution=(1600, 900)))
        sleep(5)
        if exists(Template(r"tpl1756694994721.png", record_pos=(-0.312, 0.205), resolution=(1600, 900))):
            touch(Template(r"tpl1754468732570.png", record_pos=(0.419, -0.186), resolution=(1600, 900)))
            touch(Template(r"tpl1754531349491.png", record_pos=(0.037, 0.018), resolution=(1600, 900)))
            touch(Template(r"tpl1754531372070.png", record_pos=(0.323, 0.229), resolution=(1600, 900)))
        else:
            raise Exception("提示克制关系引导未出现")
        touch(Template(r"tpl1754468748416.png", record_pos=(0.343, 0.235), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468751102.png", record_pos=(0.453, -0.091), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468752882.png", record_pos=(0.438, -0.098), resolution=(1600, 900)))
        sleep(2)
        touch(wait(Template(r"tpl1756694175694.png", record_pos=(0.459, -0.253), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1756694181772.png", record_pos=(0.287, 0.113), resolution=(1600, 900))))
        touch(wait(Template(r"tpl1754468841878.png", record_pos=(0.005, -0.092), resolution=(1600, 900))))
        touch(Template(r"tpl1754531665224.png", record_pos=(-0.406, 0.223), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754468864512.png", record_pos=(-0.459, 0.006), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468867226.png", record_pos=(-0.399, 0.158), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1754468873417.png", record_pos=(-0.239, -0.17), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754468887925.png", record_pos=(-0.468, -0.258), resolution=(1600, 900)))
        sleep(1)
        if exists(Template(r"tpl1756710617494.png", record_pos=(-0.234, -0.048), resolution=(1600, 900))):
            touch(Template(r"tpl1754531740413.png", record_pos=(-0.444, 0.197), resolution=(1600, 900)))
            sleep(1)
        else:
            raise Exception('引导丢失')

        touch(Template(r"tpl1754468898308.png", record_pos=(0.217, 0.223), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754468901759.png", record_pos=(-0.072, 0.179), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754468904053.png", record_pos=(0.203, 0.104), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754468913849.png", record_pos=(0.471, -0.249), resolution=(1600, 900)))
        sleep(2)
        touch((566, 756))
        sleep(2)
        touch(Template(r"tpl1756694290525.png", record_pos=(-0.248, -0.163), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1754468924096.png", record_pos=(-0.471, -0.259), resolution=(1600, 900)))
        touch(Template(r"tpl1754468927127.png", record_pos=(0.463, -0.209), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756710516397.png", record_pos=(0.377, -0.194), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756710527797.png", record_pos=(0.148, 0.149), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756710537303.png", record_pos=(0.284, -0.095), resolution=(1600, 900)))
        sleep(2)
        touch(Template(r"tpl1756710547400.png", record_pos=(0.468, -0.251), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756710553587.png", record_pos=(0.338, 0.119), resolution=(1600, 900)))
        sleep(4)
        touch((320, 425))
        sleep(4)
        touch((320, 425))
        sleep(3)
        touch(Template(r"tpl1756710600283.png", threshold=0.5, record_pos=(-0.386, -0.211), resolution=(1600, 900)))
        sleep(2)
        if exists(Template(r"tpl1756710617494.png", record_pos=(-0.234, -0.048), resolution=(1600, 900))):
            touch(Template(r"tpl1756710637297.png", record_pos=(0.289, -0.038), resolution=(1600, 900)))
            sleep(2)
        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900))):
            touch(Template(r"tpl1756711070032.png", record_pos=(0.439, 0.086), resolution=(1600, 900)))
            sleep(2)
            touch(Template(r"tpl1756711219904.png", record_pos=(0.407, 0.249), resolution=(1600, 900)))
            sleep(15)

        else:
            raise Exception("一键上阵引导丢失")
        if exists(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900))):
            touch(Template(r"tpl1756711263910.png", record_pos=(0.387, -0.247), resolution=(1600, 900)))
            sleep(1)

        else:
            raise Exception("加速引导丢失")
        if exists(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900))):
            touch(Template(r"tpl1756711293640.png", record_pos=(0.323, -0.25), resolution=(1600, 900)))
            sleep(1)

        else:
            raise Exception("自动打架引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            if exists(Template(r"tpl1754468841878.png", record_pos=(0.005, -0.092), resolution=(1600, 90))):
                touch(Template(r"tpl1754468841878.png", record_pos=(0.005, -0.092), resolution=(1600, 90)))
                touch((808,153))
            else:
                pass
            touch(Template(r"tpl1756711376850.png", record_pos=(-0.283, 0.221), resolution=(1600, 900)))
            sleep(4)
        else:
            raise Exception("召唤弹窗弹出两次")
        if not exists(Template(r"tpl1756711842901.png", record_pos=(0.399, 0.244), resolution=(1600, 900))):
            raise Exception("召唤弹窗弹出两次")
        touch(Template(r"tpl1756711842901.png", record_pos=(0.399, 0.244), resolution=(1600, 900)))
        sleep(1)

        if wait(Template(r"tpl1756711907533.png", record_pos=(0.031, -0.043), resolution=(1600, 900)), timeout=120):
            touch(Template(r"tpl1756711924218.png", record_pos=(0.002, -0.088), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1756711933600.png", record_pos=(-0.009, 0.127), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1756711944832.png", record_pos=(-0.398, 0.231), resolution=(1600, 900)))
            sleep(1)

        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756711991392.png", record_pos=(-0.322, 0.214), resolution=(1600, 900)))
            sleep(1)
            touch(Template(r"tpl1756712002592.png", record_pos=(-0.454, -0.126), resolution=(1600, 900)))
            sleep(1)

        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756712056650.png", record_pos=(-0.02, 0.04), resolution=(1600, 900))):
            touch(Template(r"tpl1756712063899.png", record_pos=(-0.287, 0.204), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756712092478.png", record_pos=(-0.133, -0.08), resolution=(1600, 900))):
            touch(Template(r"tpl1756712103525.png", record_pos=(-0.069, -0.172), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")

        if exists(Template(r"tpl1756712121330.png", record_pos=(-0.213, 0.106), resolution=(1600, 900))):
            touch(Template(r"tpl1756712132012.png", record_pos=(0.099, -0.048), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756712151003.png", record_pos=(-0.194, 0.254), resolution=(1600, 900))):
            touch(Template(r"tpl1756712158614.png", record_pos=(0.079, 0.089), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756712203083.png", record_pos=(-0.127, 0.083), resolution=(1600, 900))):
            touch(Template(r"tpl1756712222890.png", record_pos=(0.156, 0.196), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756712239946.png", record_pos=(0.095, -0.014), resolution=(1600, 900))):
            touch(Template(r"tpl1756712249493.png", record_pos=(0.459, -0.009), resolution=(1600, 900)))


        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756712283779.png", record_pos=(0.007, -0.124), resolution=(1600, 900))):
            touch(Template(r"tpl1756712289861.png", record_pos=(0.321, -0.178), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):

            touch(Template(r"tpl1756712289861.png", record_pos=(0.321, -0.178), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712387316.png", record_pos=(0.051, -0.014), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712410086.png", record_pos=(0.181, 0.189), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712420056.png", record_pos=(0.013, -0.018), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712430989.png", record_pos=(0.404, 0.241), resolution=(1600, 900)))


        else:
            raise Exception("引导丢失")

        if exists(Template(r"tpl1756712471073.png", record_pos=(-0.031, -0.015), resolution=(1600, 900))):
            touch(Template(r"tpl1756712477395.png", record_pos=(0.108, 0.044), resolution=(1600, 900)))
            touch(Template(r"tpl1756712483983.png", record_pos=(0.146, 0.121), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712500347.png", record_pos=(-0.363, -0.259), resolution=(1600, 900)))


        else:
            raise Exception("引导丢失")
        if exists(Template(r"tpl1756787588181.png", threshold=0.9, record_pos=(0.471, -0.219), resolution=(1600, 900))):

            touch(Template(r"tpl1756787597384.png", threshold=0.9, record_pos=(0.467, -0.217), resolution=(1600, 900)))

        else:
            pass
        touch(Template(r"tpl1756712546834.png", record_pos=(0.389, -0.191), resolution=(1600, 900)))

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712561565.png", record_pos=(0.414, -0.084), resolution=(1600, 900)))


        else:

            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712579436.png", record_pos=(0.342, -0.089), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        sleep(2)
        touch(Template(r"tpl1756712599124.png", record_pos=(0.47, -0.25), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756712607858.png", record_pos=(0.333, 0.117), resolution=(1600, 900)))
        wait(Template(r"tpl1756991173544.png", record_pos=(0.001, -0.117), resolution=(1600, 900)))
        touch(Template(r"tpl1756712615965.png", record_pos=(-0.339, -0.195), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756712642959.png", record_pos=(0.242, -0.046), resolution=(1600, 900)))
        sleep(1)
        touch(Template(r"tpl1756712651425.png", record_pos=(0.404, 0.249), resolution=(1600, 900)))
        sleep(1)
        if wait(Template(r"tpl1756712702783.png", record_pos=(0.029, -0.034), resolution=(1600, 900)), timeout=150):
            touch(Template(r"tpl1756712724448.png", record_pos=(0.003, -0.087), resolution=(1600, 900)))
            sleep(1)


        else:
            raise Exception("引导丢失")

        if exists(Template(r"tpl1756712767662.png", record_pos=(-0.012, -0.092), resolution=(1600, 900))):
            touch(Template(r"tpl1756712777508.png", record_pos=(0.014, -0.096), resolution=(1600, 900)))
            sleep(1)

        else:
            raise Exception("引导丢失")
        touch(Template(r"tpl1756712799807.png", record_pos=(-0.415, 0.231), resolution=(1600, 900)))
        sleep(1)
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712820334.png", record_pos=(0.386, 0.171), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712837646.png", record_pos=(-0.113, 0.251), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712853111.png", record_pos=(0.208, -0.009), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712871767.png", record_pos=(-0.188, -0.071), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712883823.png", record_pos=(0.332, 0.238), resolution=(1600, 900)))
            sleep(3)



        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712896550.png", record_pos=(0.394, 0.249), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756712943120.png", threshold=0.9, record_pos=(0.266, -0.195), resolution=(1600, 900)), timeout=160):
            sleep(4)
            touch(Template(r"tpl1756712949044.png", record_pos=(-0.397, 0.229), resolution=(1600, 900)))
        else:
            raise Exception("游戏失败出错")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756712994240.png", record_pos=(-0.211, 0.216), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch((249, 193))
        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756713025129.png", record_pos=(-0.344, 0.231), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")

        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756713034587.png", record_pos=(0.443, 0.216), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):

            touch(Template(r"tpl1756713089122.png", record_pos=(0.315, 0.216), resolution=(1600, 900)))

        else:
            raise Exception("引导丢失")
        if wait(Template(r"tpl1756710775458.png", record_pos=(-0.002, 0.182), resolution=(1600, 900)), timeout=60):
            touch(Template(r"tpl1756713108533.png", record_pos=(-0.362, -0.254), resolution=(1600, 900)))
        else:
            raise Exception("引导丢失")
    except Exception as e:
        erro_pass()
        raise


if __name__ == '__main__':
    script_path = __file__
    script_name, _ = os.path.splitext(os.path.basename(__file__))
    for i in range(1):
        start_time = time.time()
        file_time = timestamp

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

        # 指定目录路径
        directory = Path(r"H:\Millennium Journey_Automation\ch_new_hand.air\log")
        # 遍历目录中所有 .png 文件（不包括子目录）
        for png_file in directory.glob("*.jpg"):
            if png_file.is_file():  # 确保是文件
                png_file.unlink()  # 删除文件
                print(f"已删除: {png_file}")
        try:
            Recorder(dev).start_recording(max_time=6000)
            open_app()
            main_process()
        except Exception as e:
            print(f"脚本执行异常: {e}")
            erro_message = traceback.format_exc()
            print(erro_message)
            result = "FAIL"
        finally:
            Recorder(dev).stop_recording(output="test.mp4")
            LogToHtml(__file__,
                      export_dir=r"H:\Millennium Journey_Automation\ch_new_hand.air",
                      lang="zh",
                      ).report(output_file="test.html")
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
            report_html = fr"http://192.168.30.148:8000/ch_new_hand.air/ch_new_hand.log/test.html"
            print(f"脚本执行完成，耗时: {duration:.2f}秒")
        if result == "SUCCESS":
            sender.send_markdown_message(
                f"**执行结果**: <font color='info'>{result}</font>\n"
                f"**设备名称**: {phone}\n"
                f"**用户账号**: {root}\n"
                f"**脚本文件**: {file}\n"
                f"**耗时**: {duration:.2f}秒\n"
                f"**报告地址**:[{report_html}]({report_html})"

            )
        else:
            sender.send_markdown_message(
                f"**执行结果**: <font color='warning'>{result}</font>\n"
                f"**设备名称**: {phone}\n"
                f"**用户账号**: {root}\n"
                f"**脚本文件**: {file}\n"
                f"**耗时**: {duration:.2f}秒\n"
                f"**报告地址**:[{report_html}]({report_html})\n"
                f"**错误信息**: \n```\n{erro_message}\n```"
            )









