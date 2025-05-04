import os
import tkinter as tk

def load_product_image(product_name, image_url=None, assets_dir="assets"):
    """
    Load product image or placeholder if not available.
    Args:
        product_name (str): Name of the product (for error messages)
        image_url (str, optional): Path to the product image
        assets_dir (str): Directory containing assets
    Returns:
        tk.PhotoImage or None: The loaded image or None if loading failed
    """
    try:
        # If image_url is provided, try to load it
        if image_url:
            image_path = os.path.join(assets_dir, image_url)
            if os.path.exists(image_path):
                try:
                    image = tk.PhotoImage(file=image_path)
                    # Resize the image to fit the card
                    width = image.width()
                    height = image.height()
                    max_size = 200  # Maximum dimension for the image
                    
                    if width > height:
                        subsample = max(1, width // max_size)
                    else:
                        subsample = max(1, height // max_size)
                        
                    image = image.subsample(subsample, subsample)
                    return image
                except tk.TclError as e:
                    print(f"Error loading image for {product_name}: {e}")
        
        # If no image_url or image not found, use placeholder
        placeholder_path = os.path.join(assets_dir, "Logo.png")
        if os.path.exists(placeholder_path):
            try:
                image = tk.PhotoImage(file=placeholder_path)
                image = image.subsample(4, 4)  # Make placeholder smaller
                return image
            except tk.TclError as e:
                print(f"Error loading placeholder image: {e}")
                
        return None
    except Exception as e:
        print(f"Error in load_product_image: {e}")
        return None 