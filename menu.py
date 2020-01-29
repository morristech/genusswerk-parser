class Day:

    def __init__(self):
        self.date = ''
        self.soup1 = ''
        self.soup2 = ''
        self.menu1 = ''
        self.menu2 = ''
        self.menu3 = ''

    def addPrices(self, priceList):
        self.s2_price = priceList[0]
        self.m1_price = priceList[1]
        self.m2_price = priceList[2]
        self.m3_price = priceList[3]


    def __str__(self):
        title = "*Genusswerk Menu for " + self.date + ":*\n"
        s1 = "*Soup 1:* " + self.soup1 + "\n" 
        s2 = "*Soup 2 (+" + self.s2_price + "€):* " + self.soup2 + "\n"
        m1 = "*Menu 1 ("+self.m1_price+"€):* " + self.menu1 + "\n"
        m2 = "*Menu 2 ("+self.m2_price+"€):* " + self.menu2 + "\n"
        m3 = "*Menu 3 ("+self.m3_price+"€):* " + self.menu3 + "\n"

        return title + s1 + s2 + m1 + m2 + m3


class Week:
    
    def __init__(self):
        self.menus = [] 

    def addNextDay(self, day):
        self.menus.append(day)

    def getTodaysMenu(self):
        from datetime import datetime
        weekday = datetime.today().weekday()
        if (weekday > 4):
            print('Enjoy your weekend and cook for yourself!')
            return
        index = weekday
        return self.menus[index]

    def __str__(self):
        output = ''
        for day in self.menus:
            output += '\n' + str(day)
        return output
