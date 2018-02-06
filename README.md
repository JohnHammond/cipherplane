# cipherplane

> John Hammond | February 4th, 2018

------------------------

This is a project based off of my reaction to the "[DES]" [challenge](https://amritabi0s.wordpress.com/2018/02/03/sharif-ctf-2018-crypto-writeups/) during SharifCTF 2018. 

The [DES] challenge offered about a thousand known plaintext/ciphertext pairs, and asked you to determine the key to submit as the flag. The real difficulty in this challenge was just __sorting through the pairs to find duplicates or similarities in the pairs.__ Had we found one single similarity in a plaintext or ciphertext, we would have been able to find a lead on the challenge and probably solve it.

But, we didn't have anything that would smartly detect duplicates or similarities in the data. I tossed the challenge aside and never completed it during the competition, but after [reading the writeups](https://ctftime.org/task/5215) I realized we seriously needed that capability.

So this is just some [Python] code to do that. It doesn't have support for command-line arguments or anything fancy... I expect dirty usage, just slapping in your own data for the script. _It will still get you the information you need._

The project is nicknamed *`cipherplane`*, as a gag off of "ciphertext" and "plaintext."

[DES]: https://en.wikipedia.org/wiki/Data_Encryption_Standard
[Python]: https://www.python.org/