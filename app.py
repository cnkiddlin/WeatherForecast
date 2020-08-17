from flask import Flask, render_template
from flask_apscheduler import APScheduler
import os


# Create static folder if it doesn't exist
if not os.path.exists('static'):
    os.mkdir('static', mode=0o777)
    os.makedirs('static/BEIJING', mode=0o777)
    os.makedirs('static/HONGKONG', mode=0o777)
    os.makedirs('static/SHANGHAI', mode=0o777)
    os.makedirs('static/TAIPEI', mode=0o777)


def create_app():
    app = Flask(__name__)
    app.config.update({
        "SCHEDULER_API_ENABLED": True,
        "JOBS": [{
            "id": "download_and_upload",
            "func": "schedule:downAndUp",
            "trigger": "cron",
            "hour": 16,
            "minute": 6
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


@app.route('/Taipei')
def taipei():
    return render_template('taipei.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)