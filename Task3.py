import timeit
import chardet
import pandas as pd


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    skip = {}
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip.get(text[k], m)
    return -1

def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

with open(r'C:\Users\Legion\Downloads\стаття 1.txt', 'rb') as file:
    raw_data = file.read()
    result1 = chardet.detect(raw_data)
    encoding1 = result1['encoding']

with open(r'C:\Users\Legion\Downloads\стаття 2.txt', 'rb') as file:
    raw_data = file.read()
    result2 = chardet.detect(raw_data)
    encoding2 = result2['encoding']

with open(r'C:\Users\Legion\Downloads\стаття 1.txt', 'r', encoding=encoding1) as file:
    text1 = file.read()

with open(r'C:\Users\Legion\Downloads\стаття 2.txt', 'r', encoding=encoding2) as file:
    text2 = file.read()


patterns = [
    ("алгоритм пошуку", "вигаданий підрядок"),
    ("рекомендаційна система", "незнайомий підрядок")
]

texts = [text1, text2]

results = []

for i, text in enumerate(texts):
    for pattern in patterns[i]:
        bm_time = timeit.timeit(lambda: boyer_moore(text, pattern), number=100)
        kmp_time = timeit.timeit(lambda: kmp_search(text, pattern), number=100)
        rk_time = timeit.timeit(lambda: rabin_karp(text, pattern), number=100)
        results.append({
            "text": f"text{i+1}",
            "pattern": pattern,
            "bm_time": bm_time,
            "kmp_time": kmp_time,
            "rk_time": rk_time
        })

df = pd.DataFrame(results)

print(df)


