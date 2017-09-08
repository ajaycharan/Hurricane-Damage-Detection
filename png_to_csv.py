import os
import csv
with open('test.csv', 'wb') as csvfile:
	csv_writer = csv.writer(csvfile)
	csv_writer.writerow(['image_url' ,'objects_to_find'])
	object_to_find = 'Fallen/Downed Tree'
	for f in os.listdir('.'):
		if f.endswith(".png"):
			url = 'https://s3.amazonaws.com/mturk-aerial-applications/mturk/' + f
			csv_writer.writerow([url, object_to_find])