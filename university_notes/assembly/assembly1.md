Quiver
### Main memory model
The number of bits, *l*, needed to distinctly address M bytes in a memory is given by:

<center>
  *l* = log_2M
</center>

### Physical address calculation
Addresses in programs - logical addresses.

The linear address that appears on the address bus - Physical address.

#### Ex
Calculate the offset according to the following physical address (CS = 2000H):
~~~
20002
20000
-----
211
~~~

#### Calculate CS according to the following physical addresses: 10400H (offset is 400H)

~~~
10400H
  400H
------
10000H

CS = 1000H
~~~

#### Which of the following physical addresses belong to the segment with CS = 2400H

~~~
33FFFH
24000H
------
0FFFFH
~~~
~~~
23000H
24000H
------
-F000H (can't be negative)
~~~
~~~
27890H
24000H
------
03890H
~~~
~~~
33000H
24000H
------
0F000H
~~~
~~~
....
----
10000H
~~~
**Result:**
The second can't be because it's negative, and the last, because it's bigger than 16 bits.

## Exam example:
Physical address of the variable is 358BCH when CS = 3234H. Calculate the physical address of the variable when CS is changing 4310H.
~~~
358BCH -
32340H
------
 357CH <-- offset
~~~
~~~
43100H +
 357CH
------
4667CH
~~~
