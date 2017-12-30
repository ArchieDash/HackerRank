n = int(input().strip())
print(len(max(bin(n)[2:].split('0'))))
