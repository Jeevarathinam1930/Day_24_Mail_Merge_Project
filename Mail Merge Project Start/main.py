#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
completed_letter=""
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as letter:
    birthday_invite=letter.readlines()
    print(birthday_invite)
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    Names=names.readlines()

for i in birthday_invite:
    completed_letter+=i
for name in Names:
    name_with_letter=completed_letter.replace("[name]",name)
    print(name_with_letter)
    final_name=name.strip()
    output_path=f"../Mail Merge Project Start/Output/ReadyToSend/{final_name}.txt"
    with open(output_path,mode="a") as files:
        final_copy=files.write(name_with_letter)






