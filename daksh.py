s=list("!@#$%^&*(){}[];':|<>?,./-=_+")## total numbers of elements in it is 28.
n=list('0123456789')#List of integrals.
a=list(('abcdefghijklmnopqrstuvwxyz'))##list of alphabets in lower case.
A=list(('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))##list of all alpabets in uppercase.
b=[]## here the input by user gets stored.
h=[]## here the message after encryption or decryption gets stored.
print('Welcome to our program. \n Our program is there to help you encode your Secret Messages(regardless of how much '
      'naughty and confidential they are) according to keys given by you. \n **Warning** -- Be sure to remember the '
      'key for decoding your message.')


def keycheck(x):## Takes the value of key.
    if x.lower()=='e' or x.lower()=='encrypt':
        d=int(input('Enter any key (0 to 25).\t Be sure to remember the key for decrypting the message. :)'))
    else:
        d=int(input('Enter the key to decrypt the message.(0 to 25)'))
    if d>25 or d<1:
        print('oh ho you have entered a wrong key value .Enter the value between 1 and 25.')
        keycheck(x)
    else:return(d)
def  inputmessage(x): ##Takes the input message from the user and saves it in listb.
    global b
    if x.lower()=='e' or x.lower()=='encrypt':
        e=input('Please enter the message you want to encrypt.')
    elif x.lower()=='d' or x.lower()=='decrypt':
        e=input('Please enter the message to decrypt.')
    b=b+list(e)
def encrypt():##Encrypts the message from the inputmessage() according to logic .
    inputmessage(x)
    f=keycheck(x)
    j='a'
    g=0
    def output1(list,element,length):
        g=list.index(element)+f
        if g>(length-1):
            g=g-(length)
            h.append(list[g])
        else:h.append(list[g])
    for i in b:
        if i in n:
            output1(n,i,len(n))
        elif i in s:
            output1(s,i,len(s))
        elif i==' ':
            h.append(' ')
        elif i in A  :
            output1(A,i,len(A))
        else:
            output1(a,i,len(a))
    for i in h :
       j=j+i
    j=j[1:len(j)]
    return(j)
def decrypt(): ##Decrypts the message from the inputmessage() according to the logic
    inputmessage(x)
    f=keycheck(x)
    j='a'
    def output2(list,i,f):
        g=list.index(i)-f
        if g<0:
            g=list.index(i)-f
            h.append(list[g])
        else:h.append(list[g])
    for i in b:
        if i==' ':
            h.append(' ')
        elif i in A:
            output2(A,i,f)
        elif i in n:
            output2(n,i,f)
        elif i in s:
            output2(s,i,f)
        else:
            output2(a,i,f)
    for i in h:
        j=j+i
    j=j[1:len(j)]
    return(j)
def check():
    global x
    if x.lower()=='e' or x.lower()=='encrypt':
        print(encrypt())
    elif x.lower()=='d' or x.lower()=='decrypt':
        print(decrypt())
    else:
        print('abe ullu check the input you have entered .. \n aaj-kal k anpad bache . \n Beta tumse na hopaye-ga. Just enter  e or encrypt / d or decrypt.')
        x=input('What do you want to do (e)ncrypt or (d)ecrypt your message.\t')
        check()
while True:
    x=input('What do you want to do (e)ncrypt or (d)ecrypt your message.\t')
    check()
    z=input('Do you want to encrypt or decrypt any other message ? (y/n)\t')
    if z.lower()=='n' or z.lower()=='no':
        break
    else:
        b=[]
        h=[]
        continue
exit()