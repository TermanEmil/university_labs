.model small

.DATA
    ;       0      2      4      6      8      10      12     14     16     18
    X   DW  9FFFh, 9FFFh, 9FFFh, 0003h, 0004h, 0009Fh, 0006h, 8FFFh, 9FFFh, 9FFFh
    N   DW  10
    A   DW  0
    B   DW  0
    C   DW  0
    
    RESULT DW 3 DUP(?)
    
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

CPY_VAR MACRO var1, var2
    mov ax, var2
    mov var1, ax    
endm

; If ax is even: multiply first 3 numbers
;          else: multiply last 3 numbers
odd_even proc
    test ax, 1
    jz  EVEN
    
    ODD:        
        CPY_VAR A, X[14]
        CPY_VAR B, X[16]
        CPY_VAR C, X[18]
        
        jmp DONE
                                                 
    EVEN:
        CPY_VAR A, X[0]
        CPY_VAR B, X[2]
        CPY_VAR C, X[4]
        
    DONE:
        ; M.S. == dx == Most Significant part
        ; L.S. == ax == Least Significant part
    
        ; A x B
        mov ax, A
        mul B   ; Mul_1
        
        ; Save the M.S. to bx
        mov bx, dx
        
        ; multiply L.S. with C
        mul C   ; Mul_2
        
        ; Save the L.S. of Mul_2
        ;  as the first bytes of the result
        mov RESULT[0], ax
        
        ; Move the M.S. of Mul_1 to ax
        mov ax, bx
        
        ; Save the M.S. of Mul_2 to bx
        mov bx, dx
        
        ; Multiply M.S. of Mul_1 with C 
        mul C   ; Mul_3
        
        ; Add to L.S. of Mul_3 the M.S. of Mul_2
        add ax, bx
        
        ; The carry is added to the M.S. of Mul_3
        adc dx, 0
        
        mov RESULT[2], ax
        mov RESULT[4], dx
     
    ret    
endp odd_even

end begin