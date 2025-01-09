import socket 
import numpy as np 
import string 
import simple_colors   
 
key={'a': 'Q', 'b': 'W', 'c': 'E', 'd': 'R', 'e': 'T', 'f': 'Y', 'g': 'U', 'h': 'I', 'i': 'O', 'j': 'P', 'k': 'A', 'l': 'S', 'm': 'D', 'n': 'F', 'o': 
'G', 'p': 'H', 'q': 'J', 'r': 'K', 's': 'L', 't': 'Z', 'u': 'X', 'v': 'C', 'w': 'V', 'x': 'B', 'y': 'N', 'z': 'M',' ':' '} 
 
 
def monoalphabetic_encrypt(plaintext): 

 
   ciphertext = "" 
   for char in plaintext.lower(): 
       if char in key: 
           ciphertext += key[char] 
       else: 
           ciphertext += char 
   return ciphertext 
 
def client(): 
 
  host = "127.0.0.1" 
  port = 65432 
  plaintext = input(simple_colors.yellow("Enter plaintext: ")) 
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: 
    client_socket.connect((host, port)) 
     
    ciphertext = monoalphabetic_encrypt(plaintext) 
    print ("This is the encypted text",ciphertext) 
    ciphertext+='monoalphabetic' 
   
    client_socket.send(ciphertext.encode()) 
 
    #print(f"Sent: {ciphertext}") 
 
    print(simple_colors.yellow('\nEncrypted message sent to the server successfully!')) 
 
if __name__ == "__main__": 
  client()