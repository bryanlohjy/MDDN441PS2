# Create sequence of images from sorted images in csv
import numpy
file = open('temp/smartgrid/montage_26x13.txt', 'r')

# 26 x 13 grid of faces - get indexes of images in a snakey order (instead of going from top to bottom repeatedly, it alternates between going from top to bottom and vice versa - more order)
def get_snake_loop(arr, snake_direction, grid_x, grid_y):
    snake_list=[]
    if (snake_direction == 'x'):
        split_arr = numpy.array_split(numpy.array(arr),grid_y)
    elif (snake_direction == 'y'):
        split_arr = numpy.array_split(numpy.array(arr),grid_x)
    index = 0
    for i in split_arr:
        to_flatten=[]
        if (index%2 == 0):
            to_flatten = i
        else:
            to_flatten = i[::-1]
        for val in to_flatten:
            snake_list.append(val)
        index += 1
    return snake_list

imgs = []
for line in file:
    imgs.append(line.replace('"','').strip())

x_sequence = get_snake_loop(imgs, 'x', 23, 16)
y_sequence = get_snake_loop(imgs, 'y', 23, 16)

# Create sequenced text files ======================
x_file = open('./temp/sequencer/x_sequence.txt', 'w') 
y_file = open('./temp/sequencer/y_sequence.txt', 'w') 
for x_img in x_sequence:
    x_file.write(x_img + '\n')

x_file.close()

for y_img in y_sequence:
    y_file.write(y_img + '\n')

y_file.close()