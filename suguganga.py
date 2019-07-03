def leapyear(year, querytype='is'):
    import calendar
    querytype == case(querytype, 'lowercase')
    if querytype == 'is':
        return calendar.isleap(year)
    elif querytype == 'closest':
        return year % 4
