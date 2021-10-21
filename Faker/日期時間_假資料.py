from faker import Faker

fake = Faker('zh_TW')

print(fake.am_pm())
# AM
print(fake.iso8601())
# 1988-07-01T02:40:03

print(fake.date())
# 1970-12-22
print(fake.date_object())
# datetime.date(2004, 3, 20)

print(fake.date_this_month(before_today=True, after_today=False))
# 2020-11-07
print(fake.day_of_month())
# 01
print(fake.day_of_week())
# Saturday
print(fake.month_name())
# April

print(fake.time())
# 02:46:38
print(fake.time_object())
# datetime.time(8, 43, 22)
print(fake.unix_time())
# 1429693221
