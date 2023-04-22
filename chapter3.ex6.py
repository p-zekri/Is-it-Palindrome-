word=input()
word=word.lower()
# print(len(word))
w=""
i=len(word) #because for loop didn't start from zero
for i in range(len(word),0,-1):
    i=i-1
#     print("i= ", i)
    w=w+word[i]
#     print(w)
if w==word:
    print("palindrome")

else:
    print("not palindrome")
# print(w)
