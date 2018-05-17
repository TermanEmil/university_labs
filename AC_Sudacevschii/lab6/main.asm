.model small
org 100h

.DATA
    student_name        db 'Emil Terman$'
    target_chars        db 'aeiouAEIOU$'
    matching_pos        DB 10
    notmatching_pos     DB 14
    
    welcome_msg         db 'Welcome, press any key to continue$'
    
    matching_msg        db 'Matching: $'
    notmatching_msg     db 'Not Matching: $'
    
    draw_square_msg     db 'Press y to draw square$'
    find_chars_msg      db 'Press y to find chars: $'
    
    color               db 1h
    bg_color            db 5h
    
    square_w            dd 50
    square_h            dd 70
    
    square_padding_x    dd 130
    square_padding_y    dd 130
    
    add_tmp             dd ?
    
.CODE

SET_CURS_POS MACRO pos_x, pos_y
    mov dh, pos_y
    mov dl, pos_x
    mov ah, 02h 
    int 10h    
ENDM

PRINT_STR MACRO str
    mov dx, offset str
    mov ah, 9
    int 21h        
ENDM               

SET_PIXEL MACRO color, pos_x, pos_y
    mov dx, pos_y
    mov cx, pos_x
    mov al, color
    mov ah, 0ch
    int 10h    
ENDM

END_PROG MACRO
    mov ax, 4c00h
    int 21h    
ENDM

begin:
    mov ax, @DATA
    mov ds, ax
    
    PRINT_STR welcome_msg
    
    ; Disable blinking
    mov ch, 32
    mov ah, 1
    int 10h
    
    ; Wait for keyboard stroke
    mov ah, 00h
    int 16h
    
    ; set graphics video mode
    mov al, 13h
    mov ah, 0
    int 10h
    
    PRINT_STR draw_square_msg
    
    ; Wait for keyboard input (without echo)
    mov ah, 00h
    int 16h
    
    ; Check for keystroke in keyboard buffer
    mov ah, 01h
    int 16h
        
        ; If Yes ('y') then draw square
        cmp al, 'y'
        jne DONT_DRAW_SQUARE
            call draw_square
        DONT_DRAW_SQUARE:
    
    SET_CURS_POS 0, 0
    PRINT_STR find_chars_msg
    
    ; read character from standard input, with echo, result is stored in AL
    mov ah, 1
    int 21h
        
        ; If Yes then find chars
        cmp al, 'y'
        jne DONT_FIND_CHARS
            call find_chars
        DONT_FIND_CHARS:
        
    END_PROG

find_chars proc
    SET_CURS_POS 0, 1
    PRINT_STR matching_msg
    SET_CURS_POS 0, 2
    PRINT_STR notmatching_msg
      
    mov si, 0
    main_string_loop:      
    
        mov di, 0        
        substr_loop:
            mov al, student_name[si]
            cmp al, target_chars[di]
            
            je  CHAR_EQ 
            jne CHAR_NOT_EQ
            
            CHAR_EQ:
                SET_CURS_POS matching_pos, 1
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
            sub dh, 12
            SET_CURS_POS notmatching_pos, dh
            
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
    
    mov cx, square_h
    height_loop:
        mov si, cx
        
        mov bx, si
        add bx, square_padding_y 
        SET_PIXEL 1100b, square_padding_x, bx
        
        mov dx, si
        add dx, square_padding_y
        
        mov cx, square_padding_x
        add cx, square_w
        SET_PIXEL 1100b, cx, dx
        
        mov cx, si
        loop height_loop
    
    mov cx, square_w
    width_loop:
        mov si, cx
        
        mov cx, si
        add cx, square_padding_x  
        SET_PIXEL 1100b, cx, square_padding_x
        
        mov dx, square_padding_y
        add dx, square_h
        
        mov cx, square_padding_x
        add cx, si
        SET_PIXEL 1100b, cx, dx
        
        mov cx, si
        loop width_loop
    
    RET   
endp draw_square

end begin
