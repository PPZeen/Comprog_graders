def read_date() :
    mname = [0,"Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    d,m,y = [e for e in input().split()]
    if m in mname : m = mname.index(m)
    d = int(d) ; y = int(y)
    return [d,m,y]
    
def zodiac(d1,m1) :
    if d1 >= 22 and m1==3 or d1 <=21 and m1==4 : z1 = "Aries"
    elif d1 >= 22 and m1==4 or d1 <=21 and m1==5 : z1 = "Taurus"
    elif d1 >= 22 and m1==5 or d1 <=21 and m1==6 : z1 = "Gemini"
    elif d1 >= 22 and m1==6 or d1 <=21 and m1==7 : z1 = "Cancer"
    elif d1 >= 22 and m1==7 or d1 <=21 and m1==8 : z1 = "Leo"
    elif d1 >= 22 and m1==8 or d1 <=21 and m1==9 : z1 = "Virgo"
    elif d1 >= 22 and m1==9 or d1 <=21 and m1==10 : z1 = "Libra"
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 : z1 = "Scorpio"
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 : z1 = "Sagittarius"
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1 : z1 = "Capricorn"
    elif d1 >= 21 and m1==1 or d1 <=20 and m1==2 : z1 = "Aquarius"
    elif d1 >= 21 and m1==2 or d1 <=21 and m1==3 : z1 = "Pisces"
    return z1
    
def days_in_feb(y) :
    if y % 400 == 0 or y % 100 != 0 and y%4 == 0 :
        return 29
    return 28
    
def days_in_month(m,y) :
    if m == 2 : return days_in_feb(y)
    elif m in [4,6,9,11] : return 30
    return 31
    
def days_in_between(d1,m1,y1,d2,m2,y2) :
    days = 0
    if m1 < 12 : days += 31
    if m1 < 11 : days += 30
    if m1 < 10 : days += 31
    if m1 < 9 : days += 30
    if m1 < 8 : days += 31
    if m1 < 7 : days += 31
    if m1 < 6 : days += 30
    if m1 < 5 : days += 31
    if m1 < 4 : days += 30
    if m1 < 3 : days += 31
    if m1 < 2 : days += days_in_feb(y1)
    if m2 > 1 : days += 31
    if m2 > 2 : days += days_in_feb(y2)
    if m2 > 3 : days += 31
    if m2 > 4 : days += 30
    if m2 > 5 : days += 31
    if m2 > 6 : days += 30
    if m2 > 7 : days += 31
    if m2 > 8 : days += 31
    if m2 > 9 : days += 30
    if m2 > 10 : days += 31
    if m2 > 11 : days += 30
    days += (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days
    
def main() :
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    z1 = zodiac(d1,m1)
    z2 = zodiac(d2,m2)
    days_all = days_in_between(d1,m1,y1,d2,m2,y2)
    print(z1,z2)
    print(days_all)
    
print(zodiac(2,9))
print(days_in_feb(2016))
print(days_in_month(2,2017))
print(days_in_between(1,1,2016, 1,1,2017))
main()

exec(input().strip())