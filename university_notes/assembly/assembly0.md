### General purpuse

#### AX

#### AL

#### AH

#### BX

#### CX
  Counter.

#### DX
  Partea mai mare a produsului se pastreaza aici.

#### SP
  Stack pointer

#### BP
  Base pointer

#### SI
  Source index.

#### DI
  Destination Index.

### Segment registers
- The mp has 20-bit address bus for 1 MB external memory but inside the CPU registers have 16 bits that can access 64 KB.

1) CS (code segment) - points at the segment containing the current program.
2) DS (data segment) - generally points at the segment where variables are defined
3) ES (extra segment) - extra segment register, it's up to a coder to define.
4)

### Special purpose registers
- **IP**- the instruction pointer o program counter: always points to the next instruction to be executed. It contains the offset (displacement) of the next instruction from the start address of the code segment.

- **Flags** Registers (or PSW [program status work])

  **Arithmetic flags**
    - 0bit CF - carry Flags
    - 2bit PF - parity Flag this flag is set to 1 when there is even number of one bits in result. In the last 8 bits.
    - 4bit AF - auxiliary flag - set to 1 when there is an unsigned overflow for low nibble (4 bits). When there is a carry from the last 4 bits to the next 4 bits.
    - 6bit ZF - zero flag - set to 1 if the result is 0. Actually, it's the first bit.
    - 7bit SF - sign flag set to 1 when the result is negative.
    - 11bit OF - overflow bit. If two positive numbers are added and a negative one is recieved, then this flag is set to 1, the same goes when negative + negative.

  **Control flags**
    - 8bit TF - trap flags
    - 9bit IF - interrupt enabled
    - 10b DF - directional flag

#### Ex:
~~~
  342A H +
  57E2 H
  ------
  8COC

  0011 0100 0010 1010 +
  0101 0111 1110 0010
  -------------------
  1000 1100 0000 1100

  CF 0
  PF 1
  OF 1
  ZF 0
  AF 0
  SF 1
~~~

~~~
    E42AH +
    96B8H
    -----
[1] 7AE2

  1110 0100 0010 1010
  1001 0110 1011 1000
  -------------------
<-0111 1010 1110-0010

  CF 1
  PF 1
  OF 1
  ZF 0
  AF 1 (la sageata dupa perechea din dreapta)
  SF 0
~~~

~~~
    C739H +
    38C7H
    -----
[1] 0000H

CF 1
PF 1
OF 0
ZF 1
AF 1
SF 0
~~~
