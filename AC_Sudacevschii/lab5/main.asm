.model small

.DATA
    X   DW  05h, 01h, 02h, 03h, 04h, 05h, 06h, 07h, 09h, 09h
    N   DW  10
    l1  DW  0
    l2  DW  0
    
.CODE
begin:
    mov ax, @DATA
    mov ds, ax
    
    call sum_proc    
    call odd_even
Exit:
hlt

; Compute sum of all numbers in the array X
;  and return in AX
sum_proc proc
    mov cx, N
    
    mov ax, 0
    mov si, 0
    
    sum_loop:
        add ax, X[si]
        add si, 2
        loop sum_loop
    ret ; result in ax
endp sum_proc

; If ax is even: multiply first 3 numbers
;          else: multiply last 3 numbers
odd_even proc
    mov dl, 2
    div dl
    
    ; After division, AH contains the remainder
    cmp ah, 0
    je EVEN
    jg ODD
    
    ; Set L1 to n - 3 and L2 to n
    ODD:        
        mov dx, n
        sub dx, 3 
        mov L1, dx
        
        mov dx, n
        mov L2, dx
        
        jmp DONE
    
    ; set L1 to 0 and L2 to 3                    
    EVEN:
        mov L1, 0
        mov L2, 3
        jmp DONE
        
    DONE:
        ; Compute in CX the number of iterations    
        mov dx, l2
        sub dx, l1
        mov cx, dx
        
        ; SI is the index of the element to start with
        ; SI = l1 * 2
        mov dx, l1
        shl dx, 1
        mov si, dx
        
        ; Init the multiplication
        mov ax, 1
    
    mult_loop:
        mov BX, X[si]
        mul BX
        add si, 2
        loop mult_loop    
    ret    
endp odd_even

end begin