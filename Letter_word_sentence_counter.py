/* Letter Word Sentence Counter
You can count the letters, words, and sentences in a given text by using the following methods:
For letters:
  
Split the text into individual characters.
Use a loop to iterate through each character and check if it is a letter. If it is a letter, increment a counter variable.

For words:
Split the text into words using spaces.
Use a loop to iterate through each word.
Increment a counter variable for each word.

For sentences:
Split the text into sentences using punctuation marks such as '.', '!' and '?'.
Use a loop to iterate through each sentence.
Increment a counter variable for each sentence.
You can also use regular expressions to count letters, words, and sentences.

Here is a Python code snippet to count the number of letters, words, and sentences in a given text:
*/
def count_text(text):
letters = 0
words = 0
sentences = 0

for char in text:
if char.isalpha():
letters += 1
if char in ['.', '!', '?']:
sentences += 1
words = len(text.split())

return (letters, words, sentences)

text = "This is a sample text. It has multiple sentences!"
print("Letters: ", count_text(text)[0])
print("Words: ", count_text(text)[1])
print("Sentences: ", count_text(text)[2])

This code uses the isalpha() method to check if a character is a letter and the split() method to split the text into words. The function returns a tuple with the count of letters, words, and sentences.
