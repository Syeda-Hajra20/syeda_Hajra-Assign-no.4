'''Assigment no.04
Q:- Write a Python program that reverses the order of words in a given sentence.
 
For sentence = "Python is fun":
output will be "fun is Python" '''
  

sentence="Python is fun"

sentence=sentence.split()[::-1]

print(" ".join(sentence))