start_year = 1901
end_year = 2000
months = [31,28,31,30,31,30,31,31,30,31,30,31]
total = []


def is_leap_year(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)
 
def start_day(months,first_day):
    start_day_list = []
    start_day_list.append(first_day)
    for month in months:
        day = month % 7
        first_day += day 
        if first_day >= 7:
            first_day %= 7
        start_day_list.append(first_day)
    return start_day_list
        
    
if __name__=='__main__':
    year_list = []
    day = 2
    count = 0
    for year in range(start_year,end_year+1):
        if is_leap_year(year):
            months[1] = 29
        else :
            months[1] = 28
        year_list = start_day(months,day)
        day = year_list.pop()
        total.append(year_list)
        for year in year_list:
            if year == 0:
                count+=1
                
    print(count)
        
            
        