import os
import sys
import ConfigParser
import Image
from PIL import Image
from PIL.ExifTags import TAGS

"""
Generates the filename for thumbnail image
"""
def generate_filename(filename):
	dot_index = filename.rindex(".")
	return filename[:dot_index] + ".thumbnail" + filename[dot_index:]


"""
Creates the thumbnail image
"""
def thumbnail_generator(images_source_dir, filename):
	# TODO: Add settings cfg file
	# This is to by-pass the image size DecompressionBombWarning DOS attack warning...
	Image.MAX_IMAGE_PIXELS = None
	supported_images = ["jpg"]
	thumbnail_size = 128, 128

	print "Generating thumbnail for", filename
	image = Image.open(images_source_dir + filename)
	image_extension = filename.split(".")[-1].lower()

	if image_extension in supported_images:
		try:
			new_filename = generate_filename(filename)
			image.thumbnail(thumbnail_size, Image.ANTIALIAS)

			print "src dir", images_source_dir
			image.save(images_source_dir + new_filename, 'JPEG')
		except IOError as ioe:
			print "Failed to generate thumbnail image for file", filename, ioe	


"""
Application entry point
"""
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print ('Usage: thumbnail.py <image-dir>')
		exit(0)

	images_source_dir = sys.argv[1] + "\\"

	# TODO: Create a logging class
	print "Starting thumbnail generator utility...\n"

	files = os.listdir(images_source_dir)
	for filename in files:
		thumbnail_generator(images_source_dir, filename)

	print "Done!\n"