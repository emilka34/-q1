import datetime as dt



class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records =[]
    
    def add_record(self, record):
        self.records.append(record)
        return self.records
    
    def today_remained(self):
        return self.limit - self.get_today_stats()
    
    def get_today_stats(self):
        count = 0
        if self.date == date.now:
            for self.amount in self.records:
                count += amount
            return count
date_now = dt.datetime.now().date()

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = date_now
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.today_remained >= self.limit:
            return f'Хватит есть!'
        else:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.today_remained} кКал'



class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            if self.get_today_stats() == self.limit:
                return 'Денег нет, держись'
            elif self.get_today_stats() < self.limit:
                return f'На сегодня осталось {self.today_remained()} руб'
            else:
                return f'Денег нет, держись: твой долг - {today_remained} руб'
        
cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
print(cash_calculator.get_today_cash_remained('rub'))