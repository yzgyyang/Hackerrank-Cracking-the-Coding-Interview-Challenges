n = int(raw_input().strip())
s = set()
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == "add":
        s.add(contact)
    elif op == "find":
        count = 0
        for item in s:
            m = min(len(contact), len(item))
            if contact[:m] == item[:m]:
                count += 1
        print count
