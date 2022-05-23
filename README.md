# Simple Wordle
Every day I wake up and spend between 5 and 20 minutes trying to solve the [Wordle puzzle](https://www.nytimes.com/games/wordle/index.html). So why not try to create my own?

I found a simple [tutorial](https://www.freecodecamp.org/news/building-a-wordle-game/) and started repeating step by step. It was fine for the first version, but there was still a lot to do - randomizing word choices, checking inputs to see if they are made up of 5-letter words and are unequal. And some other simple but important things. So I started to add some more features that were included in the original Wordle version.

First, I found another [Wordle clone](https://github.com/cwackerfuss/react-wordle) to search for a dictionary. This way I found a document with 5000 words with 5 letters. I saved it as dict.txt and created a function to randomize the words for each new game.

Then I added a function that checks if the word entered is 5 letters (no more or less) and if the word actually exists (if it is in the dictionary, it is ok). 

Oh, and I added the function that checks if this word has already been used, so the player does not lose too many tries.

Have fun playing!