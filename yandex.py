# class Snow:
#     def fall(self):
#         print('*', end='')
#
#
# s = Snow()
# s.fall()
# s.fall()
# s.fall()


# class Fallout:
#     def snow(self):
#         print('*', end='')
#
#     def rain(self):
#         print('o', end='')
#
# s = Fallout()
# s.snow()
# s.rain()
# s.snow()
# s.rain()
# s.snow()


# class Controller:
#     # def __init__(self):
#     #     self.channel_number = 1
#     #
#     # def click(self):
#     #     if self.channel_number < 5:
#     #         self.channel_number += 1
#     #     else:
#     #         self.channel_number = 1
#     #
#     # def channel(self):
#     #     return self.channel_number
#     channel = 1
#
#     def click(self):
#         self.channel += 1
#         if self.channel > 5:
#             self.channel = 1
#
#
# c = Controller()
# c.click()
# c.click()
# print(c.channel)
# c.click()
# c.click()
# print(c.channel)


# class Rainbow:
#     def __init__(self, rainbow=1):
#         if rainbow == 2:
#             self.colors_rainbow = ['violet', 'blue', 'light blue', 'green', 'yellow', 'orange', 'red', 'violet']
#         else:
#             self.colors_rainbow = ['red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'violet', 'red']
#
#     def next_color(self, color):
#         return self.colors_rainbow[(self.colors_rainbow.index(color) + 1) % 8]
#
#
# rb = Rainbow(2)
# print(rb.next_color('red'))
#
# rb = Rainbow(1)
# print(rb.next_color('violet'))
#
# rb = Rainbow()
# print(rb.next_color('light blue'))

# class JamesWebb:
#     def __init__(self, data):
#         self.data = data
#
#
#     def brightest_star(self):
#         pass
#
#
#     def brightest_galaxy(self):
#         pass
#
#
#     def stars(self):
#         pass
#
#
#     def galaxies(self):
#         pass
#
#
#     def voids(self):
#         pass
#
#     pass
#
#
# data = [[0, 0, 1, 2],
#         [3, 1, -1, -1],
#         [0, 3, -1, 0]]
# jw = JamesWebb(data)
# print(jw.brightest_star())
# print(jw.brightest_galaxy())
# print(jw.stars())
# print(jw.galaxies())
# print(jw.voids())

from itertools import product

chet = '2468'
nechet = '1357'
k = 0
for i in product(chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet):
    a = ''.join(i)
    if a.count('1') > 4 or a.count('2') > 4 or a.count('3') > 4 or a.count('4') > 4:
        continue
    if a.count('5') > 4 or a.count('6') > 4 or a.count('7') > 4 or a.count('8') > 4:
        continue
    k += 1
print(k * 2)
