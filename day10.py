def create_knot(lengths, sequence, position, skip_size):
    for length in lengths:
        for i in range(length//2):
            sequence[(position + i) % len(sequence)], sequence[(position + length - 1 - i) % len(sequence)] = sequence[(position + length - 1 - i) % len(sequence)], sequence[(position + i) % len(sequence)]
        position = (position + length + skip_size) % len(sequence)
        skip_size += 1

    return sequence[0] * sequence[1], sequence, position, skip_size

def generate_lengths(s):
    # input ex: "1,2,3"
    return [ord(c) for c in s] + [17, 31, 73, 47, 23]

def create_sparse_hash(s):
    # input ex: "1,2,3"
    lengths = generate_lengths(s)
    sequence = [i for i in range(256)]
    position = 0
    skip_size = 0

    for i in range(64):
        _, sequence, position, skip_size = create_knot(lengths, sequence, position, skip_size)

    return sequence

def create_dense_hash(sparse_hash):
    dense_hash = []

    for i in range(0, 256, 16):
        block = sparse_hash[i:i+16]
        xor_result = block[0]
        for j in range(1, len(block)):
            xor_result = xor_result ^ block[j]
        dense_hash.append(xor_result)

    return dense_hash

def create_hash(length_string):
    sparse_hash = create_sparse_hash(length_string)
    dense_hash = create_dense_hash(sparse_hash)
    final_result = ""
    for num in dense_hash:
        hex_num = hex(num)[2:]
        if len(hex_num) == 1:
            hex_num = "0" + hex_num
        final_result += hex_num

    return final_result

if __name__ == "__main__":
    print(create_knot([3, 4, 1, 5], [0, 1, 2, 3, 4], 0, 0))
    print(create_hash(""))
    print(create_hash("AoC 2017"))
    print(create_hash("1,2,3"))
    print(create_hash("1,2,4"))