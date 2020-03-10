import ftplib
import datetime


def connectFTP(host, username, password):
    ftp = ftplib.FTP()
    ftp.connect(host, timeout=30)
    ftp.login(username, password)
    return ftp


def downloadFile(ftp, location):
    localpath = './static/' + location + '/'
    try:
        for name in ftp.nlst():
            if location in name:
                path = localpath + location + '.mov'
                f = open(path, 'wb')
                print('----------Start download ' + name + '---------')
                ftp.retrbinary('RETR ' + name, f.write)
                f.close()
                print('Download of ' + name + ' done!')
                return
        print('Weather forecast of ' + location + ' not found!')
    except:
        print('Error: Download Failed!')


def uploadFile(ftp, location, date):
    try:
        ftp.cwd("/Contents/Weather Forecast")
        deletePrevious(ftp, location)
        f = open("./static/" + location + '/' + location + '.mov', 'rb')
        filename = location + date + '.mov'
        print('----------Start upload ' + filename + '----------')
        ftp.storbinary("STOR " + filename, f)
        f.close()
        print('Upload of ' + filename + ' done!')
    except:
        print('Error: Upload ' + location + ' Failed!')


def deletePrevious(ftp, location):
    try:
        for name in ftp.nlst():
            if location in name:
                print('----------Start deleting previos video of ' + location + '----------')
                ftp.delete(name)
                print('Previos video of ' + location + ' deleted!')
                return True
        print('Previos video of ' + location + ' not found!')
    except:
        print('Error: Delete Failed!')


def main():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dateFormat = date[2:4] + date[5:7] + date[8:10]

    ftpDownload = connectFTP(host='54.228.180.161', username='ukprism', password='PrettyP1ctures.')
    downloadFile(ftpDownload, 'HONGKONG')
    downloadFile(ftpDownload, 'BEIJING')
    downloadFile(ftpDownload, 'SHANGHAI')
    ftpDownload.quit()

    ftpUpload = connectFTP(host='172.20.6.50', username='zz0836', password='Q2bEKOW%')
    uploadFile(ftpUpload, "HONGKONG", dateFormat)
    uploadFile(ftpUpload, "BEIJING", dateFormat)
    uploadFile(ftpUpload, "SHANGHAI", dateFormat)
    ftpUpload.quit()


if __name__ == '__main__':
    main()



