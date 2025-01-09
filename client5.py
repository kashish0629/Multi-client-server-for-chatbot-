client5.py
import socket 
import numpy as np 
import string 
import simple_colors   

key={'a': 'Q', 'b': 'W', 'c': 'E', 'd': 'R', 'e': 'T', 'f': 'Y', 'g': 'U', 'h': 'I', 'i': 'O', 'j': 'P', 'k': 'A', 'l': 'S', 'm': 'D', 'n': 'F', 'o': 
'G', 'p': 'H', 'q': 'J', 'r': 'K', 's': 'L', 't': 'Z', 'u': 'X', 'v': 'C', 'w': 'V', 'x': 'B', 'y': 'N', 'z': 'M',' ':' '} 
 
def extend_plaintext(plaintext, key): 
    extended_plaintext = (plaintext * (len(key) // len(plaintext) + 1))[:len(key)] 
    return extended_plaintext 
 
def monoalphabetic_encrypt(plaintext): 
    ciphertext = "" 
    for char in plaintext.lower(): 
        if char in key: 
            ciphertext += key[char] 
        else: 
            ciphertext += char 
    return ciphertext 

def railfence_encrypt(plaintext, key):
    rail = [['\n' for _ in range(len(plaintext))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0
    for char in plaintext:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1
    return ''.join(rail[i][j] for i in range(key) for j in range(len(plaintext)) if rail[i][j] != '\n')

def client(): 
    host = "127.0.0.1" 
    port = 65432 
    plaintext = input(simple_colors.yellow("Enter plaintext: ")) 

    # Define the Rail Fence cipher key (number of rails)
    rail_key = 3  # Set the number of rails for the rail fence cipher

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: 
        client_socket.connect((host, port)) 
        
        ciphertext = railfence_encrypt(plaintext, rail_key) 
        ciphertext += 'railfence'  # Add a marker if needed, otherwise remove this line
       
        client_socket.send(ciphertext.encode()) 
        print(simple_colors.yellow('\nEncrypted message sent to the server successfully!')) 

if __name__ == "__main__": 
    client()
