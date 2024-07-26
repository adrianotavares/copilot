import argparse
from removebg import RemoveBg
from PIL import Image
import requests

def remove_background(input_file):
    """
    Remove the background from an image file using the RemoveBg library.

    Parameters:
    input_file (str): The path to the input image file.
    
    Returns:
    None
    """
    try:
        rmbg = RemoveBg("k7tsZ6E5h3jXEyTLfigbMNB", "error.log")
        rmbg.remove_background_from_img_file(input_file)
    except FileNotFoundError:
        print("The file is not found")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print("API KEY error occurred",e)
        else:
            print(f"HTTP error occurred:",e)
    except Exception as e:
        print("An error occured", e)

# new function to resize the image receive the arguments image path, -r, the new size
def resize_image(input_file, new_size):
    """
    Resize the image file using the PIL library.

    Parameters:
    input_file (str): The path to the input image file.
    new_size (str): The new size of the image file.
    
    Returns:
    None
    """
    try:
        img = Image.open(input_file)
        resized_img = img.resize(new_size)
        resized_img.save(input_file)
    except FileNotFoundError as e:
        print("The file is not found", e)
    except Exception as e:
        print("An error occurred", e)
        
def main():
    """
    Parse command-line arguments and call the appropriate function.
    """
    parser = argparse.ArgumentParser(description='Remove background from image.')
    parser.add_argument('input_file', type=str, help='The image file to process.')
    parser.add_argument('-rb', action='store_true', help='Remove background from image.')
    parser.add_argument('-ri', type=str, help='Resize image with specified size (width,height).')
    
    args = parser.parse_args()

    if args.rb:
        remove_background(args.input_file)
    elif args.ri:
        try:
            new_size = tuple(map(int, args.ri.split(',')))
            if len(new_size) != 2:
                raise ValueError("Size must be a tuple of two integers (width, height).")
            resize_image(args.input_file, new_size)
        except ValueError as e:
            print(f"Invalid size format: {e}")

if __name__ == "__main__":
    main()