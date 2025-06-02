def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_connections(filename):
    connections = {}
    for line in read_file(filename).splitlines():
        line = line.replace(',', '')
        line = line.split(' ')
        connections[line[0]] = connections.get(line[0], set()).union(set(line[2:]))

    return connections

def find_friends(filename, program, connections=None):
    if connections is None:
        connections = generate_connections(filename)
    friends_with_program = set()
    
    friends_to_check = {program}
    while len(friends_to_check) > 0:
        new_friends_to_check = set()
        for friend in friends_to_check:
            if friend not in friends_with_program:
                friends_with_program.add(friend)
                new_friends_to_check = new_friends_to_check.union(connections.get(friend, set()))
        friends_to_check = new_friends_to_check
    
    return friends_with_program

def find_groups_count(filename):
    connections = generate_connections(filename)
    programs_left = set(connections.keys())
    groups_count = 0

    while len(programs_left) != 0:
        program = programs_left.pop()
        program_friends = find_friends(filename, program, connections)
        groups_count += 1
        programs_left = programs_left.difference(program_friends)

    return groups_count

if __name__ == "__main__":
    print(find_friends('day12.txt', '0'))
    print(find_groups_count('day12.txt'))
                