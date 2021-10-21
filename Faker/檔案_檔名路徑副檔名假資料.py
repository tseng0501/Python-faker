from faker import Faker

fake = Faker()

print(fake.file_extension(category='image'))
# jpeg
print(fake.file_name())
# central.png
print(fake.file_path(depth=3))
# /suggest/project/worry/grow.avi
print(fake.unix_device())
# /dev/sdg
