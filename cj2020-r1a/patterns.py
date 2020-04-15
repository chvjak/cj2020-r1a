f = open("patterns3.txt")

import SuffixTrie

import sys
f = sys.stdin

def merge_asterisks(raw_pattern_list):
    res = []
    middles = ""
    for p in raw_pattern_list:
        groups = p.split("*")
        if len(groups) > 2:
            res += [groups[0] + "*" + groups[-1]]
            middles += "".join(groups[1:-1])
        else:
            res += [p]
    return res, middles 

def find_matching_string(raw_pattern_list):
    # solve for set 2 : only one *
    # aa*aa, *aa, aa*

    pattern_list, middles = merge_asterisks(raw_pattern_list)

    prefix_set = set()
    suffix_set = set()
    res = ""

    for ptrn in pattern_list:
        prefix, suffix = ptrn.split("*")
        if prefix:
            prefix_set.add(prefix)
        if suffix:
            suffix_set.add(suffix)

    if len(prefix_set):
        prefix_list = list(sorted(prefix_set, key=len, reverse=True))
        longest_pfx = prefix_list[0]
        for pfx in prefix_list[1:]:
            if longest_pfx.find(pfx) != 0:
                return "*"

        res += longest_pfx

    res += middles
    if len(suffix_set):
        suffix_list = list(sorted(suffix_set, key=len, reverse=True))
        longest_sffx = suffix_list[0]
        for sffx in suffix_list[1:]:
            if longest_sffx.rfind(sffx) != len(longest_sffx) - len(sffx):
                return "*"

        res += longest_sffx

    return res 

T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    pattern_list = []
    for n in range(N):
        raw_pattern = f.readline().strip()
        pattern = "*".join(raw_pattern.split("*"))      # remove duplicated *
        pattern_list +=  [pattern]

    res = find_matching_string(pattern_list)

    print("Case #{0}: {1}".format(t + 1, res))