from PIL import Image
import os
import sys

# Configuration
# WIDTH = 16384
# HEIGHT = 16384
# GRID_SIZE = 16
# CHUNK_SIZE = WIDTH // GRID_SIZE
INPUT_DIR = '/images'
OUTPUT_FILE = '/out/solved.png'

def solve():
    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory {INPUT_DIR} does not exist.")
        return

    print(f"Scanning input directory...")
    # Find all png files
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.png')]
    files.sort()
    
    if not files:
        print("No PNG files found.")
        return

    # Assume grid based on file count
    num_files = len(files)
    grid_side = int(num_files**0.5)
    
    if grid_side * grid_side != num_files:
        print(f"Warning: Number of files {num_files} is not a perfect square. Assuming {grid_side}x{grid_side} grid.")

    # Read first image to get chunk size
    first_img = Image.open(os.path.join(INPUT_DIR, files[0]))
    chunk_w, chunk_h = first_img.size
    
    total_width = chunk_w * grid_side
    total_height = chunk_h * grid_side
    
    print(f"Reconstructing image of size {total_width}x{total_height} from {num_files} chunks of {chunk_w}x{chunk_h}...")

    full_img = Image.new('RGB', (total_width, total_height))

    for i, filename in enumerate(files):
        row = i // grid_side
        col = i % grid_side
        
        filepath = os.path.join(INPUT_DIR, filename)
        try:
            chunk = Image.open(filepath)
            full_img.paste(chunk, (col * chunk_w, row * chunk_h))
        except Exception as e:
            print(f"Error processing {filename}: {e}")

        if (i+1) % 10 == 0:
            print(f"Processed {i+1}/{num_files}")

    output_dir = os.path.dirname(OUTPUT_FILE)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Saving to {OUTPUT_FILE}...")
    full_img.save(OUTPUT_FILE)
    print("Done.")

if __name__ == "__main__":
    solve()
