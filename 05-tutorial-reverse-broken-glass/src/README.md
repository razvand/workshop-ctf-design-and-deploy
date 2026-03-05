# Source / Generator

This directory contains the source code generator and build instructions for the "Reverse Broken Glass" challenge.

## Building

To generate the challenge images in a reproducible environment (Docker), follow these steps.

1. **Build the Generator Image**

   ```console
   docker build -t broken-glass-gen .
   ```

1. **Generate the Images**

   Run the container, mounting the `publish/` directory to `/publish` and the `flag` file to `/flag`.

   ```console
   docker run --rm -v "$(pwd)/../publish:/publish" -v "$(pwd)/../flag:/flag" broken-glass-gen
   ```

   This command will:
   1. Read the `../flag` file.
   1. Generate a large image with the flag.
   1. Split it into 256 chunks.
   1. Save the chunks to `../publish/000.png` through `../publish/255.png`.

## Clean

To clean up generated images:

```console
rm ../publish/*.png
```
