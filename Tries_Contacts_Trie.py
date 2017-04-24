def trie_insert(s, t):
    if len(s) == 0:
        t['_'] = '_'
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


def trie_count_node(t):
    if not isinstance(t, dict):
        return 0
    ans = 0
    if '_' in t:
        ans += 1
    for key, value in t.items():
        ans += trie_count_node(value)
    return ans


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
            print trie_count_node(t)
