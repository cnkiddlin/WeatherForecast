from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import operate


def download():
    ftpDownload = operate.connectFTP(host='54.228.180.161', username='ukprism', password='PrettyP1ctures.')
    operate.downloadFile(ftpDownload, 'HONGKONG')
    operate.downloadFile(ftpDownload, 'BEIJING')
    operate.downloadFile(ftpDownload, 'SHANGHAI')
    operate.downloadFile(ftpDownload, 'TAIBEI')
    ftpDownload.quit()


def upload():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dateFormat = date[2:4] + date[5:7] + date[8:10]

    ftpUpload = operate.connectFTP(host='172.20.6.50', username='zz0836', password='Q2bEKOW%')
    operate.uploadFile(ftpUpload, "HONGKONG", dateFormat)
    operate.uploadFile(ftpUpload, "BEIJING", dateFormat)
    operate.uploadFile(ftpUpload, "SHANGHAI", dateFormat)
    operate.uploadFile(ftpUpload, "TAIBEI", dateFormat)
    ftpUpload.quit()


def main():
    download()
    upload()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'cron', hour=9)
    scheduler.start()