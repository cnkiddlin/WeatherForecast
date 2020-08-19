from flask import Flask, render_template, request
from flask_apscheduler import APScheduler
import datetime
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
            "hour": 9,
            "minute": 45
        },
            {
                "id": "delete_previous_video",
                "func": "schedule:deletePrevious",
                "trigger": "cron",
                "hour": 10,
                "minute": 45
            }
        ]
    })
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Beijing')
def beijing():
    return render_template('beijing.html')


@app.route('/Shanghai')
def shanghai():
    return render_template('shanghai.html')


@app.route('/Taipei')
def taipei():
    return render_template('taipei.html')


@app.route('/HongKong')
def hongkong():
    return render_template('hongkong.html')


today = datetime.datetime.now().strftime('%Y-%m-%d')
date = today[2:4] + today[5:7] + today[8:10]
# date = "200818"
@app.route('/date/', methods=['POST', 'GET'])
def operateDate():
    global date
    if request.method == 'GET':
        return date
    else:
        date = request.form.get("date")
        return 'Changed: ' + date


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
