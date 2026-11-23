# CodeChef: Chef and String (XYSTR)
# Student: Anurag Banik (Roll: 2026ABES042)

def solve(s: str) -> int:
    pairs = 0
    i = 0
    while i < len(s) - 1:
        if (s[i] == 'x' and s[i+1] == 'y') or (s[i] == 'y' and s[i+1] == 'x'):
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs

if __name__ == '__main__':
    print('Chef and String Test:', solve('xyxxy')) # Expected: 2
