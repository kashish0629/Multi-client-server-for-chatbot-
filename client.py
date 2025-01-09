import socket 
import simple_colors   
 
def polyalphabetic_encrypt(plaintext, key): 
    ciphertext = "" 
    for i, p in enumerate(plaintext): 
        offset = ord(key[i % len(key)]) - ord('a') 
        ciphertext += chr((ord(p) - ord('a') + offset) % 26 + ord('a')) 
    return ciphertext 
 
def client(): 
 
    host = "127.0.0.1"  
    port = 65432 
       
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: 
        client_socket.connect((host, port)) 
         
        plaintext = input(simple_colors.red("Enter plaintext: ")) 
         
        plaintext = plaintext.lower()  

 
        plaintext = plaintext.replace(" ", "") 
        plaintext = "".join(c for c in plaintext if c.isalnum()) 
         
        key = "key" 
        ciphertext = polyalphabetic_encrypt(plaintext, key)
        print ("This is the encypted text",ciphertext) 
 
        ciphertext+='polyalphabetic' 
        client_socket.send(ciphertext.encode()) 
        #print(f"Sent: {ciphertext}") 
 
        print(simple_colors.red('\nEncrypted message sent to the server successfully!')) 
 
if __name__ == "__main__": 
    client() 