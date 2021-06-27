n = int(input())
words = [ input() for _ in range(n)]
words = set(words)
words = sorted(words, key=lambda x : (len(x), x))
[print(word) for word in words]