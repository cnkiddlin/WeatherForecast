from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import operate


def download():
    ftpDownload = operate.connectFTP(host='54.228.180.161', username='ukprism', password='PrettyP1ctures.')
    operate.downloadFile(ftpDownload, 'HONGKONG')
    operate.downloadFile(ftpDownload, 'BEIJING')
    operate.downloadFile(ftpDownload, 'SHANGHAI')
    ftpDownload.quit()


def upload():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dateFormat = date[2:4] + date[5:7] + date[8:10]

    ftpUpload = operate.connectFTP(host='172.20.6.50', username='zz0836', password='Q2bEKOW%')
    operate.uploadFile(ftpUpload, "HONGKONG", dateFormat)
    operate.uploadFile(ftpUpload, "BEIJING", dateFormat)
    operate.uploadFile(ftpUpload, "SHANGHAI", dateFormat)
    ftpUpload.quit()


def main():
    print(1)
    scheduler = BlockingScheduler()
    scheduler.add_job(download, 'cron', day_of_week='1-5', hour=9, minute=45)
    scheduler.add_job(upload, 'cron', day_of_week='1-5', hour=15, minute=48)
    scheduler.start()


if __name__ == '__main__':
     main()