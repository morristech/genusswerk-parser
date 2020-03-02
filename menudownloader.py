from datetime import datetime
from urllib.request import urlopen, Request
from os import remove, path
from glob import iglob
from pathlib import Path

defaultFolder = './menus/'
fileTemplate = 'menu_cw{}.pdf'

def getYear():
    return datetime.today().strftime('%Y')

def getMonth():
    return datetime.today().strftime('%m')

def getWeek():
    week = datetime.today().strftime('%V')
    if (int(week) < 10):
        return week.replace("0", "")
    return week

def weekMenuFilename():
    return fileTemplate.format(getWeek())

def expectedMenuUrl():
    template = 'https://das-genusswerk.at/wp-content/uploads/{}/{}/Men%C3%BCplan-KW-{}-das-Genusswerk.pdf'
    return template.format(getYear(), getMonth(), getWeek())

def downloadCurrentMenu(folder=defaultFolder):
    if folder == None: 
        folder = defaultFolder

    url = expectedMenuUrl()
    fileName = folder + weekMenuFilename()

    if (path.exists(fileName)):
        print('Using previously downloaded {}\n'.format(fileName))
        return True, fileName

    print('Downloading {}...\n'.format(url))
    
    userAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
    request  = Request(url, headers={'User-Agent': userAgent})
    response = urlopen(request)

    Path(folder).mkdir(parents=True, exist_ok=True)
    
    with open(fileName, 'wb') as pdf:
        pdf.write(response.read())

    return path.exists(fileName), fileName

def cleanup():
    currentWeek = weekMenuFilename()
    for fileName in iglob(fileTemplate.format('*')):    
        if fileName != currentWeek:
            remove(fileName)
