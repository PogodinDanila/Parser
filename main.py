from datetime import date, timedelta, datetime

MESSAGE = {'Status': 'Success',"Date":{"Day":None, "Month":None, "Year":None, "Hour":None, "Minute":None}, "Params":{"Repeat_always":None}}
text_i = input('Введите вашу строку: ')
n = text_i.split()

def vremy(text_i):
    if ":" in text_i:
        if (MESSAGE['Date']['Day'] == None):
            next_hour = str(date.today())
            next_hour = next_hour.split('-')
            MESSAGE['Date']['Year'] = next_hour[0]
            MESSAGE['Date']['Month'] = next_hour[1]
            MESSAGE['Date']['Day'] = next_hour[2]
        mins = text_i
        ind = mins.index(':')
        hours_1 = (mins.index(':')-2)
        hours_2 = (mins.index(':')-1)
        hours = str(mins[hours_1]) + str(mins[hours_2])
        minutes = str(mins.split(':')[1])
        MESSAGE['Date']['Hour']= hours
        MESSAGE['Date']['Minute'] = minutes
        text_i = text_i.split('в')
        text_message = text_i[0]
        MESSAGE['TEXT'] = text_message
def text_vivod(n):
    stroka =""
    for i in range(len(n)):
        stroka = stroka + " " + n[i]
    MESSAGE['TEXT'] = stroka

