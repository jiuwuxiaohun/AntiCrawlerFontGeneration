# encoding: utf-8
# -*-*-
# By:连长 『zh (www.lianzhang.org)』
# -*-*-
import json
import random

from fontTools import ttx
from fontTools.ttLib import TTFont


def random_unicode(lengths):  # 随机生成Unicode字符集
    while True:
        shuma = ((str(random.sample(random_list, int(lengths))).replace('\'', '')).replace(',', '')). \
            replace(' ', '').replace('[', '').replace(']', '')
        if shuma[0].isalpha():
            return shuma
        else:
            continue


def TTFontsXML(filenames):  # 转换成XMl 到临时目录
    filenametemp = "temp/toolstemp.xml"
    font = TTFont(filenames)
    font.saveXML(filenametemp)
    return filenametemp


def TTFonts(filenames):  # 转换XML转换ttf
    try:
        print("开始转换字体！！！" + filenames)
        ttx.main([filenames])
        print ("-----------------------------------")
    except Exception as e:
        print ("Something went wrong converting ttx -> ttf/otf:")
        print (e)
        exit()


def Editfile(fontsjson, files):
    random_list = ["a", "v", "x", "s", "q", "w", "e", "r", "t", "y", "u", "i", "o", "z", "x", "c", "v", "b", "n", "m",
                   "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
    shuma = ((str(random.sample(random_list, int(25))).replace('\'', '')).replace(',', '')). \
        replace(' ', '').replace('[', '').replace(']', '')
    filenametemp = "temp/" + shuma + ".xml"

    try:
        with open(files, 'r+') as fileOpen:
            data = fileOpen.read()
            fileOpen.close()

        for key in fontsjson.keys():
            data = data.replace(str(relationdic[key]), str(fontsjson[key]))
            data = data.replace(str(relationdic[key]).upper(), str(fontsjson[key]).upper())
        with open(filenametemp, 'w') as f:
            f.write(data)
            f.close()
        return shuma + ".ttf", filenametemp
    except Exception, ex:
        print ex
        filenametemp = "error"
        filenames = ""
        return filenametemp, filenames


if __name__ == '__main__':
    random_list = ['e', 'a', 'd', 'f', 'c', 'b', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ttf_patn = "FontTest.ttf"  # 请输入ttf文件绝对路径:
    unicodelengths = 4  # 输入 UniCode 长度:
    ttfnumber = 10  # 输入生成多少个文件:
    relationdic = {"0": "e2f1", "1": "efab", "2": "eba3", "3": "eba5", "4": "edfd", "5": "c57f", "6": "e261",
                   "7": "f4d2", "8": "bad5", "9": "d4c2",
                   "A": "bfec5", "B": "fc736", "C": "e6d21", "D": "be4a9", "E": "c0e8f", "F": "d3c26", "G": "b18a0",
                   "H": "acb06", "I": "fd33e", "J": "fd36e", "K": "d417c", "L": "ad31e", "M": "ec95a", "N": "b39ce",
                   "O": "d508a", "P": "a961d", "Q": "a76b0", "R": "b7f12", "S": "b0426", "T": "d5941", "U": "ede47",
                   "V": "fc5a6", "W": "ed947", "X": "fd781", "Y": "b761a",
                   "Z": "af370", "a": "fde89", "b": "ecb21", "c": "c123c", "d": "b4c2c", "e": "cbbc7", "f": "c10cb",
                   "g": "cb78b", "h": "fdac7", "i": "076fe", "j": "d0def", "k": "ed6de", "l": "eaa1a", "m": "de1e9",
                   "n": "9eaa5", "o": "123e5", "p": "e12e2", "q": "e5efd", "r": "e6ea9", "s": "e1e8a", "t": "b8eac",
                   "u": "23e1c", "v": "ea6ac",
                   "w": "b87de", "x": "e5dac", "y": "2ccea",
                   "z": "3ada9"}  # 必须当前混淆ttf填入关系 否则不知道谁是谁了。。。生成的json 文件也是错误的。。
    try:

        macs = len(relationdic) + 50 * ttfnumber  # 可能会有重复 多加点
        tem_list = []
        for x in range(0, int(macs)):
            tem_list.append(random_unicode(unicodelengths))
        tem_list = list(set(tem_list))  # 去重

        tempfontsxmlpa = TTFontsXML(ttf_patn)  # 转换到临时XML地址。。

        okjson = []

        for f in range(0, ttfnumber):
            relationdictemp = relationdic.copy()
            for key in relationdictemp.keys():
                b = random.sample(tem_list, 1)
                tem_list.remove(b[0])
                relationdictemp[key] = b[0]
            filenames, filenametemp = Editfile(relationdictemp, tempfontsxmlpa)
            if filenametemp != "error":  # 如果返回修改成功 启动转换ttf的程序！
                TTFonts(filenametemp)
                jsonSeve = {"url": filenames, "data": relationdictemp}
                with open('json.json', 'a+') as json_file:
                    json_file.write(json.dumps(jsonSeve, ensure_ascii=False) + "\n")
    except Exception, ex:
        print ex
