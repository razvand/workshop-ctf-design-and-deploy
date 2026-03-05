#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Gadget to pop rdi; ret
// This might be optimized out if not used, so we use a trick or just inline asm.
void __attribute__((noinline)) gadgets(void)
{
    __asm__("pop %rdi; ret");
}

int main(int argc, char **argv)
{
    if (argc > 1000) gadgets();

	char name[64];

    setvbuf(stdout, NULL, _IONBF, 0);

    // Use puts to ensure it's in the GOT/PLT for easy leaking
	puts("Tell me your name: ");
    
    // Vulnerability: Buffer overflow (read 256 bytes into 64-byte buffer)
	read(0, name, 256);
	printf("Hello, %s", name);
	return 0;
}
