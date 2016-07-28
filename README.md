# Thumbnail Generator Utility

This python utility can be used to generate thumbnail images. The thumbnails are generated in the specified directory with naming convention as <image-name>.thumbnail.<extension>.

###Install dependencies with pip
```bash
pip install Pillow
```

###Run the utility
```bash
python thumbnail.py <source-images-directory> <destination-thumbnails-directory>
```

###Improvements
1. Multi platform support
2. Add image orientation based on the EXIF data of the photos and if `Orientation` tag is found
3. Add configuration file
4. Add logging
