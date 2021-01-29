# Zero shot positive climate news classifier

[Huggingface](http://huggingface.co) is the world's best natural language text processing technology (has a free API now)[https://api-inference.huggingface.co/docs/python/html/index.html] and one of them is a text categorisation engine that requires no training! This is called "zero shot learning" and it's pretty magical.

It works because the repository it's using is a gargantuan one from Facebook called BART. [Learn more about Facebook's BART](https://huggingface.co/facebook/bart-large)

Check out the code: it's really really basic. I took a few news headlines and made up some labels "positive", "negative" and "neutral" and asked Huggingface using the BART model to predict which headline is positive, negative or neutral. 

It's astonishingly good for positive and negative, but fails at all the neutral ones. Try it out with different headlines and categories. 


