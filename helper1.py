#!/usr/bin/env python

import sys
from pwn import *


context.arch = 'amd64' # [ amd64 | i386 ]
context.os = 'linux'
context.endian = 'little'
context.word_size = 64 # [ 64 | 32]
# ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING']
context.log_level = 'INFO'
context.terminal = ['tmux','splitw','-h']


program_name = './jail'
binary = ELF(program_name)
p = process(program_name)


if __name__ == "__main__":

    '''
    will attach gdb automatically to the "jail" process (program)
    note that for the given configuration, it only wortks from within tmux
    '''
    gdb.attach(p)

    '''
    the asm function will ASSEMBLE (convert from assembly to bytecode - numbers)
    the given assembly, for the architecture specified in the context (see line 7)
    '''
    payload = asm("""
    mov rax, 0x1337 ; with love from FeDEX
    """)

    '''
    the same api (functions) can be used to interact with the process 
    as you would do with the remote connection
    '''
    p.sendline(payload)

    p.interactive()
