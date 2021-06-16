from flask import Flask
from flask import request

application = Flask(__name__)

@application.route('/')
def index():
    s = """
<html><body>
<form action="/calc" method="post">
 <input type="text" name="a">x
 <input type="text" name="b">
 <input type="submit" value="計算">
</form>
</body></html>
"""
    return s

# フォームの処理
@application.route('/calc', methods=["post"])
def calc():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    ret = a * b
    return "<H1>掛け算の結果は {}".format(ret)

