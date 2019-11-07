from datetime import datetime
from urllib.request import urlopen, Request
from os import remove, path
from glob import iglob

fileTemplate = '/tmp/genusswerkbot/menu_cw{}.pdf'

def getYear():
    return datetime.today().strftime('%Y')

def getMonth():
    return datetime.today().strftime('%m')

def getWeek():
    return datetime.today().strftime('%V')

def weekMenuFilename():
    return fileTemplate.format(getWeek())

def expectedMenuUrl():
    template = 'https://das-genusswerk.at/wp-content/uploads/{}/{}/Men%C3%BCplan-KW-{}-das-genusswerk.pdf'
    return template.format(getYear(), getMonth(), getWeek())

def downloadCurrentMenu():
    url = expectedMenuUrl()
    fileName = weekMenuFilename()

    if (path.exists(fileName)):
        print('Using previously downloaded {}\n'.format(fileName))
        return True, fileName

    print('Downloading {}...\n'.format(url))
    
    userAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
    request  = Request(url, headers={'User-Agent': userAgent})
    response = urlopen(request)
    
    with open(fileName, 'wb') as pdf:
        pdf.write(response.read())

    return path.exists(fileName), fileName

def cleanup():
    currentWeek = weekMenuFilename()
    for fileName in iglob(fileTemplate.format('*')):    
        if fileName != currentWeek:
            remove(fileName)
