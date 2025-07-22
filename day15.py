def get_lowest_16_binary(value):
    final_string = str(bin(value)[2:])
    if len(final_string) < 16:
        final_string = '0' * (16 - len(final_string)) + final_string

    return final_string[-16:]

def count_matches(gen1, gen2):
    count = 0
    for i in range(5000000):
        old_gen1 = gen1
        while gen1 % 4 != 0 or old_gen1 == gen1:
            gen1 = (gen1 * 16807) % 2147483647

        old_gen2 = gen2
        while gen2 % 8 != 0 or old_gen2 == gen2:
            gen2 = (gen2 * 48271) % 2147483647

        # Use bitwise operations instead of string conversion for performance
        # Get lowest 16 bits using bitwise AND with 0xFFFF (65535)
        if (gen1 & 0xFFFF) == (gen2 & 0xFFFF):
            count += 1

    return count

if __name__ == "__main__":
    print(count_matches(65, 8921))
