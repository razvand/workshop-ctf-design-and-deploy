# Solve

This directory contains the solution script and a containerized environment to run it.

## Prerequisites

1. **Build the Solver Image**

   ```console
   docker build -t broken-glass-solve .
   ```

1. Ensure you have the image fragments in `../publish/` (or somewhere accessible).

## Running the Solution

This runs the solver script `solve.py` which stitches the images together.

You need to mount:

1.  The directory containing the input images (e.g., `../publish`) to `/images`.
1.  A directory for the output file (e.g., `out/`) to `/out`.

```console
# Create output directory
mkdir -p out

# Run solver
docker run --rm \
    -v "$(pwd)/../publish:/images" \
    -v "$(pwd)/out:/out" \
    broken-glass-solve
```

The solved image will be at `out/solved.png`. Open it to view the flag.

## Clean

To remove the solved image:

```console
rm out/solved.png
```
