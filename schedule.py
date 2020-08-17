from apscheduler.schedulers.blocking import BlockingScheduler

import operate


def download():
    operate.downloadFile('BEIJING')
    operate.downloadFile('SHANGHAI')
    operate.downloadFile('TAIPEI')
    operate.downloadFile('HONGKONG')


def upload():
    ftpUpload = operate.connectFTP(host='172.20.6.50', username='zz0836', password='kiddLkd01220010')
    operate.uploadFile(ftpUpload, "BEIJING")
    operate.uploadFile(ftpUpload, "SHANGHAI")
    operate.uploadFile(ftpUpload, "TAIPEI")
    operate.uploadFile(ftpUpload, "HONGKONG")
    ftpUpload.quit()


def downAndUp():
    download()
    upload()


def deletePrevious():
    operate.deletePreviousLocal()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(downAndUp(), 'cron', hour=13, minute=10)
    scheduler.start()
    # upload()
    # deletePrevious()

