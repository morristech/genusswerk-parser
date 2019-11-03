import camelot
import matplotlib.pyplot as plt
import menu

def parsePdfMenu(path, debug=False):
    tables = camelot.read_pdf(path, flavor='stream', edge_tol=500, row_tol=50 , table_areas=['0,565,850,110'])
    if (tables.n != 1):
        return
    table = tables[0]
    
    if (debug):
        print(table)
        print(table.accuracy)
        camelot.plot(table, kind='contour')
        camelot.plot(table, kind='grid')
        plt.show()
    
    week = menu.Week()
    for row in table.data[1:]:
        if (len(row) != 6):
            return
        cleanRow = cleanParsedRow(row)
        day = parseMenuForDay(cleanRow)
        week.addNextDay(day)

    return week

def cleanParsedRow(row):
    cleanRow = []
    for col in row:
        cleanRow.append(' '.join(col.split()))
    return cleanRow

def parseMenuForDay(row):
    day = menu.Day()
    day.date  = row[0]
    day.soup1 = row[1]
    day.soup2 = row[2]
    day.menu1 = row[3]
    day.menu2 = row[4]
    day.menu3 = row[5]
    return day