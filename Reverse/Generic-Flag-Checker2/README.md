To find the flag of of this program using a static string search wont work.
However running ltrace we see that there is a string compare.  The end of the flag is cut off so we need to extend this with the '-s' flag.

ltrace -s 60 ./gfc2

nactf{s0m3t1m3s_dyn4m1c_4n4lys1s_w1n5_gKSz3g6RiFGkskXx}
