In this challenge we are given a jpg file

The challenge title indicates that the flag is hidden in the image metadata
We can get this data using imagemagick

So: identify -verbose meme-3.jpg | grep nactf

This gives us the flag:

nactf{m3ta_m3ta_m3ta_d3f4j}
