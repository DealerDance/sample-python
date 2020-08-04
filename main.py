#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'cloudtogo'

from flask import render_template
from flask import Flask
import os
import ctypes
import sys
app = Flask(__name__)

reload(sys)
sys.setdefaultencoding('utf8')


################################################################################

# 请修正下面错误的"Hello, word"的拼写！
# 请在修改完成后，通过主菜单 Git代码库/提交 ... 菜单项完成代码的Commit 和 Push。
# Push完成后回到 “趣码—应用工厂” 中该项目的 “蓝图” 页面( http://factory.cloudtogo.cn/project/blueprint?id=last )，点击发布新实例后，即可看到修改后的效果。

## 错误在这里 ___
#              |
#              V
msg = 'Hello, word!'

################################################################################


@app.route('/')
def hello():
    msg = '第一次修改!'

    return render_template('hello.html', Msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

