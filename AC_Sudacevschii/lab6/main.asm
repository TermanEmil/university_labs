.model small
org 100h

.DATA
    student_name        db 'Emil Terman$'
    target_chars        db 'aeiouAEIOU$'
    matching_pos        DB 10
    notmatching_pos     DB 14
    
    matching_msg        db 'Matching: $'
    notmatching_msg     db 'Not Matching: $'
    
    color               db 1h
    bg_color            db 5h
    
    square_w            dd 30
    square_h            dd 50
    
.CODE
begin:
    mov ax, @DATA
    mov ds, ax
    
    call draw_square
    ;call find_chars
    
    hlt

find_chars proc
    ; Print first msg
    mov dx, offset matching_msg
    mov ah, 9
    int 21h     
    
    ; set cursor pos
    mov dh, 1
    mov dl, 0
    mov ah, 02h 
    int 10h
    
    ; Print second msg
    mov dx, offset notmatching_msg
    mov ah, 9
    int 21h 
      
    mov si, 0
    main_string_loop:      
    
        mov di, 0        
        substr_loop:
            mov al, student_name[si]
            cmp al, target_chars[di]
            
            je  CHAR_EQ 
            jne CHAR_NOT_EQ
            
            CHAR_EQ:
                ; set cursor pos to row = 0 | col = matching_pos
                mov dh, 0
                mov dl, matching_pos
                mov ah, 02h
                int 10h
                
                inc matching_pos
                
                mov al, student_name[si]
                call print_al_char   
                
                jmp END_OF_SUBSTR_LOOP
     
            CHAR_NOT_EQ:
                ; Do nothing

            inc di
            
            ; Next iter if not end of str
            cmp target_chars[di], '$'
            jne substr_loop
        
        PRINT_ON_SECOND_LINE_IF_NO_MATCH:
            mov dh, notmatching_pos
            sub dh, 13
            mov dl, notmatching_pos
            mov ah, 02h
            int 10h
            
            inc notmatching_pos
            
            mov al, student_name[si]
            call print_al_char
        
        END_OF_SUBSTR_LOOP:
            inc si
            
            ; Next iter if it's not the end of str        
            cmp student_name[si], '$'
            jne main_string_loop

        RET
endp find_chars

; print the character in AL
print_al_char proc
    ; increment color and if it's greater than
    ; 0Fh, set it to 01h
    inc color
    
    cmp color, 0Fh
    jl LESS_COLOR        
        mov color, 01h
    
    LESS_COLOR:
    
    inc bg_color
    cmp bg_color, 0Fh
    jl LESS_BG_COL
        mov bg_color, 01h
    
    LESS_BG_COL:
    
    ; combine the color fron color and bg_color into bl
    mov bl, bg_color
    shl bl, 4
    add bl, color
    
    mov bh, 0                   ; leave it 0
    mov cx, 1                   ; nr of times
    mov ah, 09h                 ; interrupt value
    int 10h
    RET        
endp print_al_char

draw_square proc
    ; set graphics video mode
    mov al, 13h
    mov ah, 0
    int 10h
    
    mov cx, square_w
    width_loop:
        mov si, cx
        
        mov cx, square_h
        height_loop:
            mov di, cx
        
            mov al, 1100b
            mov cx, 0
            mov dx, cx
            mov ah, 0ch
            int 10h
            
            mov al, 1100b
            mov cx, square_w
            mov dx, cx
            mov ah, 0ch
            int 10h
            
            mov cx, di
            loop height_loop 
        
        mov cx, si
        loop width_loop
    
    RET   
endp draw_square

end begin
