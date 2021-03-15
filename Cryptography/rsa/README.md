In this challenge we are given the c, e, and n values for the rsa encrypted text.

Normally this would be extremely hard to decipher given the nature of RSA

However, we can hope that the number is not too hard to crack and run a brute force attack against it

We used the tool "RsaCtfTool"

By giving the command python3 RsaCtfTool.py -n {nvalue} -e {evalue} --uncipher {cvalue} we can decode the flag

nactf{sn3aky_c1ph3r}
