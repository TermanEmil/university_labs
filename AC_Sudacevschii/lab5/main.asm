.model small

.DATA
    X   DW  05h, 01h, 02h, 03h, 04h, 05h, 06h, 07h, 08h, 09h
    N   DW  10
    l1  DW  0
    l2  DW  0
    
.CODE
begin:
    mov ax, @DATA
    mov ds, ax
    
    call SumProc    
    call OddEven
Exit:
hlt

SumProc proc
    mov cx, N
    
    mov ax, 0
    mov si, 0
    
    sum_loop:
        add ax, X[si]
        add si, 2
        loop sum_loop
    ret ; result in ax
endp SumProc

OddEven proc
    mov dl, 2
    div dl
    
    cmp ah, 0
    je EVEN
    jg ODD
    
    ODD:        
        mov dx, n
        sub dx, 3 
        mov L1, dx
        
        mov dx, n
        mov L2, dx
        
        jmp DONE
                        
    EVEN:
        mov L1, 0
        mov L2, 3
        jmp DONE
        
    DONE:
    
    mov dx, l2
    sub dx, l1
    mov cx, dx
    
    mov dx, l1
    shl dx, 1
    mov si, dx
    
    mov ax, 1
    
    mult_loop:
        mov BX, X[si]
        mul BX
        add si, 2
        loop mult_loop    
    ret    
endp OddEven

end begin