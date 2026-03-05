from PIL import Image, ImageDraw, ImageFont
import os
import math

# Configuration
WIDTH = 4096
HEIGHT = 4096
GRID_SIZE = 16 # 16x16 grid = 256 images
CHUNK_SIZE = WIDTH // GRID_SIZE
OUTPUT_DIR = '/publish'
FLAG_FILE = '/flag'
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def generate_image():
    # Read flag
    with open(FLAG_FILE, 'r') as f:
        flag = f.read().strip()

    # Create large image
    print(f"Creating {WIDTH}x{HEIGHT} image...")
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Calculate font size to fill the square roughly
    # We want the text to be large. Let's try to fit it in multiple lines to make a "square" block of text.
    # Flag: D4S_CTF{all_work_no_play} (26 chars)
    # Maybe break it into lines?
    # D4S_CTF
    # {all_wor
    # k_no_pla
    # y}
    # 
    # Or just one huge line in the middle? "squared message" suggests a block shape.
    # Let's try to wrap it.

    lines = [
        "D4S_CTF",
        "{all_wo",
        "rk_no_p",
        "lay}"
    ]
    # This is roughly square-ish in char count (7, 7, 7, 4).

    font_size = 500 # Start large
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Calculate text block size
    max_line_width = 0
    total_height = 0
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=font)
        w = right - left
        h = bottom - top
        max_line_width = max(max_line_width, w)
        total_height += h

    # Adjust font size if it doesn't fit or is too small
    # For now, let's just center it.

    x_start = (WIDTH - max_line_width) // 2
    y_start = (HEIGHT - total_height) // 2

    current_y = y_start
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=font)
        w = right - left
        h = bottom - top # Height of this line

        draw.text(((WIDTH - w) // 2, current_y), line, font=font, fill='black')
        current_y += h + 25 # Add some spacing

    # Save chunks
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Splitting image into chunks...")
    count = 0
    for y in range(0, HEIGHT, CHUNK_SIZE):
        for x in range(0, WIDTH, CHUNK_SIZE):
            box = (x, y, x + CHUNK_SIZE, y + CHUNK_SIZE)
            chunk = img.crop(box)
            filename = f"{count:03d}.png"
            chunk.save(os.path.join(OUTPUT_DIR, filename))
            count += 1
            if count % 10 == 0:
                print(f"Saved {count}/{GRID_SIZE*GRID_SIZE} chunks")

    print("Done.")

if __name__ == "__main__":
    generate_image()
