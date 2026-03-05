from pwn import *

exe = ELF('/publish/piece_of_cake')

print(f"Main: {hex(exe.symbols['main'])}")
print(f"Puts@PLT: {hex(exe.plt['puts'])}")
print(f"Puts@GOT: {hex(exe.got['puts'])}")

# Check gadgets
rop = ROP(exe)
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret = rop.find_gadget(['ret'])[0]

print(f"Pop RDI: {hex(pop_rdi)}")
print(f"Ret: {hex(ret)}")
