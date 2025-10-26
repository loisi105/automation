from PIL import Image, ImageOps
import os

def merge_images(background, foreground):
    """
    Merge the logo image with the background image.

    Args:
        background: background image
        foreground: foreground image e.g. logo
    Returns:
        merged image
    """
    print("merge_images: ", background, foreground)
    padding_horizontal, padding_vertical, needed_with, needed_height = calculate_logo_size(background, foreground)

    foreground.thumbnail((needed_with, needed_height))
    w = background.size[0] - foreground.size[0] - padding_horizontal
    h = background.size[1] - foreground.size[1] - padding_vertical

    merged = background.copy()
    merged.paste(foreground, (w, h), mask=foreground)
    return merged


def calculate_logo_size(background, foreground):
    """
    Calculate the size of the logo image based on the background image.

    Args:
        background: background image
        foreground: foreground image e.g. logo
    Returns:
        padding horizontal and vertical, with and height needed for the logo image
    """
    print("calculate_logo_size: ", background, foreground)
    ratio_background = background.width / background.height
    ratio_foreground = foreground.width / foreground.height

    if ratio_background > 1.2:
        foreground.thumbnail((background.width / 5, background.width / 5 * ratio_foreground))
    elif ratio_background < 0.8:
        foreground.thumbnail((background.width / 3, background.height / 3 * ratio_foreground))
    else:
        foreground.thumbnail((background.width / 3, background.height / 3 * ratio_foreground))

    padding_horizontal = int(background.width / 80)
    padding_vertical = int(background.height / 80)

    needed_with = int(foreground.width + padding_horizontal)
    needed_height = int(foreground.width / ratio_foreground + padding_vertical)

    return padding_horizontal, padding_vertical, needed_with, needed_height


def save_image(image, path_to_image):
    """
    Save the image to the specified file path.
    Args:
        image: the image to be saved
        path_to_image: the absolute path to the image
    """
    print("save_image: ", image, path_to_image)
    os.makedirs("../DONE", exist_ok=True)
    image_out = image.copy()
    image_out.save(path_to_image)
    print("Image saved as:", path_to_image)


def find_images_in_directory(directory):
    """
    Check for image files in the specified directory and return their names.
    Args:
        directory (str): Path to the directory to check.
    Returns:
        list: A list of image file names found in the directory.
    """
    print("find_images_in_directory: ", directory)
    # Supported image file extensions
    image_extensions = {'.jpg', '.jpeg', '.png'}

    # Validate the directory exists
    if not os.path.isdir(directory):
        raise ValueError(f"The directory '{directory}' does not exist or is not accessible.")

    # List to store image file names
    image_files = []

    # Iterate through the directory contents
    for file_name in os.listdir(directory):
        # Get the file extension and check if it's an image
        if os.path.splitext(file_name)[1].lower() in image_extensions:
            image_files.append(file_name)

    return image_files


if __name__ == "__main__":
    parent_path = os.path.dirname(__file__)
    directory_path_in = parent_path + "\\..\\in\\"
    directory_path_src = parent_path + "\\..\\src\\"
    directory_path_out = parent_path + "\\..\\out\\"

    print("Input directory:", directory_path_in)
    print("Source directory:", directory_path_src)
    print("Output directory:", directory_path_out)

    images = find_images_in_directory(directory_path_in)
    if images:
        print("Image files found:", images)
    else:
        print("No image files found in the directory.")
        exit(2)

    for img in images:
        print("Processing image:", img)
        img = Image.open(directory_path_in + img)
        img_rotated = ImageOps.exif_transpose(img)  # Rotate image if needed to correct EXIF data

        logo = Image.open(directory_path_src + "logo.png")

        background = img_rotated.copy()
        foreground = logo.copy()

        merged_image = merge_images(background, foreground)

        save_image(merged_image, directory_path_out + '_' + img.filename.split('\\')[-1])
    exit(0)
