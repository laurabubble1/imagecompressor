import os
from PIL import Image

def compress_image(input_path, output_path, quality):
    """Compress an image and save it to the output path."""
    with Image.open(input_path) as img:
        if img.mode == 'RGBA':
            # Create a white background and paste the image on it
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
            img = background

        img.save(output_path, 'JPEG', quality=quality, optimize=True, progressive=True)

def compress_images_in_folder(input_folder, output_folder, quality):
    """Compress all images in the input folder and save them to the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

            try:
                compress_image(input_path, output_path, quality)
                print(f"Compressed {filename} and saved to {output_folder}")
            except Exception as e:
                print(f"Failed to compress {filename}: {e}")

if __name__ == '__main__':
    input_folder = './input'
    output_folder = './output'
    compress_images_in_folder(input_folder, output_folder, quality=50)
