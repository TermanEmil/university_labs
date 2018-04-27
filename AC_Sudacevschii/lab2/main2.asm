.model  small
.stack  100h
.data   
    X DB 11h, 22h
    Y DW 3344h, 5566h, 7788h
    Z DD 99AABBCCh 

.code
begin:
    mov ax, @data
    mov ds, ax
    
    ; Task 1
    ;mov ax, Y
    ;mov bx, Y+2
    ;mov cx, Y+4
    
    ; Task 2
    ;push ax
    ;push bx
    ;push cx
    ;mov ax, 0
    ;mov bx, 0
    ;mov cx, 0
    ;pop cx
    ;pop bx
    ;pop ax
    
    ; Task 3
    ; 1 Immediate Addressing Mode
    xor ax, ax
    mov ax, 1122h
    
    ;2  Register Addressing Mode
    xor bx, bx
    mov bx, ax
    
    ; 3 Direct Addressing Mode
    xor ax, ax
    mov ax, [0006h]
    
    ; 4 Register Indirect Addressing Mode
    xor bx, bx
    lea bx, Y
    mov ax, [bx]
    
    ; 5 Based Addressing Mode
    xor ax, ax
    mov ax, [bx+0002h]
    
    ; 6 Index Addressing Mode
    xor si, si
    lea si, [Y+2]
    xor ax, ax
    mov ax, 0004h[si]
    
    ;7 Based Indexed Addressing Mode
    xor ax, ax
    mov ax, [bx][si]
    
    ;8 Based Indexed Plus Displacement Mode
    xor ax, ax
    mov ax, 0002h[bx+si]
 





