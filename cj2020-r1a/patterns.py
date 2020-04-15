f = open("patterns1.txt")

# this is special trie which can't have branches
# but can have wildcards/asterisks sections
class PatternTrie:
    def __init__(self):
        self.data = []      

    def place(self, starting_pos, data):
         # consider subgroups - i.e C, CD
         # consider placement in * as well as among known letters
        self.data = self.data[:starting_pos] + data + self.data[starting_pos: ]

    def can_place(self, starting_pos, data):
        # if it is not the first group then it is preceeded by *, so it can start anywhere on or after starting_pos => ruining the whole sense of the trie
        # => a pattern should be an array of tries
        for p, t in enumerate(self.tries[starting_pos]):
            if t.found(data):
                return starting_pos + p # position of matching trie
        else:
            return starting_pos + 1     # position of next asterisk (if there is one)


def find_matching_string(patterns):
    for p in patterns:
        groups = p.split("*")       # A*CD*E = > A, {C&D|CD}, E are groups
        for g in groups:
            for tp in pattern_trie.positions():
                if pattern_trie.can_place(tp, g):
                    break
            else:
                return false # actually backtrack, revert the previous group placement and try next tp or even the whole previous pattern placement

            pattern_trie.place(tp, g)

    return ""

def try_applying_next_group(patterns, groups):
    if len(groups):
        #if group applies
            try_applying_next_group(patterns, groups[1:])
    else:
        return try_applying_next_pattern(patterns[1:])

def try_applying_next_pattern(patterns):
    if len(patterns):
        p = patterns[0]
        groups = p.split("*")       # A*CD*E = > A, {C&D|CD}, E are groups
        try_applying_next_group(groups)

def find_matching_string(patterns):
        return try_applying_next_pattern(patterns[1:])


T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    patterns = []
    for n in range(N):
        patterns +=  f.readline().strip()

    res = find_matching_string(patterns)

    print("Case #{1}: {2}".format(t + 1, res))