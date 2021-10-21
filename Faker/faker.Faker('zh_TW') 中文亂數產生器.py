from faker import Faker

fake = Faker('zh_TW')

print(fake.name())
# 袁家銘
print(fake.name_female())  # 女生人名
# 莫怡萱
print(fake.name_male())    # 男生人名
# 孫威廷
print(fake.romanized_name())  # 羅馬拼音
# Ping Long

print(fake.last_name())
# 楊
print(fake.last_name_female())
# 李
print(fake.last_name_male())
# 黃
print(fake.last_romanized_name())
# Lin

print(fake.first_name())
# 家豪
print(fake.first_name_female())
# 惠雯
print(fake.first_name_male())
# 冠霖
print(fake.first_romanized_name())
# Jing
