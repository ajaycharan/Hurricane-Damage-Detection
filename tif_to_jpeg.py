import os
from PIL import Image
import image_slicer
for f in os.listdir('.'):
	if f.endswith(".tif"):
		im = Image.open(f)
		fn, ext = os.path.splitext(f)
		print 'Converting {}'.format(f)
		im.save(fn + '.jpg')
		print 'Splitting image {}'.format(fn + '.jpg')
		image_slicer.slice(fn + '.jpg', 16)