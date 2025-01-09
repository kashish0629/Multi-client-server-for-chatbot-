import socket 
import numpy as np 
import string 
import simple_colors 
 
#poly 
def polyalphabetic_decrypt(ciphertext, key): 
    plaintext = "" 
    for i, c in enumerate(ciphertext): 
        offset = ord(key[i % len(key)]) - ord('a') 
        plaintext += chr((ord(c) - ord('a') - offset) % 26 + ord('a')) 
    return plaintext 
 
#caeser 
def toLowerCase(plain): 
 return plain.lower() 
 
def removeSpaces(plain): 
 return ''.join(plain.split()) 
 
def generateKeyTable(key): 
 keyT = [['' for i in range(5)] for j in range(5)] 
 dicty = {chr(i + 97): 0 for i in range(26)} 
 
 for i in range(len(key)): 
  if key[i] != 'j': 
   dicty[key[i]] = 2 
 dicty['j'] = 1 
 
 i, j, k = 0, 0, 0 
 while k < len(key): 

 
  if dicty[key[k]] == 2: 
   dicty[key[k]] -= 1 
   keyT[i][j] = key[k] 
   j += 1 
   if j == 5: 
    i += 1 
    j = 0 
  k += 1 
 
 for k in dicty.keys(): 
  if dicty[k] == 0: 
   keyT[i][j] = k 
   j += 1 
   if j == 5: 
    i += 1 
    j = 0 
 return keyT 
 
 
def search(keyT, a, b): 
 arr = [0, 0, 0, 0] 
 
 if a == 'j': 
  a = 'i' 
 elif b == 'j': 
  b = 'i' 
 
 for i in range(5): 
  for j in range(5): 
   if keyT[i][j] == a: 
    arr[0], arr[1] = i, j 
   elif keyT[i][j] == b: 
    arr[2], arr[3] = i, j 
 return arr 

 
 
 
def mod5(a): 
 if a < 0: 
  a += 5 
 return a % 5 
 
 
def decrypt(str, keyT): 
 ps = len(str) 
 i = 0 
 while i < ps: 
  a = search(keyT, str[i], str[i+1]) 
  if a[0] == a[2]: 
   str = str[:i] + keyT[a[0]][mod5(a[1]-1)] + keyT[a[0]][mod5(a[3]-1)] + str[i+2:] 
  elif a[1] == a[3]: 
   str = str[:i] + keyT[mod5(a[0]-1)][a[1]] + keyT[mod5(a[2]-1)][a[1]] + str[i+2:] 
  else: 
   str = str[:i] + keyT[a[0]][a[3]] + keyT[a[2]][a[1]] + str[i+2:] 
  i += 2 
 
 return str 
 
def playfair_decrypt(str, key): 
 ks = len(key) 
 key = removeSpaces(toLowerCase(key)) 
 str = removeSpaces(toLowerCase(str)) 
 keyT = generateKeyTable(key) 
 return decrypt(str, keyT) 
 
#monoalphabetic 
key = {'a': 'Q', 'b': 'W', 'c': 'E', 'd': 'R', 'e': 'T', 'f': 'Y', 'g': 'U', 'h': 'I', 'i': 'O', 'j': 'P', 'k': 'A', 'l': 'S', 'm': 'D', 'n': 'F', 'o': 
'G', 'p': 'H', 'q': 'J', 'r': 'K', 's': 'L', 't': 'Z', 'u': 'X', 'v': 'C', 'w': 'V', 'x': 'B', 'y': 'N', 'z': 'M',' ':' '} 
 

 
reversed_key = {v: k for k, v in key.items()} 
 
def monoalphabetic_decrypt(ciphertext): 
  plaintext = "" 
  for char in ciphertext.upper(): 
      if char in reversed_key: 
          plaintext += reversed_key[char] 
      else: 
          plaintext += char 
  return plaintext 
 
#rail 
def railfence_decrypt(cipher,key): 
 
    rail = [['\n' for i in range(len(cipher))] 
                for j in range(key)] 
      
    dir_down = None 
    row, col = 0, 0 
      
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True 
        if row == key - 1: 
            dir_down = False 
          
        rail[row][col] = '*' 
        col += 1 
          
        if dir_down: 
            row += 1 
        else: 
            row -= 1 
    index = 0 

 
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and 
            (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1 
 
    result = [] 
    row, col = 0, 0 
    for i in range(len(cipher)): 
          
        if row == 0: 
            dir_down = True 
        if row == key-1: 
            dir_down = False 
              
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1 
 
        if dir_down: 
            row += 1 
        else: 
            row -= 1 
    return("".join(result)) 
 
def handle_client(conn, addr):    
     
    while True: 
        data=conn.recv(1024).decode() 
        if not data:  
            break 
             
        if "polyalphabetic" in data: 
 
 
            print(simple_colors.blue(f"Connected to {addr}, using polyalphabetic algo")) 
            data = data.replace("polyalphabetic", "") 
            print(simple_colors.blue('\nMessage received successfully from client 1')) 
            key = "key"  
            plaintext = polyalphabetic_decrypt(data, key) 
             
        elif "playfair" in data: 
            print(simple_colors.blue(f"Connected to {addr}, using playfair algo")) 
            data = data.replace("playfair", "") 
            print(simple_colors.blue('\nMessage received successfully from client 2')) 
            key='Monarchy' 
            plaintext = playfair_decrypt(data, key) 
             
        elif "monoalphabetic" in data: 
            print(simple_colors.blue(f"Connected to {addr}, using monoalphabetic algo")) 
            data = data.replace("monoalphabetic", "") 
            print(simple_colors.blue('\nMessage received successfully from client 3')) 
            plaintext = monoalphabetic_decrypt(data) 
             
        elif "railfence" in data: 
            print(simple_colors.blue(f"Connected to {addr}, using railfence algo")) 
            data = data.replace("railfence", "") 
            print(simple_colors.blue('\nMessage received successfully from client 4')) 
            key = 3 
            plaintext = railfence_decrypt(data, key) 
             
        print(simple_colors.blue(f"Received from {addr}: {plaintext}\n")) 
         
    conn.close() 
    print(simple_colors.blue(f"{addr} disconnected")) 
 
def start_server(): 
    host = "127.0.0.1" 
    port = 65432   

 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind((host, port)) 
     
    server_socket.listen(4) 
    print(simple_colors.blue(f"Server listening on {host}:{port}")) 
         
    for i in range(4): 
        conn, addr = server_socket.accept() 
        handle_client(conn, addr) 
         
if __name__ == "__main__": 
    start_server()