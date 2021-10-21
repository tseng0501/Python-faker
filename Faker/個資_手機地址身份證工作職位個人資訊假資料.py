from faker import Faker

fake = Faker('zh_TW')

print(fake.language_name())
# Turkmen
print(fake.country_calling_code())
# +290 8
print(fake.phone_number())
# 0977-739186
print(fake.ssn())
# D169226625
print(fake.job())
# 工業設計

print(fake.simple_profile())
# {'username': 'sfang', 'name': '李雅文', 'sex': 'M', 'address': '42346 板橋縣民有路310號之3', 'mail': 'xiuyingxue@gmail.com', 'birthdate': datetime.date(1936, 2, 13)}
