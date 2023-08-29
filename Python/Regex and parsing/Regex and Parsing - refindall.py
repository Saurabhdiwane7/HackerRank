# Q = https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import re

Storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)