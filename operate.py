import ftplib


def connectFTP(host, username, password):
    ftp = ftplib.FTP()
    ftp.set_pasv(False)
    ftp.connect(host, timeout=30)
    ftp.login(username, password)
    return ftp


def downloadFile(location):
    ftp = connectFTP(host='54.228.180.161', username='ukprism', password='PrettyP1ctures.')
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
    finally:
        ftp.quit()


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

if __name__ == '__main__':
    downloadFile('SHANGHAI')