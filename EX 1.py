# EX1 FLOW CONTROL,FUNTION AND STRING MANIPULATION
# II-BCA(24-27) SATHIYAPRIYA G

def reverse_string(text):
  return text[::-1]
def count_words(text):
     words=text.split()
     return len(words)
print("flow control,functions and manipulation")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
input_text=input("Enter a sentence:")
if input_text.startswith("Hello"):
   print("Greetings:Hello!")
elif input_text.startswith("Goodbye"):
   print("printing:Goodbye!")
else:
   print("custom message:",input_text)
reverse_string=reverse_string(input_text)
print("reverse string:",reverse_string)
word_count=count_words(input_text)
print("word count:",word_count)
