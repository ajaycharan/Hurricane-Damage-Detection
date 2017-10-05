import os
import random
image_dir = "images"
annotation_dir = "annotations"
annotation_prefix = "label_"
images = [f for f in os.listdir('images') if f.endswith(".png")]
random.shuffle(images)

train_val = images[:int(0.8*len(images))]
test = images[int(0.8*len(images)):]
train =  train_val[:int(0.8*len(train_val))]
validation = train_val[int(0.8*len(train_val)):]

for set, fname in zip([train, test, validation], ["training", "testing", "validation"]):
    for f in set:
        os.renames(os.path.join(image_dir, f), os.path.join(image_dir, fname, os.path.basename(f)))
        os.renames(os.path.join(annotation_dir, annotation_prefix + f), os.path.join(annotation_dir, fname, annotation_prefix + os.path.basename(f)))

    
