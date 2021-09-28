with open('day8/input.txt') as f:
    input_raw = f.read().strip()

width, height = 25, 6
px_layer = width*height
n_layers = int (len(input_raw) / px_layer)
layers = [input_raw[i*px_layer : (i+1)*px_layer] for i in range(n_layers)]


counts = [l.count('0') for l in layers]
min_layer = layers[counts.index(min(counts))]

## Part 1
print(f'Part 1: {min_layer.count("1")*min_layer.count("2")}')

## Part 2
for y in range(height):
    line = ""
    for x in range(width):
        l = 0
        while layers[l][x + y*width] == "2":
            l += 1
        line += chr(9608) if layers[l][x + y*width] == '1' else ' '

    print(line)

pass

