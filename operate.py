import ftplib
import datetime
import requests
import os


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
                path = localpath + location + getDateToday() + '.mov'
                f = open(path, 'wb')
                print('----------Start downloading ' + name + '---------')
                ftp.retrbinary('RETR ' + name, f.write)
                f.close()
                print('Download of ' + name + ' done!')
                return
        print('Weather forecast of ' + location + ' not found!')
    except:
        print('Error: Download Failed!')
    finally:
        ftp.quit()


def uploadFile(ftp, location):
    try:
        ftp.cwd("/Contents/Weather Forecast")
        deletePreviousFtp(ftp, location)
        f = open("./static/" + location + '/' + location + getDateToday() + '.mov', 'rb')
        filename = location + getDateToday() + '.mov'
        print('----------Start upload ' + filename + '----------')
        ftp.storbinary("STOR " + filename, f)
        f.close()
        print('Upload of ' + filename + ' done!')
    except:
        print('Error: Upload ' + location + ' Failed!')


def deletePreviousFtp(ftp, location):
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


def deletePreviousLocal():
    print("删除昨天的天气预报")
    for location in ['BEIJING', 'SHANGHAI', 'TAIPEI', 'HONGKONG']:
        path = "./static/" + location + '/' + location + getDateYesterday() + '.mov'
        if os.path.exists(path):
            print(path)
            os.remove(path)
    print("删除完成")


def postDate():
    data = {'date': getDateToday()}
    r = requests.post('http://localhost:5000/date', data)
    print('Date Posted: ' + str(r.status_code))


def getDateToday():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    return today[2:4] + today[5:7] + today[8:10]


def getDateYesterday():
    date = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
    return date[2:4] + date[5:7] + date[8:10]


if __name__ == '__main__':
    # postDate()
    downloadFile('TAIPEI')
