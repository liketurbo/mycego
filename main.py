import sys
import os
from PIL import Image

def compose(dir_p):
	# let's assume that amount of images in the folder is always more than 4
	PER_IMAGE_WIDTH = 400
	PER_IMAGE_HEIGHT = 400
	IMAGES_PER_ROW = 4

	images = os.listdir(dir_p)

	max_width = PER_IMAGE_WIDTH * IMAGES_PER_ROW
	max_height = int(len(images) / IMAGES_PER_ROW) * PER_IMAGE_HEIGHT

	width_i = 0
	height_i = 0

	combined_image = Image.new("RGB", (max_width, max_height))

	for image_p in images:
		image = Image.open(os.path.join(dir_p, image_p))

		resizing_factor = PER_IMAGE_WIDTH / image.width
		new_height = int(image.height * resizing_factor)
		resized_image = image.resize((PER_IMAGE_WIDTH, new_height))

		combined_image.paste(resized_image, (width_i, height_i))
		width_i += PER_IMAGE_WIDTH
		if width_i >= max_width:
			width_i = 0
			height_i += PER_IMAGE_HEIGHT

	combined_image.save("Result.tif")

for index, arg in enumerate(sys.argv):
	if index > 0:
		compose(arg)