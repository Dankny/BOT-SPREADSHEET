import random

# SIMCard Prefix in Indonesia
no_hp_xl = '0877'
no_hp_xl2 = '0818'
no_hp_xl3 = '0819'
no_hp_xl4 = '0859'
no_hp_im3 = '0856'
no_hp_im3_2 = '0857'
no_hp_im3_3 = '0858'
no_hp_simpati = '0821'
no_hp_simpati2 = '0822'
no_hp_simpati3 = '0811'
no_hp_simpati4 = '0813'
no_hp_byu = '0851'
no_hp_kartuAs = '0852'
no_hp_axis = '0838'
no_hp_axis2 = '0832'
no_hp_axis3 = '0831'



provider = [no_hp_byu, no_hp_kartuAs, no_hp_axis, no_hp_axis2, no_hp_axis3,
            no_hp_simpati, no_hp_simpati2, no_hp_simpati3, no_hp_simpati4, no_hp_xl, 
            no_hp_xl2, no_hp_xl3, no_hp_xl4, no_hp_im3, no_hp_im3_2, no_hp_im3_3]
# Shuffle all the prefix
random.shuffle(provider)

# Combine the prefix with number generator (4 digits for prefix and another 
# 8 digits to complete the phone number)
for i in range(0, 530):
    random.shuffle(provider)
    temp = provider[0] + str(random.randint(10000000, 99999999))
    print(temp)
    