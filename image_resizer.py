from PIL import Image
def resize_image(input_path, output_path, new_width, new_height):
        with Image.open(input_path) as img:
            # Resize the image
            img = img.resize((new_width, new_height))
            # Save the resized image
            img.save(output_path)
            print(f"Image resized and saved to {output_path}")
if __name__ == "__main__":
    input_path = "dice1.png"
    output_path = "output.png"
    width = int(input("Enter new width: "))
    height =int(input("Enter new width: "))
    resize_image(input_path, output_path, width, height)
