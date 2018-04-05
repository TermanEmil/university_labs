.model small

.DATA
    ;X DB    01h
    ;Z DB    02h
    
    X DB    54h
    Z DB    57h
    
    Y DW    0000h
    
.CODE
begin:
    mov ax, @DATA
    mov ds, ax
    
    ;    8(Z + X) - 17  if Z - X <= 2
    ;Y = 
    ;    X / 2 - 42 + Z if Z - X > 2
    
    ; cmp Z, X + 2
    mov al, Z
    mov ah, X
    add ah, 2
    cmp al, ah
    
    je EQUAL
    jg GREATER
    jmp LESS
    
    EQUAL:
        jmp LESS
    GREATER:
        mov ax, 0h
        mov bx, 0h
        
        mov al, X
        shr ax, 1
        sub ax, 42
        
        mov bl, Z
        add ax, bx
        
        mov Y, ax
        jmp ENDPROG
    LESS:
        mov ax, 0h
        mov bx, 0h
        
        mov al, Z
        mov bl, X
        
        add ax, bx
        mov cl, 3
        shl ax, cl
        
        sub ax, 17
        mov Y, ax
        
        jmp ENDPROG
    
    ENDPROG:
    
end begin    
    