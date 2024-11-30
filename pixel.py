from PIL import Image
import numpy as np


def encrypt_image(input_image_path, output_image_path):
    # Open the image
    image = Image.open(input_image_path)
    pixels = np.array(image)

    # Encrypt pixels by applying a simple operation
    encrypted_pixels = (pixels + 50) % 256  # Add 50 to each pixel value
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))

    # Save the encrypted image
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")


def decrypt_image(encrypted_image_path, output_image_path):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_pixels = np.array(encrypted_image)

    # Decrypt pixels by reversing the operation
    decrypted_pixels = (encrypted_pixels - 50) % 256  # Subtract 50 from each pixel value
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))

    # Save the decrypted image
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")


# Example usage:
if __name__ == "__main__":
    encrypt_image('image.jpg', 'encrypted_image.png')
    decrypt_image('encrypted_image.png', 'decrypted_image.jpg')