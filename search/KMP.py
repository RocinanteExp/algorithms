import sys

def build_kmp_table(pattern):
    table = [0] * len(pattern)
    i = 1
    mismatch_index = 0

    while i < len(pattern):
        #
        if pattern[i] == pattern[mismatch_index]:
            mismatch_index += 1
            table[i] = mismatch_index
            i += 1
        elif mismatch_index != 0:
            mismatch_index = table[mismatch_index - 1]
        else:
            table[i] = 0
            i += 1

    return table

def kmp_search(text, pattern):
    table = build_kmp_table(pattern)
    index_text = 0
    index_pattern = 0
    while index_text < len(text):
        if text[index_text] != pattern[index_pattern]:
            if index_pattern == 0:
                index_text += 1
            else:
                index_pattern = table[index_pattern - 1]
        else:
            index_text += 1
            index_pattern += 1
            if index_pattern == len(pattern):
                print(f"pattern '{pattern}' found at {str(index_text - index_pattern)}")
                index_pattern = table[index_pattern - 1]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: python {sys.argv[0]} <text> <pattern>')
        sys.exit()

    kmp_search(sys.argv[1], sys.argv[2])
