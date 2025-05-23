def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def calculate_checksum(filename):
    data = read_file(filename)
    checksum = 0

    for row in data.splitlines():
        numbers = row.split(',')
        min_number = int(numbers[0])
        max_number = int(numbers[0])
        for number in numbers:
            number = int(number)
            if number < min_number:
                min_number = number
            if number > max_number:
                max_number = number
        checksum += (max_number - min_number)

    return checksum

def calculate_divisible_sum(filename):
    data = read_file(filename)
    divisible_sum = 0

    for row in data.splitlines():
        numbers = row.split(',')
        for i in range(len(numbers)):
            curr_number = int(numbers[i])
            for j in range(i+1, len(numbers)):
                other_number = int(numbers[j])
                if curr_number % other_number == 0:
                    divisible_sum += curr_number // other_number
                    break
                elif other_number % curr_number == 0:
                    divisible_sum += other_number // curr_number
                    break

    return divisible_sum

if __name__ == "__main__":
    print(calculate_checksum("day2.csv"))
    print(calculate_divisible_sum("day2.csv"))