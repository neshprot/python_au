TEXT = "axaxaxax aaaxxxxax"
PATTERN = "xax"


def rabin_carp(text, pattern):
    result = []

    if len(text) >= len(pattern) > 0:
        pattern_sum = 0
        local_sum = 0
        for k, item in enumerate(pattern):
            pattern_sum += ord(item)
            local_sum += ord(text[k])
        for k in range(len(text) - len(pattern) + 1):
            if local_sum == pattern_sum:
                if text.startswith(pattern, k):
                    result.append(k)
            if k + len(pattern) < len(text):
                local_sum += ord(text[k + len(pattern)]) - ord(text[k])
            else:
                local_sum += ord(text[k - 1 + len(pattern)]) - ord(text[k])
    if len(pattern) == 0:
        for i in range(len(text)):
            result.append(i)
    return result


res = rabin_carp(TEXT, PATTERN)
print(res)
