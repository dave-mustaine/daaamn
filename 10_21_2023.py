# import math
#
# print(math.factorial(100))

import pymorphy2
# import re
#
TEXT = open('Понедельник_начинается_в_субботу.txt', 'r', encoding='utf-8')
#
s = list(re.sub(r'[^\w\s]', '', TEXT.read()).lower().split())
#
# # for word in words:
# #     word.lower()
#
# print(s)
#
# morph = pymorphy2.MorphAnalyzer(lang='ru')
# s = [morph.normal_forms(i)[0] for i in s if morph.parse(i)[0].tag.POS not in ('PREP', 'CONJ', 'PRCL', 'INTJ')]
#
# print(s)

# import random
#
# test_list = ["ff", "fF", "Ff", "Ff", "FF", "ff", "fF", "FF"]
#
# b, c = random.sample(test_list, 2)
#
# test_list.remove(b)
# test_list.remove(c)
#
# print(test_list)
