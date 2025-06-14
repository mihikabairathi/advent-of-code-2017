from functools import cmp_to_key

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def generate_particle_list(filename):
    particles = []
    for line in read_file(filename).splitlines():
        split_line = line.split(', ')

        p = split_line[0][3:-1].split(',')
        position = (int(p[0]), int(p[1]), int(p[2]))

        v = split_line[1][3:-1].split(',')
        velocity = (int(v[0]), int(v[1]), int(v[2]))

        a = split_line[2][3:-1].split(',')
        acceleration = (int(a[0]), int(a[1]), int(a[2]))

        particle = {'a': acceleration, 'p': position, 'v': velocity}
        particles.append(particle)

    return particles

def sort_particles(p1: dict, p2: dict):
    s1 = abs(p1['a'][0]) + abs(p1['a'][1]) +abs(p1['a'][2])
    s2 = abs(p2['a'][0]) + abs(p2['a'][1]) +abs(p2['a'][2])

    return s1 - s2

def find_closest_particle(filename):
    particles = generate_particle_list(filename)
    sorted_particles = sorted(particles, key=cmp_to_key(sort_particles))
    return particles.index(sorted_particles[0]), particles.index(sorted_particles[1]), particles.index(sorted_particles[2]), particles.index(sorted_particles[3]), particles.index(sorted_particles[4])

def simulate_collisions(filename):
    particles = generate_particle_list(filename)

    for i in range(10000):
        new_particles = []
        positions = {}
        for particle in particles:
            positions[particle['p']] = positions.get(particle['p'], 0) + 1
        for particle in particles:
            if positions[particle['p']] == 1:
                new_particles.append(particle)
        particles = new_particles

        simulate_particles(particles)

    return len(particles)

def simulate_particles(particles):
    for particle in particles:
        particle['v'] = (particle['v'][0] + particle['a'][0], particle['v'][1] + particle['a'][1], particle['v'][2] + particle['a'][2])
        particle['p'] = (particle['v'][0] + particle['p'][0], particle['v'][1] + particle['p'][1], particle['v'][2] + particle['p'][2])

if __name__ == '__main__':
    print(find_closest_particle('day20.txt'))
    print(simulate_collisions('day20.txt'))