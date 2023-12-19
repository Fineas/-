section .data
    file_name db "flag.txt", 0     ; Null-terminated file_name

section .bss
    file_content  resb 1024             ; Reserve a 1024 byte file_content

section .text
    global _start

_start:
    ; Open the file "flag.txt" with read-only flag
    mov rax, 2                    ; Syscall number for sys_open
    lea rdi, [file_name]          ; First argument: file_name
    mov rsi, 0                    ; Second argument: flags (0 for read only)
    syscall                       ; Invoke the kernel
    
    ; Read the contents of the file into file_content
    mov rdi, rax                  ; Move the file descriptor into rdi
    mov rax, 0                    ; Syscall number for sys_read
    lea rsi, [file_content]       ; Second argument: file_content
    mov rdx, 0x123                ; Third argument: count (maximum allowed size)
    syscall                       ; Invoke the kernel
    
    ; Write the contents of file_content to standard output
    mov rdx, rax                  ; Save the number of bytes read for writing
    mov rax, 1                    ; Syscall number for sys_write
    mov rdi, 1                    ; First argument: file descriptor (1 for stdout)
    lea rsi, [file_content]       ; Second argument: file_content, already contains file_content
    syscall                       ; Invoke the kernel

    ; Exit program
    mov rax, 60                   ; Syscall number for sys_exit
    mov rdi, 0                    ; First argument: exit status (0 for success)
    syscall                       ; Invoke the kernel
