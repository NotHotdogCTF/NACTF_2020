This challenge gives us another webpage.

By the name and theme of the challenge we can assume it concerns cookies

When we attempt to log in we are told that we are not a cookie lover

By inspecting our cookies we can see that we do actually have a cookie stating that we are a cookie lover

However, this cookie has the path "index.php"

If we change the path to "auth.php" we can login and claim the flag

Unfortunately, the cookie is replaced when we click the login button.

Thus we have to add out own.

In the browser we type JavaScript:void(document.cookie("user=cookie_lover"))

We then go and change the path to /auth.php

We can now login and claim our flag

nactf{c00kie_m0nst3r_5bxr16o0z}
