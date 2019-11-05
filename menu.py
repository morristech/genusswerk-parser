class Day:

    def __init__(self):
        self.date = ''
        self.soup1 = ''
        self.soup2 = ''
        self.menu1 = ''
        self.menu2 = ''
        self.menu3 = ''

    def __str__(self):
        l1 = "*Genusswerk Menu for " + self.date + ":*\n"
        l2 = "*Soups:* " + self.soup1 + " OR " + self.soup2 + "\n"
        l3 = "*Menu 1:* " + self.menu1 + "\n"
        l4 = "*Menu 2:* " + self.menu2 + "\n"
        l5 = "*Menu 3:* " + self.menu3 + "\n"

        return l1 + l2 + l3 + l4 + l5


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
