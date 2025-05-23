def sequence_of_digits_sum(s):
    result = 0
    for i in range(len(s)):
        if s[i] == s[(i+1) % len(s)]:
            result += int(s[i])

    return result

def sequence_of_digits_sum_halfway(s):
    result = 0
    for i in range(len(s)):
        if s[i] == s[(i + len(s)//2) % len(s)]:
            result += int(s[i])

    return result

if __name__ == "__main__":
    print(sequence_of_digits_sum("51629928149116951271")) 
    print(sequence_of_digits_sum_halfway("516299281491624428165295")) 
