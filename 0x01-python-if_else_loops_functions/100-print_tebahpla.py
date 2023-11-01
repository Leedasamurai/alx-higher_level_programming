#!/usr/bin/python3

rev = 0
for r in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(r - rev)), end="")
    rev = 32 if rev == 0 else 0

print()
# in reverse order, alternating lowercase and uppercase 
