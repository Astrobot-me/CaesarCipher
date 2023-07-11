# string = "Hello Mate"
# print(string.split(' '))
alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
print(alphabet_list)
r_alpha = alphabet_list.copy()
r_alpha.reverse()

print(r_alpha)
string ="Hello! , How are you Mr. Daksh?"
input_string_list = string.split(" ")
print(input_string_list)
special_character = list("!@#$%^&*(){}[];':|<>?,./-=_+")
print(len(special_character))
print("?><".lower())
def decrypt(string, key):
    decrypted_text_list = []

    input_string_list = string.split(" ")

    for a in input_string_list:
        decrypted_subtext = ''
        for b in a:
            x = r_alpha.index(b.lower())
            new_index = x + (int(key)-1)
            if x <= 22:
                decrypted_subtext = decrypted_subtext + r_alpha[new_index]
            elif x >= 23:
                decrypted_subtext = decrypted_subtext + r_alpha[(new_index-23)]

        decrypted_text_list.append(decrypted_subtext)

    for decrypted_text in decrypted_text_list:
        print(decrypted_text.title(), end=" ")

st = "KHOOR GDNVK FUDFEERQHV LGN KRZ WR VSHOO WKLV"

#decrypt(st, 4)