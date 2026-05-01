import random
word_list=['banana','camel','america']
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
for i in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
display=""
display_list=[]
Hang=0
for letters in chosen_word:
    display_list.append("_")
while not display == chosen_word:
    guess=input("Guess a letter from the word: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}.")
    if not guess in chosen_word:
        if Hang==5:
            print(fr'''
The word was "{chosen_word}"
You Hang!''')
            break
        else:
            Hang+=1
            print(f"You are left with {6-Hang} chances")
    disp=""
    for letter in chosen_word:
        if letter==guess:
            disp+=letter
        else:
            disp+="_"
    i=0
    for char in disp:
        if char==guess:
            display_list[i]=char
        i+=1
    display=""
    for ch in display_list:
        display+=ch
    print(display)
    if display==chosen_word:
        print("You guessed right")
