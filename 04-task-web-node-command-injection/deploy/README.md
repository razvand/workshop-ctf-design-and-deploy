# Deploy

## Build and Run

```console
# Build the image (from the parent directory context)
docker build -t node-cmd-injection -f Dockerfile ..

# Run the container
docker run -d --rm -p 3000:3000 --name node-cmd-injection-container node-cmd-injection
```

The challenge will be available at `http://localhost:3000`.
