import argparse
from removebg import RemoveBg


def remove_background(input_file, output_file):
    """
    Remove the background from an image file using the RemoveBg library.

    Parameters:
    input_file (str): The path to the input image file.
    output_file (str): The path to save the output image file without background.

    Returns:
    None
    """
    rmbg = RemoveBg("k7tsZ6E5h3jXEyTLfigbMNBH", "error.log")
    rmbg.remove_background_from_img_file(input_file)
    rmbg.save(output_file)


def main():
    """
    Parse command-line arguments and call the remove_background function.
    """
    parser = argparse.ArgumentParser(description='Remove background from image.')
    parser.add_argument('input_file', type=str, help='The image file to remove the background from.')
    parser.add_argument('output_file', type=str, help='The output file to save the image without background.')

    args = parser.parse_args()

    remove_background(args.input_file, args.output_file)


if __name__ == "__main__":
    main()