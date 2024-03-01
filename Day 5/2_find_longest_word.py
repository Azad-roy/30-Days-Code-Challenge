# 2.Implement a function to find the longest word in a sentence.
       
def find(sentence):
    long = ""
    max_length = 0
    
    words = sentence.split()

    for word in words:
        if len(word) > max_length:
            long = word
            max_length = len(word)
    return long

sentence = "Hello coders, Let's do something special"
print("Longest word:", find(sentence))