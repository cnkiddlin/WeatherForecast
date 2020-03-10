from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/HongKong')
def hongkong():
    return render_template('hongkong.html')


@app.route('/Beijing')
def beijing():
    return render_template('beijing.html')


@app.route('/Shanghai')
def shanghai():
    return render_template('shanghai.html')


if __name__ == '__main__':
    app.debug = True
    app.run()