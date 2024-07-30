import argparse
import requests
from removebg import RemoveBg
from PIL import Image

def remove_background(input_file):
    # Remove the background from an image file using the RemoveBg library.

    try:
        rmbg = RemoveBg("k7tsZ6E5h3jXEyTLfigbMNBH", "error.log")
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

def resize_image(input_file, ri):
    #Resize the image file using the PIL library.
        
    try:
         new_size = tuple(map(int, ri.split(',')))
         if len(new_size) != 2:
            raise ValueError("Size must be a tuple of two integers (width, height).")
    except ValueError as e:
         print(f"Invalid size format: {e}")
            
    try:
        img = Image.open(input_file)
        resized_img = img.resize(new_size)
        resized_img.save(input_file)
    except FileNotFoundError as e:
        print("The file is not found", e)
    except Exception as e:
        print("An error occurred", e)
        
def main():
    #Parse command-line arguments and call the appropriate function.
    
    parser = argparse.ArgumentParser(description='Remove background from image.')
    parser.add_argument('input_file', type=str, help='The image file to process.')
    parser.add_argument('-rb', action='store_true', help='Remove background from image.')
    parser.add_argument('-ri', type=str, help='Resize image with specified size (width,height).')
    
    args = parser.parse_args()

    if args.rb:
        remove_background(args.input_file)
    elif args.ri:
        resize_image(args.input_file, args.ri)

if __name__ == "__main__":
    main()