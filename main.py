import pyperclip as clipboard

alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
print(alphabet_list)
r_alpha = alphabet_list.copy()
r_alpha.reverse()
print(r_alpha)
special_character = list("!@#$%^&*(){}[];':|<>?,./-=_+")
r_specialChar = special_character.copy()
r_specialChar.reverse()
num_list = list('012345679')
r_num = num_list.copy()
r_num.reverse()
print(special_character)
print(r_specialChar)


def encrypt(string, key):
    encrypted_text_list = []
    output_string = ""
    input_string_list = string.split(" ")

    for a in input_string_list:
        encrypted_subtext = ''
        for b in a:
            if b.lower() in alphabet_list:
                x = alphabet_list.index(b.lower())
                new_index = x + (int(key)-1)
                if new_index < 25:
                    encrypted_subtext = encrypted_subtext + alphabet_list[new_index]
                elif new_index >= 25:
                    encrypted_subtext = encrypted_subtext + alphabet_list[(new_index-26)]
            elif b in special_character:
                x = special_character.index(b.lower())
                new_index = x + (int(key) - 1)
                if new_index < 27:
                    encrypted_subtext = encrypted_subtext + special_character[new_index]
                elif new_index >= 27:
                    encrypted_subtext = encrypted_subtext + special_character[(new_index - 28)]
            elif b in num_list:
                x = num_list.index(str(b))
                new_index = x + (int(key) - 1)
                if new_index < 9:
                    encrypted_subtext = encrypted_subtext + num_list[new_index]
                elif new_index >= 9:
                    encrypted_subtext = encrypted_subtext + num_list[(new_index - 10)]

        encrypted_text_list.append(encrypted_subtext)

    for encrypted_text in encrypted_text_list:
        # print(encrypted_text.upper(), end=" ")
        output_string = output_string + encrypted_text
        output_string = output_string + " "

    try:

        clipboard.copy(output_string.upper())
        print("Copied to Clipboard")
    except:
        print("Copying to Clipboard Failed")

    print(f"Encrypted Text :> {output_string.upper()}")


def decrypt(string, key):
    decrypted_text_list = []
    output_string = ""

    input_string_list = string.split(" ")

    for a in input_string_list:
        decrypted_subtext = ''
        for b in a:
            if b.lower() in r_alpha:
                x = r_alpha.index(b.lower())
                new_index = x + (int(key)-1)
                if new_index < 25:
                    decrypted_subtext = decrypted_subtext + r_alpha[new_index]
                elif new_index >= 25:
                    decrypted_subtext = decrypted_subtext + r_alpha[(new_index-26)]
            elif b in r_specialChar:
                x = r_specialChar.index(b.lower())
                new_index = x + (int(key) - 1)
                if new_index < 27:
                    decrypted_subtext = decrypted_subtext + r_specialChar[new_index]
                elif new_index >= 27:
                    decrypted_subtext = decrypted_subtext + r_specialChar[(new_index - 28)]
            elif b in r_num:
                x = r_num.index(str(b))
                new_index = x + (int(key) - 1)
                if new_index < 9:
                    decrypted_subtext = decrypted_subtext + r_num[new_index]
                elif new_index >= 9:
                    decrypted_subtext = decrypted_subtext + r_num[(new_index - 10)]
        decrypted_text_list.append(decrypted_subtext)

    for decrypted_text in decrypted_text_list:
        #print(decrypted_text.title(), end=" ")
        output_string = output_string + decrypted_text
        output_string = output_string + " "

    try:

        clipboard.copy(output_string.title())
        print("Copied to Clipboard")
    except:
        print("Copying to Clipboard Failed")

    print(f"Decrypted Text :> {output_string.title()}")


while True:
    choice = input("Do You Want to Encrypt(e) or Decrypt(d):>")
    if choice.lower() == "e" or choice.lower() == "encrypt":
        input_string = input("Enter the text you want to Encrypt :>")
        input_key = int(input("Enter your encryption Key 🔑(max:26):>"))
        encrypt(input_string, input_key)

    elif choice.lower() == "d" or choice.lower() == "decrypt":
        input_string = input("Enter the text you want to decrypt :>")
        input_key = int(input("Enter your decryption Key 🔑:>"))
        decrypt(input_string, input_key)

    else:
        print("Invalid Input!!")

    print("")
    again = input("Do you to use the program again(yes/no):")
    if again.lower() == "yes" or again.lower() == "y":
        pass
    else:
        print("Thanks for using this program")
        break