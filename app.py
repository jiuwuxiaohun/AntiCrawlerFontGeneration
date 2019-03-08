# encoding: utf-8
# -*-*-
# By:连长 『zh (www.lianzhang.org)』
# -*-*-
import linecache
import random

from flask import Flask, json, render_template

app = Flask(__name__)


def random_json():
    count = len(open('json.json', 'rU').readlines())  # 获取行数
    hellonum = random.randrange(1, count, 1)  # 生成随机行数
    return linecache.getline('json.json', hellonum)  # 随机读取某行


@app.route('/')
def index():
    import random
    jsons = random_json()
    dictjsons = json.loads(jsons)

    dict_values = dictjsons['data'].values()
    random.shuffle(dict_values)
    context = {
        'fonturl': dictjsons['url'],
        'data': dict_values,

    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
