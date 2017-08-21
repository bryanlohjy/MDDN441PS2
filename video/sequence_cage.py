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

# Create sequenced list of images in csv file ======================
sequence_csv = open('./temp/sequencer/sequence.csv', 'w')
column_titles = 'index,x_img,y_img'
sequence_csv.write(column_titles + '\n')

index = 0
for i in range(len(x_sequence)):
    sequence_csv.write('{},{},{}\n'.format(index, x_sequence[index], y_sequence[index]))
    index+=1

sequence_csv.close()