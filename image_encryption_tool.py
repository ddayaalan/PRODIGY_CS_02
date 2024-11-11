
from PIL import Image
import numpy as np

def load_image(image_path):
    """Loads an image and returns it as a numpy array."""
    image = Image.open(image_path).convert("RGB")
    return np.array(image)

def save_image(image_array, save_path):
    """Saves a numpy array as an image."""
    image = Image.fromarray(image_array)
    image.save(save_path)

def encrypt_image(image_array, key):
    """Encrypts the image by applying XOR with a key to each pixel."""
    encrypted_image = image_array ^ key
    return encrypted_image

def decrypt_image(encrypted_array, key):
    """Decrypts the image by applying XOR with the same key."""
    decrypted_image = encrypted_array ^ key
    return decrypted_image

def main():
    # Load the image
    image_path = "E:\Ethical Hacking Project\Prodialogy infotech\Task 2\input_image.png"  # Replace with your image path
    image_array = load_image(image_path)
    
    # Define a key for encryption (must be between 0-255)
    key = 123  # Simple integer key for demonstration

    # Encrypt the image
    encrypted_array = encrypt_image(image_array, key)
    save_image(encrypted_array, "encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

    # Decrypt the image
    decrypted_array = decrypt_image(encrypted_array, key)
    save_image(decrypted_array, "decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

if __name__ == "__main__":
    main()
