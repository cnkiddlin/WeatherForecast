from flask import Flask, render_template
from flask_apscheduler import APScheduler


def create_app():
    app = Flask(__name__)
    app.config.update({
        "SCHEDULER_API_ENABLED": True,
        "JOBS": [{
            "id": "download_and_upload",
            "func": "schedule:main",
            "trigger": "cron",
            "hour": 9
        }]
    })
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    return app


app = create_app()


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
    app.run(host='0.0.0.0', debug=False)