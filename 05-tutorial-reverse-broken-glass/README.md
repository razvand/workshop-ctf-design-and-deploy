# Reverse Broken Glass

**Reverse Broken Glass** is a forensics/scripting CTF challenge.
The goal is to recover a flag hidden within a large image that has been shattered into 256 smaller pieces.

## Requirements

The only requirement to run, build, deploy, and solve this challenge is **Docker**. No other tools (like Python, ImageMagick) are required on your host machine.

This setup is designed to work seamlessly on:

* **Linux**
* **Windows** (via Docker Desktop)
* **macOS** (via Docker Desktop)

## Challenge Structure

This repository is organized into three main directories, each serving a specific phase of the challenge lifecycle:

1. **`src/`**:
   * **Purpose**: Contains the generator script (`generate.py`) and the build environment.
   * **Action**: Generates the 256 image fragments (`000.png` to `255.png`).
   * **Output**: The image files in the `publish/` directory.

2. **`publish/`**:
   * **Purpose**: Prepares the challenge artifacts for distribution to players.
   * **Action**: Packages the image fragments into a zip archive (`broken_glass.zip`).
   * **Output**: A zip file ready to be shared with contestants.

3. **`solve/`**:
   * **Purpose**: Contains the solution script (`solve.py`) and a solver environment.
   * **Action**: Stitches the image fragments back together to reveal the flag.

## The Flag

The flag for this challenge is stored in the `flag` file in the root directory.

## Getting Started

To get started with this challenge, follow the instructions in the `README.md` file within each directory, starting with `src/` to generate the images.
