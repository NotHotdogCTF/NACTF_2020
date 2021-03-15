In this challenge we have a message sent 101 times.

We can get every instance of this message by dividing the length of the message by 101 and splitting at that point to get 101 individual messages.

We know that this is a noisy channel so we can assume some corruption between the messages.

We made a simple consensus algorithm (contained in exploit.py) that compares each bit of the message against all other copies and takes the version that most agree on. 

We can then take the binary and convert it to ascii text.

nactf{n01sy_n013j_|\|()|$'/}
