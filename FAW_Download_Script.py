import urllib.request
import json
import argparse
import os

# flag -d --disable-verbose does not print the intermediate steps
'''
	This cropping tool is written to work with the JSON file format obtained 
	from the Dataturks labelling tool. Might not work with other JSON file
	formats
'''
# Path to the directory where the images should be saved
save_path = '/home/hariharan/Code/PS-1/prj/FAW_Images/'

# Base URL of the server (to which adding /content/... gives the link to the image)
base_url = 'http://34.93.100.171'

# Parsing CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--disableVerbose', action='store_true',
					 help='disables verbosity')
args = parser.parse_args()


def download_images():
	
	# Checking if save directory exists. If not, creating the save directory
	if not os.path.exists(save_path):
		os.makedirs(save_path)

	try:
		with open('FAW Test.json', 'r') as f1, open('input_file.txt', 'w') as f2:
			for line in f1:
				x = json.loads(line)
				file_name = save_path + x['content'].split('/')[-1]
				height = x['annotation'][0]['imageHeight']
				width = x['annotation'][0]['imageWidth']
				xrmin = x['annotation'][0]['points'][0][0]
				xrmax = x['annotation'][0]['points'][2][0]
				yrmin = x['annotation'][0]['points'][0][1]
				yrmax = x['annotation'][0]['points'][2][1]
				xmin = int(xrmin * width)
				ymin = int(yrmin * height)
				xmax = int(xrmax * width)
				ymax = int(yrmax * height)
				f2.write(file_name + ',' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + ',' + 'FAW\n')
				try:
					urllib.request.urlretrieve(base_url + x['content'], file_name)
					print("Downloading image %s" % x['content'].split('/')[-1])
				except Exception as e:
					print("Unable to download image %s" % x['content'].split('/')[-1])
					print(str(e))
	except IOError as e:
		print("Operation failed: %s" % e.strerror)

if __name__ == '__main__':
	print("Starting...")
	download_images()