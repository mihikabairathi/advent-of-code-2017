def short_circuit(step_size, biggest_value=2017):
    spinlock = [0]
    current_position = 0
    zero_position = 0

    for i in range(1, biggest_value + 1):
        new_position = ((current_position + step_size) % len(spinlock)) + 1
        spinlock.insert(new_position, i)
        current_position = new_position

        if current_position <= zero_position:
            zero_position += 1

    return spinlock[(current_position + 1) % len(spinlock)], spinlock[zero_position + 1]

def short_circuit_efficient(step_size, biggest_value=2017):
    spinlock_length = 1
    current_position = 0
    after_zero = None

    for i in range(1, biggest_value + 1):
        new_position = ((current_position + step_size) % spinlock_length) + 1
        if new_position == 1:
            after_zero = i

        current_position = new_position
        spinlock_length += 1

    return after_zero

if __name__ == "__main__":
    print(short_circuit(3))  # Output: 638
    print(short_circuit_efficient(3, 50000000))
