from faker import Faker

fake = Faker('zh_TW')

print(fake.address())
# 30751 基隆市仁愛街93號6樓
print(fake.building_number())
# 4號
print(fake.city())
# 卑南縣
print(fake.city_name())
# 草屯
print(fake.city_name_suffix())
# 縣
print(fake.country())
# 俄羅斯
print(fake.country_code())
# LT
print(fake.postcode())
# 824
print(fake.secondary_address())
# 之2
print(fake.street_address())
# 自由街759號
print(fake.street_name())
# 信義
print(fake.street_name_suffix())
# 路
