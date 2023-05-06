#convert the first two letter to upper case and double every other words "The red fox jumped over the lazy dog." using python
comment = "The red fox jumped over the lazy dog."
#STEP 1:
new = ''
comment_arr = comment.split(' ') #['the'. 'red' ... 'dog']

for word in comment_arr:
   # first_two_letters = word[:2].upper()
   # rest_letters = word[2:]
   # doubled_letter = ''
   # for letter in rest_letters:
   #     doubled_letter += letter * 2
   # new += first_two_letters + doubled_letter + ''

    word = word[:2].upper() + '' .join([letter * 2 for letter in word[2:]])
    new += word + ' '
     
print(new)




