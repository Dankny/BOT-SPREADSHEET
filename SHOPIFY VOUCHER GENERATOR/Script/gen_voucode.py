import string
import random

# voucher id code generator
def id_generator(size_letters=4, size_num=2, letters=string.ascii_uppercase, num=string.digits):
    letters = ''.join(random.choice(letters) for _ in range(size_letters))
    nums = ''.join(random.choice(num) for _ in range(size_num))
    return letters + nums

# print all the id codes and manual copy the id codes for data source in spreadsheet
for i in range(0, 100):
    print(id_generator())