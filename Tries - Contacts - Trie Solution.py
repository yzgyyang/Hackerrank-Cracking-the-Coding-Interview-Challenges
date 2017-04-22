def trie_insert(s, t):
    if '_' not in t:
        t['_'] = 0
    t['_'] += 1
    if len(s) == 0:
        return
    if s[0] not in t:
        t[s[0]] = {}
    trie_insert(s[1:], t[s[0]])


def trie_find(s, t):
    if len(s) == 0:
        return t
    if s[0] not in t:
        return {}
    return trie_find(s[1:], t[s[0]])


n = int(raw_input().strip())
trie = {}

for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == "add":
        trie_insert(contact, trie)
    elif op == "find":
        t = trie_find(contact, trie)
        if t == {}:
            print 0
        else:
            print t['_']