def check():
    l = [1, 3, 5, 7, 8, 10, 12]
    sh = [4, 6, 9, 11]
    if int(MESSAGE["Date"]["Minute"]) >= 60:
        MESSAGE["Date"]["Hour"] = int(MESSAGE["Date"]["Hour"]) + int(MESSAGE["Date"]["Minute"]) // 60
        MESSAGE["Date"]["Minute"] = int(MESSAGE["Date"]["Minute"]) % 60
    if int(MESSAGE["Date"]["Hour"]) >= 24:
        MESSAGE["Date"]["Day"] = str(int(MESSAGE["Date"]["Day"]) + int(MESSAGE["Date"]["Hour"]) // 24)
        MESSAGE["Date"]["Hour"] = str(int(MESSAGE["Date"]["Hour"]) % 24)
    while True:
        if int(MESSAGE["Date"]["Month"]) in l:
            if (int(MESSAGE["Date"]["Day"]) > 31):
                MESSAGE["Date"]["Day"] = str(int(MESSAGE["Date"]["Day"]) - 31)
                MESSAGE["Date"]["Month"] = str(int(MESSAGE["Date"]["Month"]) + 1)
            else:
                break
        elif int(MESSAGE["Date"]["Month"]) in sh:
            if (int(MESSAGE["Date"]["Day"]) > 30):
                MESSAGE["Date"]["Month"] = str(int(MESSAGE["Date"]["Month"]) + 1)
                MESSAGE["Date"]["Day"] = str(int(MESSAGE["Date"]["Day"]) - 30)
            else:
                break
        elif int(MESSAGE["Date"]["Month"]) == 2:
            if (int(MESSAGE["Date"]["Day"]) > 28):
                MESSAGE["Date"]["Month"] = str(int(MESSAGE["Date"]["Month"]) + 1)
                MESSAGE["Date"]["Day"] = str(int(MESSAGE["Date"]["Day"]) - 28)
            else:
                break
    if int(MESSAGE["Date"]["Month"]) > 12:
        MESSAGE["Date"]["Year"] = int(MESSAGE["Date"]["Year"]) + int(MESSAGE["Date"]["Month"]) // 12
        MESSAGE["Date"]["Month"] = int(MESSAGE["Date"]["Month"]) % 12
def months (m):
    if ("december" == m) | ("декабря" == m) | ("декабрь" == m) | ("Dec" == m) | ("декабре" == m):
        return "12"
    elif ("january" == m) | ("январь" == m) | ("января" == m) | ("Jan" == m) | ("январе" == m):
        return "1"
    elif ("february" == m) | ("февраль" == m) | ("февраля" == m) | ("Feb" == m) | ("феврале" == m):
        return "2"
    elif ("march" == m) | ("март" == m) | ("марта" == m) | ("Mar" == m) | ("марте" == m):
        return "3"
    elif ("april" == m) | ("апрель" == m) | ("апреля" == m) | ("Apr" == m) | ("апреле" == m):
        return "4"
    elif ("may" == m) | ("май" == m) | ("мая" == m) | ("May" == m) | ("мае" == m):
        return "5"
    elif ("june" == m) | ("июнь" == m) | ("июня" == m) | ("Jun" == m) | ("июне" == m):
        return "6"
    elif ("jule" == m) | ("июль" == m) | ("июля" == m) | ("Jul" == m) | ("июле" == m):
        return "7"
    elif ("august" == m) | ("август" == m) | ("августа" == m) | ("Aug" == m) | ("августе" == m):
        return "8"
    elif ("september" == m) | ("сентябрь" == m) | ("сентября" == m) | ("Sep" == m) | ("сентябре" == m):
        return "9"
    elif ("october" == m) | ("октябрь" == m) | ("октября" == m) | ("Oct" == m) | ("октябре" == m):
        return "10"
    elif ("november" == m) | ("ноябрь" == m) | ("ноября" == m) | ("Nov" == m) | ("ноябре" == m):
        return "11"
    return 0
def week(m):
    if ("monday" == m) | ("понедельник" == m) | ("понедельникам" == m) | ("Mon" == m):
        return "0"
    if ("tuesday" == m) | ("вторник" == m) | ("вторникам" == m) | ("Tue" == m):
        return "1"
    if ("wednesday" == m) | ("среда" == m) | ("средам" == m) | ("среду" == m) | ("Wed" == m):
        return "2"
    if ("thursday" == m) | ("четверг" == m) | ("четвергам" == m) | ("Thu" == m):
        return "3"
    if ("friday" == m) | ("пятница" == m) | ("пятница" == m) | ("пятницу" == m) | ("Fri" == m):
        return "4"
    if ("saturday" == m) | ("суббота" == m) | ("субботам" == m) | ("субботу" == m) | ("Sat" == m):
        return "5"
    if ("sunday" == m) | ("воскресенье" == m) | ("воскресеньям" == m) | ("воскресенье" == m) | ("Sun" == m):
        return "6"
    return 0
def week_opred(n):
    for i in n:
        putn = week(i)
    from datetime import date, timedelta, datetime
    data = datetime.today()
    t = data.weekday()
    if (int(putn) - t) > 0:
        day_week = str((date.today() + timedelta(days=(int(putn) - t))))
    if (int(putn) - t) <= 0:
        day_week = str((date.today() + timedelta(days=(7+(int(putn) - t)))))
    day_week = day_week.split('-')
    MESSAGE['Date']['Year'] = day_week[0]
    MESSAGE['Date']['Month'] = day_week[1]
    MESSAGE['Date']['Day'] = day_week[2]

def utro():
    now_time = str(date.today())
    now_time = now_time.split('-')
    MESSAGE['Date']['Year'] = now_time[0]
    MESSAGE['Date']['Month'] = now_time[1]
    MESSAGE['Date']['Day'] = now_time[2]
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    current_time = current_time.split(':')
    MESSAGE["Date"]["Hour"] = '9'
    MESSAGE["Date"]["Minute"] = '00'
    r = '9'
    if (int(current_time[0]) - int(r)) > 0:
        MESSAGE['Date']['Day'] = int(now_time[2]) + 1
def denb():
    now_time = str(date.today())
    now_time = now_time.split('-')
    MESSAGE['Date']['Year'] = now_time[0]
    MESSAGE['Date']['Month'] = now_time[1]
    MESSAGE['Date']['Day'] = now_time[2]
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    current_time = current_time.split(':')
    MESSAGE["Date"]["Hour"] = '12'
    MESSAGE["Date"]["Minute"] = '00'
    r = '12'
    if (int(current_time[0]) - int(r)) > 0:
        MESSAGE['Date']['Day'] = int(now_time[2]) + 1

def vecher():
    now_time = str(date.today())
    now_time = now_time.split('-')
    MESSAGE['Date']['Year'] = now_time[0]
    MESSAGE['Date']['Month'] = now_time[1]
    MESSAGE['Date']['Day'] = now_time[2]
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    current_time = current_time.split(':')
    MESSAGE["Date"]["Hour"] = '17'
    MESSAGE["Date"]["Minute"] = '00'
    r = '17'
    if (int(current_time[0])-int(r)) > 0:
        MESSAGE['Date']['Day'] = int(now_time[2])+1

def time_vsegda():
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    current_time = current_time.split(':')
    MESSAGE["Date"]["Hour"] = current_time[0]
    MESSAGE["Date"]["Minute"] = current_time[1]

if ('пятница' in n) or ('Friday' in n) or ('пятницу' in n):
    week_opred(n)

    time_vsegda()
    t = n.remove('пятницу')


if ('понедельник' in n) or ('Monday' in n):
    week_opred(n)

    time_vsegda()
    t = n.remove('понедельник')

if ('вторник' in n) or ('Thuesday' in n):
    week_opred(n)

    time_vsegda()
    t = n.remove('вторник')

if ('среда' in n) or ('среду' in n) or ('Wednesday' in n):
    week_opred(n)

    time_vsegda()
    t = n.remove('среду')

if ('четверг' in n) or ('Thursday' in n):
    week_opred(n)

    t = n.remove('четверг')
if ('суббота' in n) or ('субботу' in n) or ('Saturday' in n):
    week_opred(n)

    time_vsegda()
    t = n.remove('субботу')
if ('воскресенье' in n) or ('Sunday' in n):
    week_opred(n)

    time_vsegda()
    t = n.remove('воскресенье')





u=0
d=datetime.now()
now_mnt = d.strftime("%m")
now_day = d.strftime("%d")
for i in n:
    g = n[u]
    if g.isdigit():
        if n[u+1] == 'февраля' or 'января' or 'октября' or 'марта' or 'апреля' or 'мая' or 'июня' or 'июля' or 'агуста' or 'сентября' or 'ноября' or 'декабря':
            MESSAGE['Date']['Month'] = months(n[u + 1])
            MESSAGE['Date']['Day'] = g
            if (int(months(n[u+1]))-int(now_mnt)) >= 0:
                day_year = str(date.today())
                day_year = day_year.split('-')
                MESSAGE['Date']['Year'] = day_year[0]
            elif (int(months(n[u+1]))-int(now_mnt)) < 0:
                day_year = str(date.today() + timedelta(days=365))
                day_year = day_year.split('-')
                MESSAGE['Date']['Year'] = day_year[0]
            if (MESSAGE["Date"]["Hour"] == None) and (MESSAGE["Date"]["Minute"] == None):

                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = current_time[0]
                MESSAGE["Date"]["Minute"] = current_time[1]
            t = n.remove(n[u + 1])
    u = u + 1




j = 0
if ('числа' in n) or ('числу' in n) or ('число' in n):
    for i in n:
        g = n[j]
        if g.isdigit() == True:
            MESSAGE['Date']['Day'] = n[j]
            day_year = str(date.today())
            day_year = day_year.split('-')
            MESSAGE['Date']['Year'] = day_year[0]
            if (int(now_day) - int(n[j])) >= 0:
                true_months = int(now_mnt) + 1
                MESSAGE['Date']['Month'] = true_months
            elif (int(now_day) - int(n[j])) < 0:
                MESSAGE['Date']['Month'] = now_mnt
        j = j + 1
if ('завтра' in n) or ('tomorrow' in n):
    tomorrow = str((date.today() + timedelta(days=1)))
    tomorrow = tomorrow.split('-')
    MESSAGE['Date']['Year'] = tomorrow[0]
    MESSAGE['Date']['Month'] = tomorrow[1]
    MESSAGE['Date']['Day'] = tomorrow[2]
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    current_time = current_time.split(':')
    MESSAGE["Date"]["Hour"] = current_time[0]
    MESSAGE["Date"]["Minute"] = current_time[1]
    t = n.remove('завтра')

elif ('послезавтра'in n) or ('aftertomorrow' in n):
    from datetime import date, timedelta, datetime
    tomorrow = str((date.today() + timedelta(days=2)))
    tomorrow = tomorrow.split('-')
    MESSAGE['Date']['Year'] = tomorrow[0]
    MESSAGE['Date']['Month'] = tomorrow[1]
    MESSAGE['Date']['Day'] = tomorrow[2]
    text_i = text_i.split('послезавтра')
    text_message = text_i[0]
    MESSAGE['TEXT'] = text_message
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    current_time = current_time.split(':')
    MESSAGE["Date"]["Hour"] = current_time[0]
    MESSAGE["Date"]["Minute"] = current_time[1]
    t = n.remove('послезавтра')


elif ('через' in n) or ('следующей' in n) or ('следующий' in n):
    if ('дня' in text_i) or ('дней' in text_i):
        u = 0
        for i in n:

            g = n[u]
            if g.isdigit():
                now_time = str(date.today())
                now_time = now_time.split('-')
                MESSAGE['Date']['Year'] = now_time[0]
                MESSAGE['Date']['Month'] = now_time[1]
                MESSAGE['Date']['Day'] = int(now_time[2]) + int(g)
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = current_time[0]
                MESSAGE["Date"]["Minute"] = current_time[1]

            u = u + 1



    if ('неделю' in n):
        next_week = str((date.today() + timedelta(days=7)))
        next_week = next_week.split('-')
        MESSAGE['Date']['Year'] = next_week[0]
        MESSAGE['Date']['Month'] = next_week[1]
        MESSAGE['Date']['Day'] = next_week[2]
        now = datetime.now()
        current_time = str(now.strftime("%H:%M:%S"))
        current_time = current_time.split(':')
        MESSAGE["Date"]["Hour"] = current_time[0]
        MESSAGE["Date"]["Minute"] = current_time[1]
        t = n.remove('неделю')
        text_vivod(n)

    if ('недели' in n):
        u = 0
        for i in n:

            g = n[u]
            if g.isdigit() == True:
                next_some_hour = str(date.today())
                next_some_hour = next_some_hour.split('-')
                MESSAGE['Date']['Year'] = next_some_hour[0]
                MESSAGE['Date']['Month'] = next_some_hour[1]
                MESSAGE['Date']['Day'] = int(next_some_hour[2])+(int(g)*7)
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = current_time[0]
                MESSAGE["Date"]["Minute"] = current_time[1]

            u = u + 1
        if 'недели' in n:
            t = n.remove('недели')

        text_vivod(n)



    if ('час' in n) or ('60 минут' in n):

        next_hour = str(date.today())
        next_hour = next_hour.split('-')
        MESSAGE['Date']['Year'] = next_hour[0]
        MESSAGE['Date']['Month'] = next_hour[1]
        MESSAGE['Date']['Day'] = next_hour[2]
        now = datetime.now()
        current_time = str(now.strftime("%H:%M:%S"))
        current_time = current_time.split(':')
        MESSAGE["Date"]["Hour"] = int(current_time[0])+1
        MESSAGE["Date"]["Minute"] = current_time[1]
        if 'час' in n:
            t = n.remove('час')
        if '60 минут' in n:
            t = n.remove('60 минут')
        text_vivod(n)
    if ('год' in text_i) or ('года' in text_i):
        u = 0
        for i in n:

            g = n[u]
            if g.isdigit() == True:
                next_some_hour = str((date.today() + timedelta(days=(365)*int(g))))
                next_some_hour = next_some_hour.split('-')
                MESSAGE['Date']['Year'] = int(next_some_hour[0])
                MESSAGE['Date']['Month'] = next_some_hour[1]
                MESSAGE['Date']['Day'] = int(next_some_hour[2])
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = current_time[0]
                MESSAGE["Date"]["Minute"] = current_time[1]

            u = u + 1

        if 'год' in n:
            t = n.remove('год')
        if 'года' in n:
            t = n.remove('года')
        text_vivod(n)
    if ('часа' in text_i) or ('часов' in text_i):
        u = 0
        for i in n:

            g = n[u]
            if g.isdigit() == True:
                next_some_hour = str(date.today())
                next_some_hour = next_some_hour.split('-')
                MESSAGE['Date']['Year'] = next_some_hour[0]
                MESSAGE['Date']['Month'] = next_some_hour[1]
                MESSAGE['Date']['Day'] = next_some_hour[2]
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = int(current_time[0]) + int(g)
                MESSAGE["Date"]["Minute"] = current_time[1]

            u = u + 1
        if 'часа' in n:
            t = n.remove('часа')
        if 'часов' in n:
            t = n.remove('часов')
        text_vivod(n)

    elif ('минуты' in text_i) or ('минут' in text_i):
        u = 0
        for i in n:

            g = n[u]
            if g.isdigit() == True:
                now_time = str(date.today())
                now_time = now_time.split('-')
                MESSAGE['Date']['Year'] = now_time[0]
                MESSAGE['Date']['Month'] = now_time[1]
                MESSAGE['Date']['Day'] = now_time[2]
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = int(current_time[0])
                MESSAGE["Date"]["Minute"] = int(current_time[1]) + int(g)
                t = n.remove(g)
            u = u + 1
        if 'минуты' in n:
            t = n.remove('минуты')
        if 'минут' in n:
            t = n.remove('минут')
        text_vivod(n)
    t = n.remove('через')

if ('утром' in n) or ('утрам' in n) or ('утра' in n):
    utro()
if ('вечером' in n) or ('вечера' in n):
    vecher()
if ('дня' in n) or ('днем' in n) or ('днём' in n):
    denb()
if ":" in text_i:
    if (MESSAGE['Date']['Day'] == None):

        next_hour = str(date.today())
        next_hour = next_hour.split('-')
        MESSAGE['Date']['Year'] = next_hour[0]
        MESSAGE['Date']['Month'] = next_hour[1]
        MESSAGE['Date']['Day'] = next_hour[2]

    mins = text_i
    print(mins)
    ind = mins.index(':')
    hours_1 = (mins.index(':')-2)
    hours_2 = (mins.index(':')-1)
    hours = str(mins[hours_1]) + str(mins[hours_2])
    minutes = str(mins.split(':')[1])
    MESSAGE['Date']['Hour']= hours
    MESSAGE['Date']['Minute'] = minutes

if (MESSAGE['Date']['Day'] == None):
    MESSAGE['Status'] == 'Failure'

if ('каждый' in n) or ('каждую' in n) or ('каждые' in n) or ('каждое' in n) or ('по' in n):

    if ('пятница' in text_i) or ('Friday' in text_i) or ('пятницу' in text_i) or ('пятницам' in text_i):

        MESSAGE['Params']['Day_of_week'] = 'Friday'
        MESSAGE['Params']['Repeat_always'] = 'Every Friday'
        week_opred(n)
        if 'пятницам' in n:
            t = n.remove('пятницам')
        if 'пятницу' in n:
            t = n.remove('пятницу')
        text_vivod(n)
    if ('понедельник' in text_i) or ('Monday' in text_i) or ('понедельникам' in text_i):

        MESSAGE['Params']['Repeat_always'] = 'Every Monday'
        MESSAGE['Params']['Day_of_week'] = 'Monday'
        week_opred(n)
        if 'понедельник' in n:
            t = n.remove('понедельник')
        if 'понедельникам' in n:
            t = n.remove('понедельникам')
        text_vivod(n)
    if ('вторник' in text_i) or ('Tuesday' in text_i) or ('вторникам' in text_i):
        MESSAGE['Params']['Day_of_week'] = 'Tuesday'
        MESSAGE['Params']['Repeat_always'] = 'Every Tuesday'
        week_opred(n)
        if 'вторник' in n:
            t = n.remove('вторник')
        if 'вторникам' in n:
            t = n.remove('вторникам')
        text_vivod(n)
    if ('среда' in text_i) or ('среду' in text_i) or ('Wednesday' in text_i) or ('средам' in text_i):

        MESSAGE['Params']['Day_of_week'] = 'Wednesday'
        MESSAGE['Params']['Repeat_always'] = 'Every Wednesday'
        week_opred(n)
        if 'среду' in n:
            t = n.remove('среду')
        if 'средам' in n:
            t = n.remove('средам')
        text_vivod(n)
    if ('четверг' in text_i) or ('Thursday' in text_i) or ('четвергам' in text_i):

        MESSAGE['Params']['Day_of_week'] = 'Thursday'
        MESSAGE['Params']['Repeat_always'] = 'Every Thursday'
        week_opred(n)
        if 'четверг' in n:
            t = n.remove('четверг')
        if 'четвергам' in n:
            t = n.remove('четвергам')
        text_vivod(n)
    if ('суббота' in text_i) or ('субботу' in text_i) or ('Saturday' in text_i) or ('субботам' in text_i):


        MESSAGE['Params']['Day_of_week'] = 'Saturday'
        MESSAGE['Params']['Repeat_always'] = 'Every Saturday'
        week_opred(n)
        if 'субботу' in n:
            t = n.remove('субботу')
        if 'субботам' in n:
            t = n.remove('субботам')
        text_vivod(n)

    if ('воскресенье' in text_i) or ('Sunday' in text_i) or ('воскресеньям' in text_i):

        MESSAGE['Params']['Day_of_week'] = 'Sunday'
        MESSAGE['Params']['Repeat_always'] = 'Every Sunday'
        week_opred(n)
        if 'воскресенье' in n:
            t = n.remove('воскресенье')
        if 'воскресеньям' in n:
            t = n.remove('воскресеньям')
        text_vivod(n)
    if ('год' in text_i):
        MESSAGE['Params']['Repeat_always'] = 'Every year'

        if 'год' in n:
            t = n.remove('год')
        text_vivod(n)

    if ('день' in text_i):

        MESSAGE['Params']['Repeat_always'] = 'Every day'
        next_some_hour = str(date.today())
        next_some_hour = next_some_hour.split('-')
        MESSAGE['Date']['Year'] = next_some_hour[0]
        MESSAGE['Date']['Month'] = next_some_hour[1]
        MESSAGE['Date']['Day'] = next_some_hour[2]
        now = datetime.now()
        current_time = str(now.strftime("%H:%M:%S"))
        current_time = current_time.split(':')
        MESSAGE["Date"]["Hour"] = current_time[0]
        MESSAGE["Date"]["Minute"] = current_time[1]
        if 'день' in n:
            t = n.remove('день')
        text_vivod(n)

    if ('утром' in text_i) or ('утрам' in text_i) or ('утра' in text_i):
        utro()
        if 'утрам' in n:
            t = n.remove('утрам')
        if 'утро' in n:
            t = n.remove('утро')
        text_vivod(n)
        MESSAGE['Params']['Repeat_always'] = 'Every day'
    if ('вечер' in text_i) or ('вечерам' in text_i):
        vecher()
        MESSAGE['Params']['Repeat_always'] = 'Every day'
        if 'вечерам' in n:
            t = n.remove('вечерам')
        if 'вечер' in n:
            t = n.remove('вечер')
        text_vivod(n)

    if ('дня' in text_i) or ('дней' in text_i):
        u = 0
        MESSAGE['Params']['Repeat_always'] = 'Every day'
        for i in n:

            g = n[u]
            if g.isdigit():
                now_time = str(date.today())
                now_time = now_time.split('-')
                MESSAGE['Date']['Year'] = now_time[0]
                MESSAGE['Date']['Month'] = now_time[1]
                MESSAGE['Date']['Day'] = int(now_time[2]) + int(g)
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = current_time[0]
                MESSAGE["Date"]["Minute"] = current_time[1]

            u = u + 1

        next_year = str(date.today())
        next_year = next_year.split('-')
        MESSAGE['Date']['Year'] = int(next_year[0])
        MESSAGE['Date']['Month'] = next_year[1]
        MESSAGE['Date']['Day'] = next_year[2]
        now = datetime.now()
        current_time = str(now.strftime("%H:%M:%S"))
        current_time = current_time.split(':')
        MESSAGE["Date"]["Hour"] = current_time[0]
        MESSAGE["Date"]["Minute"] = current_time[1]
    if ('часа' in text_i) or ('часов' in text_i):
        MESSAGE['Params']['Repeat_always'] = 'Every a few hour'
        u = 0
        for i in n:
            g = n[u]
            if g.isdigit() == True:
                next_some_hour = str(date.today())
                next_some_hour = next_some_hour.split('-')
                MESSAGE['Date']['Year'] = next_some_hour[0]
                MESSAGE['Date']['Month'] = next_some_hour[1]
                MESSAGE['Date']['Day'] = next_some_hour[2]
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = int(current_time[0]) + int(g)
                MESSAGE["Date"]["Minute"] = current_time[1]

            u = u + 1
        if 'часа' in n:
            t = n.remove('часа')
        if 'часов' in n:
            t = n.remove('часов')
        text_vivod(n)
    if ('час' in n):
        MESSAGE['Params']['Repeat_always'] = 'Every hour'

        next_year = str(date.today())
        next_year = next_year.split('-')
        MESSAGE['Date']['Year'] = int(next_year[0])
        MESSAGE['Date']['Month'] = next_year[1]
        MESSAGE['Date']['Day'] = next_year[2]
        now = datetime.now()
        current_time = str(now.strftime("%H:%M:%S"))
        current_time = current_time.split(':')
        MESSAGE["Date"]["Hour"] = current_time[0]
        MESSAGE["Date"]["Minute"] = current_time[1]
        if 'час' in n:
            t = n.remove('час')

        text_vivod(n)
    if ('число' in text_i):
        MESSAGE['Params']['Repeat_always'] = 'Every this day of the month'
        u = 0
        for i in n:
            g = n[u]
            if g.isdigit() == True:
                next_some_hour = str(date.today())
                next_some_hour = next_some_hour.split('-')
                MESSAGE['Date']['Year'] = next_some_hour[0]
                MESSAGE['Date']['Month'] = next_some_hour[1]
                MESSAGE['Date']['Day'] = g
                now = datetime.now()
                current_time = str(now.strftime("%H:%M:%S"))
                current_time = current_time.split(':')
                MESSAGE["Date"]["Hour"] = int(current_time[0])
                MESSAGE["Date"]["Minute"] = current_time[1]

            u = u + 1

        if 'число' in n:
            t = n.remove('число')
        text_vivod(n)

    if 'каждое' in n:
        t = n.remove('каждое')
    text_vivod(n)
    if 'каждый' in n:
        t = n.remove('каждый')
    text_vivod(n)
    if 'каждую' in n:
        t = n.remove('каждую')
    text_vivod(n)
    if 'по' in n:
        t = n.remove('по')
    text_vivod(n)
    if 'каждые' in n:
        t = n.remove('каждые')
    text_vivod(n)

    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    current_time = current_time.split(':')
    MESSAGE["Date"]["Hour"] = current_time[0]
    MESSAGE["Date"]["Minute"] = current_time[1]


if ":" in text_i:
    if (MESSAGE['Date']['Day'] == None):
        next_hour = str(date.today())
        next_hour = next_hour.split('-')
        MESSAGE['Date']['Year'] = next_hour[0]
        MESSAGE['Date']['Month'] = next_hour[1]
        MESSAGE['Date']['Day'] = next_hour[2]
    mins = text_i
    ind = mins.index(':')
    hours_1 = (mins.index(':')-2)
    hours_2 = (mins.index(':')-1)
    hours = str(mins[hours_1]) + str(mins[hours_2])
    minutes = str(mins.split(':')[1])
    MESSAGE['Date']['Hour']= hours
    MESSAGE['Date']['Minute'] = minutes
    text_i = text_i.split('в')
    text_message = text_i[0]
    MESSAGE['TEXT'] = text_message

day_of_week = 'Wednesday or Thursday or Friday'
if (' на неделе' in text_i):
    MESSAGE['Params']['Day_of_week'] = day_of_week
    next_hour = str(date.today())
    next_hour = next_hour.split('-')
    MESSAGE['Date']['Year'] = next_hour[0]
    MESSAGE['Date']['Month'] = next_hour[1]
    MESSAGE['Date']['Day'] = next_hour[2]
    time_vsegda()
    t = n.remove('неделе')
    t = n.remove('на')





cifra = 0
o = 0
for i in n:
    cifra = n[o]
    if cifra.isdigit():
        t = n.remove(cifra)
    o = o + 1


text_vivod(n)
check()
print(MESSAGE)
