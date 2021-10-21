from faker import Faker

fake = Faker('zh_TW')

print(fake.color())
# #6626ef
print(fake.color(hue='red'))
# #ed6595
print(fake.color(hue=(100, 200), color_format='rgb'))
# rgb(36, 181, 79)
print(fake.color(hue=135, luminosity='dark', color_format='hsv'))
# hsv(135, 95, 65)
print(fake.color_name())
# DarkMagenta
print(fake.hex_color())
# #dd5cbb
print(fake.rgb_color())
# 35,232,144
