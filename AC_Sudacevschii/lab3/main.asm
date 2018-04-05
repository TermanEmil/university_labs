.model small

.DATA
    a DW    0014h
    b DB      01h
    n DW    0005
    x DW    0000
    
.CODE
begin:
    mov ax, @DATA
    mov ds, ax
    
    mov si, 0
    mov x[si], 0
    
    ; xi = xi-1 - 3b + a/4
    ; 3b
    mov AL, 3
    mov BL, b
    mul BL
    mov DX, AX
    
    ; a / 4 == a << 2
    mov AX, a
    mov CL, 2
    shr AX, CL

    
    ; a/4 - 3b
    sub AX, DX 
    
    mov cx, n
    sum_loop:
        mov x[si + 2], AX
        mov BX, x[si]
        add x[si + 2], BX
        add si, 2
        loop sum_loop
    
end begin    
    