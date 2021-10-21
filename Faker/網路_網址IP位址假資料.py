from faker import Faker

fake = Faker('zh_TW')

print(fake.company_email())
# dmeng@zou.com
print(fake.domain_name())
# tang.com
print(fake.domain_word())
# gao
print(fake.email())
# slei@gmail.com
print(fake.free_email())
# mliu@hotmail.com
print(fake.free_email_domain())
# yahoo.com
print(fake.hostname())
# desktop-15.wan.com
print(fake.http_method())
# POST
print(fake.image_url())
# https://placeimg.com/431/555/any
print(fake.ipv4())
# 28.144.124.103
print(fake.ipv4_network_class())
# c
print(fake.ipv4_private())
# 192.168.96.99
print(fake.ipv4_public())
# 75.81.186.65
print(fake.mac_address())
# d2:3c:7b:3b:93:4f
print(fake.uri())
# http://fu.com/wp-content/categories/main/index/
print(fake.uri_extension())
# .php
print(fake.uri_page())
# search
print(fake.url())
# http://qiao.com/
print(fake.user_name())
# mingyan
