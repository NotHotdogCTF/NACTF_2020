In this challenge we are given a webpage with many different forms that take in a username and password

By inspecting the page code we can see at the bottom the verify() function

This specifies the username and password (admin, password123)

Entering this into the first button prompts an incorrect response. We can then check and see that only one form calls the verify function.

In the code we see that this is form 673.

By then navigating to form 673 and entering the username and password we can then receive the flag

nactf{cl13n75_ar3_3v11}
