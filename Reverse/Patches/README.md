While reversing this challenge we can see that there is a function called 'print_flag' that is never called.
Since we can tell from the disassembly that the flag will be generated here we can jump to that location in GDB to read the flag.

1.) First run the patches in gdb:  gdb patches
2.) Set a break at main: break *main
3.) Jump to 'print_flag': set $pc = print_flag
4.) Continue program to get flag: s

nactf{unl0ck_s3cr3t_funct10n4l1ty_w1th_b1n4ry_p4tch1ng_L9fcKhyPupGVfCMZ}
