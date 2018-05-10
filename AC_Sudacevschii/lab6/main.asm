.model small

.DATA
    student_name        db 'Emil Terman', 0
    target_chars        db 'aeiou', 0
    matching_col_pos    DW 00h
    
    
.CODE
begin:
    mov ax, @DATA
    mov ds, ax
    
    call find_chars

find_chars proc  
    mov si, 0
    main_string_loop:
        
        mov di, 0        
        substr_loop:
            mov al, student_name[si]
            cmp al, target_chars[di]
            
            je CHAR_EQ 
            jne CHAR_NOT_EQ
            
            CHAR_EQ:
                mov dh, 0
                ; print matching
                mov al, student_name[si]    ; char
                mov bh, 0                   ; leave it 0
                mov bl, 5Ch                 ; color: high = bg | low = font
                mov cx, 1                   ; nr of times
                mov ah, 09h                 ; interrupt value
                int 10h
                
                ; Move cursor one char forward
                mov ah, 03h                 ; get current cursor pos
                int 10h
                
                inc dl
                mov ah, 02h                 ; set cursor pos
                int 10h
                        
            CHAR_NOT_EQ:
                mov dh, 1
            
            
            
            add di, 1
            
            ; Next iter if not end of str
            cmp target_chars[di], 0
            jne substr_loop
            
        add si, 1
        
        ; Next iter if it's not the end of str        
        cmp student_name[si], 0
        jne main_string_loop
    
   
endp find_char

end begin
