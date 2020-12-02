# Harsha Lakamsani
# HTCA (half-triangle cellular automata) algorithm
# 1CA displayed (nCA)

import matplotlib.pyplot as plt # pyplot
from matplotlib import colors # for colormap
import numpy as np # random vals
from PIL import Image, ImageDraw # write plots to gif 
import os # image garbage collection, may not work on all kernels
import gc # automated garbage collection  

# initial null plane
x_size = 200
y_size = 200
data = np.zeros((x_size,y_size)) # maroon canvas at start
# colormap for binary grid coloring (0, 1 respectively)
cmap = colors.ListedColormap(['maroon', 'gold'])
# random positioning at start
pos_x = np.random.randint(0, x_size)
pos_y = np.random.randint(0, y_size)
counter = 600 # number of iterations
sub_counter = 0 # current iteration
images = [] # collate plots
control = 13 # HT arm length

# HT method
def half_triangle(pos_x, pos_y):
  # try/catch for OOB error
  try:
    # intended half-triangle (HT) behavior
    if data[pos_x][pos_y] == 0:
      orientation = np.random.randint(0,1)
      if orientation == 0:
        for y_new in range(0, control):
          data[pos_x][pos_x-y_new] = 1
        for x_new in range(0, control):
          data[(-1*x_new)+pos_x][pos_y] = 1
        data[pos_x+1][pos_y-1] = 1
      else:
        for y_new in range(0, control):
          data[pos_x-y_new][y_new] = 1
        for x_new in range(0, control):
          data[pos_x][(-1*x_new)+pos_y] = 1
        data[pos_x-1][pos_y+1] = 1        
#     # intended double half-triangle (2HT) behavior
#     if data[pos_x][pos_y] == 0:
#       # switch conditional (binary 0, 1)
#       orientation = np.random.randint(0,2)
#       # NW-oriented HT
#       if orientation == 0:
#         # top
#         for y_new in range(0, control):
#           data[pos_x][pos_y-y_new] = 1
#         # side
#         for x_new in range(0, control):
#           data[pos_x+x_new][pos_y] = 1
#         # offcenter
#         data[pos_x+1][pos_y-1] = 1
#       # SW-oriented HT
#       else:
#         # top
#         for y_new in range(0, control):
#           data[pos_x][pos_y+y_new] = 1
#         # side
#         for x_new in range(0, control):
#           data[pos_x-x_new][pos_y] = 1
#         # offcenter
#         data[pos_x-1][pos_y+1] = 1     
    else:
      # this is the secondary breaker, change True to exit condition if wanted
      # with n >= 2 workers, must implement a separate interaction  
      True
  # catch any out-of-bounds error
  except IndexError:
    True
 
# do-while loop for algorithm
while True:
  # call HT method
  half_triangle(pos_x, pos_y)
  # reset positions to rand ints
  pos_x = np.random.randint(0, x_size)
  pos_y = np.random.randint(0, y_size)
  # set colormap
  plt.imshow(data, cmap=cmap)
  # no axes
  plt.axis('off')
  # save plot to local dir
  plt.savefig('fig.png', bbox_inches='tight')
  # open saved png plot
  im = Image.open('fig.png')
  # add png to array of images for processing
  images.append(im)
  del(im)
#   os.remove('fig.png')
  gc.collect()
  # increment iteration #
  sub_counter += 1
  print(sub_counter)
  # conditional for exit (max iterations reached/not)
  if sub_counter == counter:
    break

# save images array as collated gif
images[0].save('test.gif', save_all=True, append_images=images[1:], optimize=True, duration=40, fps=60, loop=0)