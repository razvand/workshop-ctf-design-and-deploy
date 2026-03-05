# Publish

This directory is responsible for packaging the challenge artifacts for distribution to players.

## Prerequisites

1.  Ensure you have run the generator in the `src/` directory.
2.  Ensure this directory contains the 256 generated image files (`000.png`, `001.png`, ..., `255.png`).

## Creating Distribution Archive

To create a zip archive (`broken_glass.zip`) containing the 256 image files:

1.  **Build the Publisher Image**

    ```console
    docker build -t broken-glass-pub .
    ```

2.  **Generate the Archive**

    Run the container, mounting the current directory to `/publish`. The container will zip the contents of `/publish` (the images) and overwrite/create `broken_glass.zip`.

    ```console
    docker run --rm -v "$(pwd):/publish" broken-glass-pub
    ```

    The `broken_glass.zip` file will appear in this directory.

## Clean

To remove the generated archive:

```console
rm broken_glass.zip
```
