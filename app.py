import json
import uuid

from flask import Flask, Response, make_response, request, render_template, redirect, url_for

import settings

app = Flask(__name__)
print(app.config)
app.config.from_object(settings)

# app.config['DEBUG'] = True

data = {
    'a': 'taipei',
    'b': 'new taipei'
}


class Girl:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.gender = '女'

    def __str__(self):
        return self.name


@app.route('/', endpoint='index')
def hello_world():
    return 'Hello World!'


@app.route('/getcity/<key>')
def get_city(key):
    return data.get(key)


@app.route('/add/<int:key>')
def add(key):
    return str(key + 10)


@app.route('/index/<path:p>')
def get_path(p):
    return str(p)


@app.route('/test/<uuid:id>')
def test(id):
    return str(id)


@app.route('/test1')
def test1():
    return str(uuid.uuid4())


@app.route('/test11')
def test12():
    return data


@app.route('/test2')
def test2():
    return '234', 200


@app.route('/test3')
def test3():
    return Response('888')


@app.route('/test4')
def test4():
    print(request.headers)
    content = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
123
</body>
</html>
    '''
    res = make_response(content)
    res.headers['mytest'] = '123abc'
    return res


@app.route('/test5')
def test5():
    return render_template('register.html')


@app.route('/test52', methods=['GET', 'POST'])
def test52():
    # get 請求
    # print(request.args)
    # print(request.args.get('vv'))
    if request.method == 'POST':
        # post請求
        print(request.form.get('vv'))
        users = []
        users.append({'name': 'jason'})
        # return json.dumps(users)
        return redirect('/test3')
    return '123'


@app.route('/testu')
def testu():
    return url_for('test5')


@app.route('/show')
def show():
    name = 'jason'
    friends = ['arr', 'gg']
    dict = {'gift': 'apple', 'gift1': 'clock'}
    g = Girl('mei', 'taipei')
    return render_template('show.html', name=name, friends=friends, dict=dict, g=g)


@app.route('/show2')
def show2():
    name = 'jason'
    friends = ['arr', 'gg']
    dict = {'gift': 'apple', 'gift1': 'clock'}
    g = Girl('mei', 'taipei')
    msg = '<h1>520 happy</h1>'
    return render_template('show2_filter.html', name=name, friends=friends, dict=dict, g=g, msg=msg)


@app.route('/show3')
def show3():
    name = 'jason'
    friends = ['arr', 'gg']
    dict = {'gift': 'apple', 'gift1': 'clock'}
    g = Girl('mei', 'taipei')
    msg = '<h1>520 happy</h1>'
    return render_template('show2_filter_self.html', name=name, friends=friends, dict=dict, g=g, msg=msg)


def replace_hello(value):
    print(value)
    value = value.replace('hello', '')
    return value.strip()


app.add_template_filter(replace_hello, 'replace_hello')

@app.template_filter('list_r')
def reverse_list(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li

if __name__ == '__main__':
    app.run()
