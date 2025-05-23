def find_steps(input):
    # layers are 0, 1, 2, etc. 
    
    if input == 1:
        return 0

    nearest_end = int((input-1)**0.5)
    round = (nearest_end + 1) // 2 # 2

    length_of_layer_side = 2 * round + 1 # 5
    end_of_that_round = length_of_layer_side ** 2 # 25
    total_in_that_round = end_of_that_round - (length_of_layer_side - 2)**2 # 16
    extra_steps = abs(((total_in_that_round - end_of_that_round + input) % (total_in_that_round//4)) - (length_of_layer_side // 2))

    return round + extra_steps

def find_min_greater_than(input):
    num_in_layer = 0
    layer = 0
    grid = {(0, 0): 1}

    while True:
        layer += 1
        num_in_layer += 8
        num_per_side = num_in_layer // 4 + 1

        side_tracker = 1 # 2
        last_layer_tracker = max(0, num_in_layer - 8 - 1)

        for i in range(num_in_layer):
            if i == 0:
                last_layer_tracker = max(0, num_in_layer - 8 - 1)
                side_tracker = 1

            grid[(layer, i)] = grid.get((layer, i-1), 0)

            if side_tracker == 0:
                last_layer_tracker = (last_layer_tracker - 1) % max(1, num_in_layer - 8)
                grid[(layer, i)] += grid.get((layer - 1, last_layer_tracker), 0)
                if i == num_in_layer - 1:
                    grid[(layer, i)] += grid.get((layer, 0), 0)
            elif side_tracker == 1:
                grid[(layer, i)] += grid.get((layer, i-2), 0)
                grid[(layer, i)] += grid.get((layer - 1, last_layer_tracker), 0)
                if i == num_in_layer - 2:
                    grid[(layer, i)] += grid.get((layer, 0), 0)
                if layer == 1:
                    grid[(layer, i)] += grid.get((layer - 1, last_layer_tracker + 1), 0)
                else:
                    grid[(layer, i)] += grid.get((layer - 1, (last_layer_tracker + 1) % max(1, num_in_layer - 8)), 0)

            elif side_tracker == num_per_side - 2:
                grid[(layer, i)] += grid.get((layer - 1, last_layer_tracker), 0)
                grid[(layer, i)] += grid.get((layer - 1, (last_layer_tracker - 1) % max(1, num_in_layer - 8)), 0)
                if i == num_in_layer - 2:
                    grid[(layer, i)] += grid.get((layer, 0), 0)
            else:
                grid[(layer, i)] += grid.get((layer - 1, last_layer_tracker), 0)
                grid[(layer, i)] += grid.get((layer - 1, (last_layer_tracker - 1) % max(1, num_in_layer - 8)), 0)
                if layer == 1:
                    grid[(layer, i)] += grid.get((layer - 1, last_layer_tracker + 1), 0)
                else:
                    grid[(layer, i)] += grid.get((layer - 1, (last_layer_tracker + 1) % max(1, num_in_layer - 8)), 0)
            
            if side_tracker != 0:
                last_layer_tracker = (last_layer_tracker + 1) % max(1, num_in_layer - 8)
            side_tracker = (side_tracker + 1) % (num_per_side - 1)

            if grid[(layer, i)] > input:
                return grid[(layer, i)]
            else:
                print(f'{grid[(layer, i)]} is for layer and index ({layer}, {i})')


if __name__ == "__main__":
    print(find_steps(1)) # 0
    print(find_steps(12)) # 3
    print(find_steps(23)) # 2
    print(find_steps(1024)) # 31
    print(find_steps(25)) # 4

    print(find_min_greater_than(900)) #931