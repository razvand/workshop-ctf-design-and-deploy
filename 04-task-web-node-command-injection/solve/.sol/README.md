# Solve

## Build Solver

```console
docker build -t node-cmd-injection-solver .
```

## Run Solver

Against local deployment:
```console
# Using host networking (Linux)
docker run --rm --network host node-cmd-injection-solver python3 exploit.py http://127.0.0.1:3000

# Or using host.docker.internal (Mac/Windows)
docker run --rm node-cmd-injection-solver python3 exploit.py http://host.docker.internal:3000
```
