# REF. https://faker.readthedocs.io/en/master/providers/baseprovider.html

from faker import Faker

fake = Faker()

product_number_str=fake.bothify(text='Product Number: ????-########')
print(product_number_str)

