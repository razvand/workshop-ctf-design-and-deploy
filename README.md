# Designing and Deploying CTF Cybersecurity Challenges

This repository contains materials for the "CTF Design and Deploy" workshop.
The goal is to teach how to create, package, and deploy Capture The Flag (CTF) challenges using Docker, ensuring reproducibility and ease of use.

## Repository Structure

The repository is organized into a series of modules, alternating between tutorials (guided learning) and tasks (independent exercises).

### Modules

1. **[01-tutorial-pwn-call-shell](./01-tutorial-pwn-call-shell)**
   * **Category**: Binary Exploitation (Pwn)
   * **Topic**: Simple Stack Buffer Overflow (x86)
   * **Goal**: Overwrite the return address to call a `win()` function.

1. **[02-task-rop-call-shell](./02-task-rop-call-shell)**
   *  **Category**: Binary Exploitation (Pwn)
   *  **Topic**: Return Oriented Programming (ROP) (x86-64)
   *  **Goal**: Construct a ROP chain to call `system("/bin/sh")`.

1.  **[03-tutorial-web-command-injection](./03-tutorial-web-command-injection)**
    * **Category**: Web Exploitation
    * **Topic**: OS Command Injection (PHP)
    * **Goal**: Inject shell commands into a vulnerable PHP script.

1. **[04-task-web-node-command-injection](./04-task-web-node-command-injection)**
   * **Category**: Web Exploitation
   * **Topic**: OS Command Injection (Node.js)
   * **Goal**: Exploit a vulnerable Node.js application.

1. **[05-tutorial-reverse-broken-glass](./05-tutorial-reverse-broken-glass)**
   * **Category**: Reverse Engineering / Forensics
   * **Topic**: Scripting & Image Reconstruction
   * **Goal**: Stitch together 256 image fragments to reveal a flag.

1. **[06-task-reverse-exec-encrypt](./06-task-reverse-exec-encrypt)**
   * **Category**: Reverse Engineering
   * **Topic**: Static Binary Analysis
   * **Goal**: Recover an encryption key hidden in machine code instructions to decrypt the flag.

## Challenge Structure

Each challenge follows a consistent directory structure:

* **`src/`** (or `build/`): Contains the source code and build scripts (Dockerfiles) to generate the challenge artifacts (binaries, source files, etc.).
* **`publish/`**: Contains the logic to package the challenge for distribution to contestants (e.g., creating zip files).
* **`deploy/`** (for network services): Contains the configuration to host the challenge as a network service (using Docker and `xinetd` or web servers).
* **`solve/`**: Contains a reference solution, including a solver script and a Docker environment to run it.
* **`flag`**: The flag file for the challenge.
* **`README.md`**: Specific instructions for that challenge.

## Requirements

* **Docker**: All steps (building, deploying, solving) are containerized. You only need Docker installed on your machine.
* No other tools (like GCC, Python, PHP, Node.js) are strictly required on the host system.

## Usage

Navigate to a challenge directory and follow the `README.md` instructions. The general workflow is:

1. **Generate**: Build the challenge artifacts in `src/` (or `build/`).
1. **Publish**: Package the artifacts in `publish/`.
1. **Deploy**: (If applicable) Start the challenge service in `deploy/`.
1. **Solve**: Run the solution script in `solve/` to verify the challenge is working correctly.
