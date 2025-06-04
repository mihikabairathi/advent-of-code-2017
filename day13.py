import copy

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def parse_layers(filename):
    layers = dict()
    for layer in read_file(filename).splitlines():
        layer = layer.split(':')
        layers[int(layer[0])] = {'depth': int(layer[1].strip()), 'scanner_position': 0, 'direction': -1}

    return layers

def compute_severity(filename=None, layers=None):
    if layers is None:
        layers = parse_layers(filename)
    max_layer = max(layers.keys())
    caught_layers = 0
    severity = 0

    for i in range(max_layer + 1):
        if i in layers and layers[i]['scanner_position'] == 0:
            severity += (i * layers[i]['depth'])
            caught_layers += 1
        for layer in layers:
            if layers[layer]['scanner_position'] == 0:
                layers[layer]['direction'] = -layers[layer]['direction']
            elif layers[layer]['scanner_position'] == layers[layer]['depth'] - 1:
                layers[layer]['direction'] = -layers[layer]['direction']
            layers[layer]['scanner_position'] += layers[layer]['direction']

    return severity, caught_layers

def compute_severity_efficient(layers_by_time, delay):
    diff = 0
    if delay not in layers_by_time:
        diff = max(layers_by_time.keys()) - delay
    layers = layers_by_time[delay + diff]
    max_layer = max(layers.keys())

    for i in range(diff, max_layer + 1):
        if i in layers and layers[i]['scanner_position'] == 0:
            return 1
        
        if delay + i + 1 in layers_by_time:
            layers = layers_by_time[delay + i + 1]
        else:
            new_layers = copy.deepcopy(layers)
            for layer in new_layers:
                if new_layers[layer]['scanner_position'] == 0:
                    new_layers[layer]['direction'] = -new_layers[layer]['direction']
                elif new_layers[layer]['scanner_position'] == new_layers[layer]['depth'] - 1:
                    new_layers[layer]['direction'] = -new_layers[layer]['direction']
                new_layers[layer]['scanner_position'] += new_layers[layer]['direction']
            layers_by_time[delay + i + 1] = new_layers
            layers = new_layers

    return 0

def find_delay(filename):
    layers = parse_layers(filename)
    layers_by_time = {0: copy.deepcopy(layers)}
    delay = 0
    while True:
        caught_layers = compute_severity_efficient(layers_by_time=layers_by_time, delay=delay)
        if caught_layers == 0:
            return delay
        delay += 1

if __name__ == "__main__":
    print(compute_severity('day13.txt'))
    print(find_delay('day13.txt'))
