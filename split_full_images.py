import os, image_slicer
from PIL import Image
full_image_dir = 'full_images'
split_image_dir = 'split_images'
number_splits = 16**2
print "Splitting images into {}".format(number_splits)
if not os.path.exists(split_image_dir):
	os.makedirs(split_image_dir)
num_images = len(os.listdir(full_image_dir))
print "{} Images to split".format(num_images)
for i, f in enumerate(os.listdir(full_image_dir)):
	if i % 20 == 0:
		print "Splitting image {}/{}".format(i+1, num_images)
	if f.endswith(".jpg"):
		tiles = image_slicer.slice(os.path.join(full_image_dir, f), number_splits, save=False)
		image_slicer.save_tiles(tiles, prefix = image_slicer.get_basename(f), directory=split_image_dir)
		