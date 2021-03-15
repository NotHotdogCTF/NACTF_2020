We are again given another webpage to find a flag hidden in

By inspecting the code we can see there is an image that is being attempted to load that is not appearing

If we try to go to the address of the image we get a 404 error

Thus, we know that the image address is not correct.

If we then correct the subdomain of the address challenges.nactf.com vs hidden.challenges.nactf.com

The image then appears and we can take the flag text from the image

nactf{h1dd3n_1mag3s}
