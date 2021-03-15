This challenge gives us another webpage with a login form

The challenge details lets us know that this is a server side login

Thus, we can assume we need to inject some sql to bypass the login

First we attempted using 1=1 is always true sql however it appears the input was sanitized in some way so this failed

Next we attempted ""="" is always true

So: 'or ''=' in both the username and password fields

This lets us login and claim the flag

flag: nactf{sQllllllll_1m5qpr8x}
