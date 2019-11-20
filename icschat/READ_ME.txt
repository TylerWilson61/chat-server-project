#IMPLEMENTATIONS


#LOGIN SYSTEM
'''
For the login system I created a dictionary that holds all
the usernames and passwords together that have been logged in before.
You start the program by running the login window, and from there may enter
the registration window if you do not have an account, or you may
directly enter the chat window if you have an account. When there is an error
from registering an account or logging into the system, and error msg is
display and the client is prompted to try again.
'''

#GUI
'''
So technically we made three GUI windows: the registration window,the login
window, and the client window. I struggled to make the client window
optimal, however it is fully functional. I used threading to continuously check for messages from other peers while in the client window. The encryption is functional, however it does not look pretty in display. In actuality, the encrypted message doesn't need to be displayed, we just wanted it to be known to the user that there is encryption. This feature can easily be taken out or made "prettier" in the future.
'''




#ENCRYPTION
'''
For the encryption we used the RSA encryption method. Firstly I created a file that holds all functions related to creating the keys and encrypting the files. Secondly I imported these files into the client state machine and created new actions to send the public keys out to the other user when chatting. The public key is used to encrypt the messages sent to a user then the user uses their own private key to decrypt the text. Changes also had to be made to the server to accommodate this. The search functionality wasn't working after encryption because the server couldn't read the encrypted messages so we had to move the search functionality to the clients side. This was done by storing individual user history on their own computer, and conducting the search through the client state machine. 
'''


#TO RUN

'''
1) download the repo
2) open up terminal and run the chat_server.py file
3) open up another terminal window and run the login_window.py file
4) To play around with more users, add a third window to add more peers
