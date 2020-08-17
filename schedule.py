from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import operate


def download():
    operate.downloadFile('BEIJING')
    operate.downloadFile('SHANGHAI')
    operate.downloadFile('HONGKONG')
    operate.downloadFile('TAIBEI')


def upload():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dateFormat = date[2:4] + date[5:7] + date[8:10]
    ftpUpload = operate.connectFTP(host='172.20.6.50', username='zz0836', password='kiddlkd0122001')
    operate.uploadFile(ftpUpload, "BEIJING", dateFormat)
    operate.uploadFile(ftpUpload, "SHANGHAI", dateFormat)
    operate.uploadFile(ftpUpload, "HONGKONG", dateFormat)
    operate.uploadFile(ftpUpload, "TAIBEI", dateFormat)
    ftpUpload.quit()


def main():
    download()
    upload()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'cron', hour=13, minute=10)
    scheduler.start()
