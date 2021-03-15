In this challenge we are given a .c file and an address to netcat into

Here we can see that we are asked for a number to get the flag

From looking at the code we can see that the number must satisfy an arithmetic condition.

It must be an unsigned integer and when added to 2718281828 it must equal 42.

So, we must overflow the integer to wrap around to 42. 

We wrote a program (arithmetic.c) to do the addition for us to account for any mistakes.

Note: when you overflow an unsigned integer it starts again at 0 so you must account for that as well.

This program gives us our number: 1576685510

Entering this to the server gives us our flag.

nactf{0verfl0w_1s_c00l_6e3bk1t5}
