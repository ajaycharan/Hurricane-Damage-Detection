import csv
import re
import json
import numpy as np
import os
from PIL import Image

#import matplotlib.pyplot as plt

image_size = [362,543] #Height, width
re_file_name = re.compile('.*/(.*)$')
folder = 'image_labels'
if not os.path.exists(folder):
	os.makedirs(folder)

with open('Batch_2939578_batch_results.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)  # skip the headers
    for row in reader:
        re_filename_search = re.search(re_file_name, row[27]) #Find filename in URL
        if re_filename_search:
            filename = re_filename_search.group(1)
        else:
            print "Could not find filename in ", row[27]
            continue
        label_set = json.loads(row[29])
        image_arr = np.zeros(image_size, dtype='uint8')
        for label in label_set:
            #image_arr[label['left']:(label['left'] + label['width']), label['top']:(label['top'] + label['height'])] = True
            image_arr[label['top']:(label['top'] + label['height']),label['left']:(label['left'] + label['width'])] = 255
            img = Image.fromarray(image_arr, mode='L').convert('1')
#        if label_set:
#            print label_set
#            print filename
#            im = plt.imread(filename)
#            implot = plt.imshow(im)
#            plt.imshow(image_arr, cmap='Greys', alpha=0.3)
#            plt.show()
            img.save(os.path.join(folder, 'label_' + filename))