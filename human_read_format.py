def human_read_format(bytes):
    if bytes >= 1_024 ** 3:
        return f'{round(bytes / (1_024 ** 3))}ГБ'
    elif bytes >= 1_024 ** 2:
        return f'{round(bytes / (1_024 ** 2))}МБ'
    elif bytes >= 1_024:
        return f'{round(bytes / 1_024)}КБ'
    else:
        return f'{bytes}Б'


# print(human_read_format(1023))
# print(human_read_format(15000))

print(len('There are different programming paradigms.') * 8)
