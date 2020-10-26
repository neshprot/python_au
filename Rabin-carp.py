t = """Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов."""
p = "Иван"


def find_all_rabin_karp(text, pattern):
    result = []
    patternsum = sum(ord(s) for s in pattern)
    for i in range(len(text) - len(pattern) + 1):
        textwindowsum = sum(ord(text[l + i]) for l in range(len(pattern)))
        if textwindowsum == patternsum:
            if text.startswith(pattern, i):
                result.append(i)
    return result
print(find_all_rabin_karp(t, p))