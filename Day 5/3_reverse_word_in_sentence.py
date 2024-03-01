# 3.Write a program to reverse the order of words in a sentence.

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    
    reversed_sentence=" ".join(reversed_words)
    return reversed_sentence

sentence = "The quick brown fox jumps over the lazy dog"
reversed_sentence = reverse_sentence(sentence)
print("Original sentence:", sentence)
print("Reversed sentence:", reversed_sentence)