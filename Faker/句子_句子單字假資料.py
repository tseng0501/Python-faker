from faker import Faker

fake = Faker('zh_TW')

print(fake.sentence())
# 發生服務選擇人民游戲然后一下法律.
print(fake.sentences())
# ['發現密碼地區那個精華制作.', '擁有地方手機所有.', '業務決定地址經濟投資方式.']
print(fake.text(max_nb_chars=15))
# 基本主要研究根據一種當然各種.
print(fake.word())
# 關於
print(fake.words())
# ['一種', '電影', '大學']
