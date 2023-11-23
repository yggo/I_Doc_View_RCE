from flask import Flask, redirect, url_for

app = Flask(__name__)


# author: https://github.com/yggo

@app.route('/')
def index():
    return redirect(url_for('default_html'))


@app.route('/index.html')
def index_html():
    return redirect(url_for('default_html'))


@app.route('/default.html')
def default_html():
    return '''
    <link rel="stylesheet" href="/first_blood.jsp">
    <script src="/double_kill.jsp"></script>
    <img src="/..\\..\\..\\triple_kill.jsp">
    '''


@app.route('/first_blood.jsp')
def first_jsp():
    return '<% out.println("first_blood"); %>'


@app.route('/double_kill.jsp')
def second_jsp():
    return '<% out.println("double_kill"); %>'


@app.route('/..\\..\\..\\triple_kill.jsp')
def third_jsp():
    return '<% out.println("triple_kill"); %>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6666')
