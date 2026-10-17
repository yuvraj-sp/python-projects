alphabets = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
print(''' ██████╗ █████╗ ███████╗██████╗ ███████╗██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     ███████║███████╗██████╔╝█████╗  ██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══██║╚════██║██╔═══╝ ██╔══╝  ██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████║██║     ███████╗██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                               
      ''')


# def encrypt(original_text,shift_amount):

#     cypher_text=""

#     for letter in original_text:
#         shifted_position=alphabets.index(letter)+shift_amount
#         shifted_position %= len(alphabets)
#         cypher_text += alphabets[shifted_position]

#     print(f"Here is the encoded result :{cypher_text}")


# def decrypt(original_text,shift_amount):
#     output_text=""

#     for letter in original_text:
#         shifted_position=alphabets.index(letter)-shift_amount
#         shifted_position %= len(alphabets)
#         output_text += alphabets[shifted_position]

#     print(f"Here is the encoded result :{output_text}")


# encrypt(original_text=text,shift_amount=shift)
# decrypt(original_text=text,shift_amount=shift)

def caesar(original_text,shift_number,encode_or_decode):
        cypher_text=""
    
    

        if encode_or_decode == "decode":
            shift_number*= -1
        for letter in original_text:
            if letter not in alphabets:
                cypher_text+=letter
            else:
                shifted_position=alphabets.index(letter) + shift_number
                shifted_position%=len(alphabets)
                cypher_text+=alphabets[shifted_position]

        print(f"Here is the {encode_or_decode}d result :{cypher_text}")

should_continue = True
while should_continue:
    direction=input("Type encode to encrypt,Type decode to decrypt: \n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    caesar(text,shift,direction)

    restart=input("yes to contine, no to stop \n").lower()
    if restart=="no":
        should_continue=False
        print("goodbye")