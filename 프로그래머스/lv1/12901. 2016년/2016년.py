def solution(a, b):
    weekday = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b
    for x in range(1,a):
        day+=month[x]
    return weekday[day%7]