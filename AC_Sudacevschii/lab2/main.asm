.model small
.STACK 100H
.DATA
    x DB 12H, 34H
    y DW 6688H, 7799H
    z DD 11223344H

; Main code
.CODE
    begin:
        ; Task 1
        mov ax, DATA
        mov ds, ax
        ;mov al, x[0]
        ;mov ah, x[1]
        ;mov bx, y[0]
        ;mov cx, y[2]
        ;mov si, z[0]
        ;mov di, z[2]  
        
        ; Task 2
        ;PUSH ax
        ;PUSH bx
        ;PUSH cx
        ;PUSH si
        ;PUSH di
        
        ; Reset
        ;xor ax, ax
        ;xor bx, bx
        ;xor cx, cx
        ;xor si, si
        ;xor di, di
        
        ;pop di
        ;pop si
        ;pop cx
        ;pop bx
        ;pop ax
        
        LEA bx, Y
        mov cx, [bx]
        mov dx, [bx][2]
        
        xor cx, cx
        mov bx, 5H
        mov cl, [bx]
        mov ch, [6H]
        
        xor cx, cx
        PUSH 7H
        POP bx
        mov cl, [bx]
        
        xor cx, cx
        LEA bx, Y
        LDS cx, bx 