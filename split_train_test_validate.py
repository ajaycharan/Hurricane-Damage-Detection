import os
import random

images = [f for f in os.listdir('.') if f.endswith(".png")]
random.shuffle(images)

train_val = images[:int(0.8*len(images))]
test = images[int(0.8*len(images)):]
train =  train_val[:int(0.8*len(train_val))]
validation = train_val[int(0.8*len(train_val)):]

for set, fname in zip([train, test, validation], ["training", "testing", "validation"]):
    for f in set:
        os.renames(f, os.path.join('.', fname, os.path.basename(f)))


