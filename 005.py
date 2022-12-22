# given a string and a number k which is a factor of the string's length, print the unique characters of each substring of k chars

def merge_the_tools(string, k):
    parts = [string[i:i+k] for i in range(0, len(string), k)] # 'AABCAAADA' --> ['AAB','CAA','ADA']
    for part in parts:
        print(''.join(set(part)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)