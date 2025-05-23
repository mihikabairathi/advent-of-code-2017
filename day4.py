def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def valid_passphrase(passphrase):
    word_set = set()
    for word in passphrase.split():
        if word in word_set:
            return False
        else:
            # Check for anagrams
            for word_present in word_set:
                if set(word) == set(word_present):
                    return False

            word_set.add(word)
    return True

def valid_passphrases(filename):
    passphrases = read_file(filename)
    valid_count = 0
    for passphrase in passphrases.splitlines():
        if valid_passphrase(passphrase):
            valid_count += 1

    return valid_count

if __name__ == "__main__":
    print(valid_passphrases("day4.txt"))