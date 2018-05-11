.model small

; xi = xi-1 - 3b + a/4

.DATA
    a   DW    0016
    b   DB    01h
    n   DW    50
    SUM DD    0000h
    x   DW    ?
    
.CODE
begin:
    mov ax, @DATA
    mov ds, ax
    
    mov si, 0
    mov x[si], 0
    
    ; 3b
    mov AL, 3
    mov BL, b
    mul BL
    mov DX, AX
    
    ; a / 4 == a << 2
    mov AX, a
    mov CL, 2
    shr AX, CL  ; shift right

    
    ; a/4 - 3b
    sub AX, DX 

    ; cx = n    
    mov cx, n

    ; while cx is not 0
    sum_loop:
        mov x[si + 2], AX
        mov BX, x[si]
        add x[si + 2], BX
        
        ; Add carry from the above operation
        mov BX, x[si + 2]
        add SUM, BX
        adc SUM[2], 0       
        
        add si, 2
        loop sum_loop
    
end begin    
    