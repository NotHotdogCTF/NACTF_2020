In this challenge we are given a file "file.txt"

By analyzing the hex of this image we can see that the header shares many characteristics of a PNG file

However, there are some issues. 

By opening another PNG file from the same source (we used the one given in the challenge "static" we can then repair the header

By repairing the header we can then open the image and see the flag

nactf{th3_turn1p5_ar3_tak17g_0v35_skf9}
