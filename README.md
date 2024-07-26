# Image Processing Script

This Python script uses the `removebg` library to remove the background from an image file.

## Requirements

- Python 3
- Python libs 
  `argparse`
  `removebg`
  `Pillow`
  `requests` 

## Installation

1. Clone this repository:

```bash
git clone https://github.com/adrianotavares/copilot
```

2. Navigate to the repository directory:

```bash
cd yourrepository
```

3. Install the required Python libraries:

```bash
pip install -r removebg
pip install -r Pillow
```

## Usage

### Remove Background

To remove the background from an image, run the following command:

- ```-rb```: Flag to remove the background from the image.
- ```input_file```: The path to the image file to be processed.

### Resize Image

To resize an image, run the following command:

- ```-ri```: Flag to resize the image.
- ```width,height```: The new dimensions of the image (width, height).
- ```input_file```: The path to the image file to be processed.

### Example

To remove the background from an image called image.jpg:

```bash
python script.py -rb image.jpg
```

To resize an image called image.jpg to 100x200 pixels:

```bash
python script.py -ri 100,200 image.jpg
```

To help `-h, --help`, to see the command line instructions

```bash
python script.py -help
```

Instructions 

```bash
usage: script.py [-h] [-rb] [-ri RI] input_file

Remove background from image.

positional arguments:
  input_file  The image file to process.

options:
  -h, --help  show this help message and exit
  -rb         Remove background from image.
  -ri RI      Resize image with specified size (width,height).
```

## License

This project is licensed under the terms of the MIT license.
