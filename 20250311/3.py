#create a list fill wuth weekdays from Monday to Sunday
#weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#rint(weekdays)
#create a list fill with Months from January to December
#months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#print(months)
#創建一個十二生肖的list
#zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
#print(zodiacs)

#創建一個農民歷萬年曆list，使用者輸入西元年月日可以顯示該日期是農曆幾年?該年的生肖?和星期
import datetime
from lunarcalendar import Converter, Solar, Lunar

# 創建一個星期列表
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 創建一個十二生肖列表
zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

# 輸入西元年月日
year = int(input('Enter the year: '))
month = int(input('Enter the month: '))
day = int(input('Enter the day: '))

# 輸入的日期
input_date = f'{year}/{month}/{day}'

# 輸入日期的星期
input_weekday = weekdays[datetime.datetime(year, month, day).weekday()]

# 輸入日期的生肖
input_zodiac = zodiacs[(year - 4) % 12]

# 輸入日期的農曆年
def chinese_lunar(year, month, day):
    solar_date = Solar(year, month, day)
    lunar_date = Converter.Solar2Lunar(solar_date)
    return lunar_date

lunar_date = chinese_lunar(year, month, day)
print(f'The date {input_date} is Lunar Year: {lunar_date.year}, Month: {lunar_date.month}, Day: {lunar_date.day}, Zodiac: {input_zodiac}, Weekday: {input_weekday}')