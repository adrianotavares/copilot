import argparse
import requests
from removebg import RemoveBg
from PIL import Image, UnidentifiedImageError
from colorama import init, Fore, Style
import json

# Initialize colorama
init(autoreset=True)

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

class ColoredHelpFormatter(argparse.HelpFormatter):
    def format_help(self):
        help_text = super().format_help()
        return f"{Fore.BLUE}{help_text}{Style.RESET_ALL}"
        
def remove_background(input_file):
    try:
        rmbg = RemoveBg(config['REMOVE_BG_API_KEY'], config['ERROR_LOG_FILE'])
        rmbg.remove_background_from_img_file(input_file)
        new_file = input_file.replace('.', '_no_bg.')
        print(f"{Fore.GREEN}New file created: {new_file}")
    except requests.exceptions.HTTPError as e:
            print(f"{Fore.RED}API KEY error occurred: {e}")
    except Exception as e:
        print(f"{Fore.RED}An error occured: {e}")         

def resize_image(input_file, ri):
    try:
         new_size = tuple(map(int, ri.split(',')))
         if len(new_size) != 2:
            raise ValueError(f"{Fore.RED}Size must be a tuple of two integers (width, height).")
    except ValueError as e:
         print(f"{Fore.RED}Invalid size format: {e}")
        
    try:
        img = Image.open(input_file)
        resized_img = img.resize(new_size)
        resized_img.save(input_file)
        print(f"{Fore.GREEN}Image {input_file} has been resized.")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

def get_image_size(input_file):
    try:
        img = Image.open(input_file)
        width, height = img.size
        return width, height
    except Exception as e:
        print(f"{Fore.RED}An error occurred while getting the image: {e}")
        return None

def handle_image_file(input_file):
    try:
        img = Image.open(input_file)
    except FileNotFoundError as e:
        print(f"{Fore.RED}The file is not found {e}")
        quit()
    except UnidentifiedImageError:
        print(f"{Fore.RED}The file is not a valid image: {input_file}")
        quit()
    except Exception as e:
        print(f"{Fore.RED}An error occurred while handling the image: {e}")    
        quit()
            
def main():
    parser = argparse.ArgumentParser(description='Image Processing Script.', formatter_class=ColoredHelpFormatter )
    parser.add_argument('input_file', type=str, help='The image file to process.')
    parser.add_argument('-rb', action='store_true', help='Remove background from image.')
    parser.add_argument('-ri', type=str, help='Resize image with specified size (width,height).')
    parser.add_argument('-gs', action='store_true', help='Get the size of the image.')
    
    args = parser.parse_args()
    
    handle_image_file(args.input_file)

    if args.rb:
        remove_background(args.input_file)
    elif args.ri:
        resize_image(args.input_file, args.ri)
    elif args.gs:
        size = get_image_size(args.input_file)
        if size:
            print(f"{Fore.BLUE}Image: {args.input_file} size: {size} (width, height)")

if __name__ == "__main__":
    main()