def redistribute(banks):
    # banks is a list of block counts
    max_banks = max(banks)
    max_index = banks.index(max_banks)
    banks[max_index] = 0

    each_block_increment = max_banks // len(banks)
    banks = [blocks + each_block_increment for blocks in banks]

    remainder = max_banks % len(banks)
    for i in range(1, remainder + 1):
        banks[(max_index + i) % len(banks)] += 1

    return banks

def num_redistributions(banks):
    # banks is a list of block counts
    MAX_ITERATIONS = 1000000  # Safety limit
    seen_configs = {}
    iteration = 0

    while iteration < MAX_ITERATIONS:
        # Use tuple of banks as key for faster lookup
        config = tuple(banks)
        if config in seen_configs:
            return iteration - seen_configs[config], iteration
        seen_configs[config] = iteration
        banks = redistribute(banks)
        iteration += 1

    raise Exception(f"Exceeded maximum iterations ({MAX_ITERATIONS}) without finding a repeat")

if __name__ == "__main__":
    print(num_redistributions([0, 2, 7, 0]))
