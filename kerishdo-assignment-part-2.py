#Assignment strategies part 2
#Student name: Kerish Do
#Student ID: 000885324



print('Welcome to Circle Phones’ Profit calculator. You can calculate your profits for a specific day, by week or you can divide the week into weekdays and the weekend. ')
print('Welcome to Circle Phones Profit calculator ')

#Variables
Aiphone = 120.45
Andiphone = 99.50
Atablet = 75.69
Andtablet = 65.73
WinTablet = 51.49

#These time period list
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday' ]
workweeks = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday']
wk = ['Saturday', 'Sunday']


dieuKien = 1
while dieuKien == 1:
    print('You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend')
    print ("""Enter:
        \t1 - For specific Day
        \t2 - For the week (7 Days)
        \t3 - For Week Business Days (Monday to Friday)
        \t4 - For Happy Weekend days 
        \t0 - Exit """)
    timePeriod = int(input())
    if timePeriod == 1:
        i = 1
        totalProfitForTheDay = 0
        print('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n')
        day = input()
        while i == 1:
            print('Enter product number 1-5, or enter 0 to stop: ')
            product_number = int(input())

            if product_number == 1:
                price = float(120.45)
            elif product_number == 2:
                price = float(99.5)
            elif product_number == 3:
                price = float(75.69)
            elif product_number == 4:
                price = float(65.73)
            elif product_number == 5:
                price = float(51.49)


            if product_number > 0 and product_number <= 5: 
                print('Enter quantity sold: ')
                quantity = int(input())
                totalProfitForThatCategory = float(price * quantity) 
                totalProfitForTheDay = totalProfitForTheDay + totalProfitForThatCategory 

            elif product_number < 0 or product_number > 5:
                print ('Please enter product number 1 - 5 only, or enter 0 to stop!') 
            else: 
                i = 0 
        else: 
            print ('Total Profit for the',day,'is: $', totalProfitForTheDay,'\n')
            if totalProfitForTheDay >= 10000:
                print('You did well this',day,'!','Keep up the great work!\n')
            else: print('We did not reach our goal for this',day,'. More work is needed.\n')
    if timePeriod == 2:
        b = 1
        totalProfitForTheWeek = 0
        w = -1
        while b == 1:    
            i = 1
            w = w + 1
            if w < 7:
                print('For', weekdays[w])
                while i == 1: 
                    print('Enter product number 1-5, or enter 0 to stop: ')
                    product_number = int(input())

                    if product_number == 1:
                        price = float(120.45)
                    elif product_number == 2:
                        price = float(99.5)
                    elif product_number == 3:
                        price = float(75.69)
                    elif product_number == 4:
                        price = float(65.73)
                    elif product_number == 5:
                        price = float(51.49)

                    if product_number > 0 and product_number <= 5: 
                        print('Enter quantity sold: ')
                        quantity = int(input())
                        totalProfitForThatCategory = float(price * quantity) 
                        totalProfitForTheWeek = totalProfitForTheWeek + totalProfitForThatCategory 

                    elif product_number < 0 or product_number > 5:
                        print ('Please enter product number 1 - 5 only, or enter 0 to stop!') 
                    else: 
                        i = 0      
            else:
                b = 0
                print ('Total Profit for the week is: $', totalProfitForTheWeek,'\n')
                if totalProfitForTheWeek >= 10000:
                    print('You did well this week! Keep up the great work!\n')
                else: print('We did not reach our goal for this week. More work is needed.\n')
    if timePeriod == 3:
        b = 1
        totalProfitForBusinessDays = 0
        w = -1
        while b == 1:    
            i = 1
            w = w + 1
            if w < 5:
                print('For', workweeks[w])
                while i == 1: 
                    print('Enter product number 1-5, or enter 0 to stop: ')
                    product_number = int(input())

                    if product_number == 1:
                        price = float(120.45)
                    elif product_number == 2:
                        price = float(99.5)
                    elif product_number == 3:
                        price = float(75.69)
                    elif product_number == 4:
                        price = float(65.73)
                    elif product_number == 5:
                        price = float(51.49)

                    if product_number > 0 and product_number <= 5: 
                        print('Enter quantity sold: ')
                        quantity = int(input())
                        totalProfitForThatCategory = float(price * quantity) 
                        totalProfitForBusinessDays = totalProfitForBusinessDays + totalProfitForThatCategory 

                    elif product_number < 0 or product_number > 5:
                        print ('Please enter product number 1 - 5 only, or enter 0 to stop!') 
                    else: 
                        i = 0      
            else:
                b = 0
                print ('Total Profit for the week (business days) is: $', totalProfitForBusinessDays,'\n')
                if totalProfitForBusinessDays >= 10000:
                    print('You did well this week (business days)! Keep up the great work!\n')
                else: print('We did not reach our goal for this week (business days). More work is needed.\n')
    if timePeriod == 4:
        b = 1
        totalProfitForWeekendDays = 0
        w = -1
        while b == 1:    
            i = 1
            w = w + 1
            if w < 2:
                print('For', wk[w])
                while i == 1: 
                    print('Enter product number 1-5, or enter 0 to stop: ')
                    product_number = int(input())

                    if product_number == 1:
                        price = float(120.45)
                    elif product_number == 2:
                        price = float(99.5)
                    elif product_number == 3:
                        price = float(75.69)
                    elif product_number == 4:
                        price = float(65.73)
                    elif product_number == 5:
                        price = float(51.49)

                    if product_number > 0 and product_number <= 5: 
                        print('Enter quantity sold: ')
                        quantity = int(input())
                        totalProfitForThatCategory = float(price * quantity) 
                        totalProfitForWeekendDays = totalProfitForWeekendDays + totalProfitForThatCategory 

                    elif product_number < 0 or product_number > 5:
                        print ('Please enter product number 1 - 5 only, or enter 0 to stop!') 
                    else: 
                        i = 0      
            else:
                b = 0
                print ('Total Profit for the weekend is: $', totalProfitForWeekendDays,'\n')
                if totalProfitForWeekendDays >= 10000:
                    print('You did well this weekend! Keep up the great work!\n')
                else: print("We did not reach our goal for this weekend. More work is needed.\n")
    elif timePeriod == 0:
        dieuKien = 0



    
    