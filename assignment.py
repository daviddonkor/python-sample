#Importing the relavant libraries
from Crypto.Cipher import AES
from Crypto.Random.random import Random
import os

#We are going to create a class to will extend the Experimental API
#The use has to call the API with the right parameters and the images will be generated on the system. 

class ExtendedExperimentalAPI:

    def __init__(self,key,mode):
        self.key=key
        self.mode=mode
        self.modetext=str(mode)
        self.useIV=True
        if(self.mode==AES.MODE_ECB):
            self.useIV=False
        #key=b'770A8A65DA156D24EE2A093277530142'

    def pad(self,s):
        return s+b"\0"*(AES.block_size - len(s) % AES.block_size)

    def encrypt(self,message):
        
        message=self.pad(message)
        #Generating the IV
        iv=Random.new().read(AES.block_size)
        #Checking if IV is needed for decryption or not
        if(self.useIV):
            cipher=AES.new(self.key, self.mode,iv)
        else:
            cipher=AES.new(self.key, self.mode)
        return iv+cipher.encrypt(message)

    def encrypt_file(self,filename):
        #Checking if file exits
        if(os.path.isfile(filename)==False):
            raise Exception("File not found!")
        #Breaking the file path to have the extension
        ext=os.path.splitext(filename)
        with open(filename, 'rb') as f:
            data = f.read()
        f.close()
        enc=self.encrypt(data)
        with open(ext[0]+'_enc_'+self.modetext+ext[1],'wb') as w:
            w.write(enc)
        w.close()
    
    def decrypt(self,message):
        iv=message[:AES.block_size]
        #Checking if IV is needed for decryption or not
        if(self.useIV):
            cipher=AES.new(self.key, self.mode,iv)
        else:
            cipher=AES.new(self.key, self.mode)
        msg=cipher.decrypt(message[AES.block_size:])
        #remove the padding added to the message
        return msg.rstrip(b"\0")

    #funtion to decrypt file
    def decrypt_file(self,filename):
        if(os.path.isfile(filename)==False):
            raise Exception("File not found!")
        ext=os.path.splitext(filename)
        with open(filename, 'rb') as f:
            data = f.read()
        f.close()
        dec=self.decrypt(data)
        with open(ext[0]+'_dec_'+self.modetext+ext[1],'wb') as w:
            w.write(dec)
        w.close()
    

#Creating the three Encrypted file Class
enc_cbc_2=ExtendedExperimentalAPI(b'770A8A65DA156D24EE2A093277530142',AES.MODE_CBC)
enc_ecb_1=ExtendedExperimentalAPI(b'770A8A65DA156D24EE2A093277530142',AES.MODE_ECB)
enc_cfb_3=ExtendedExperimentalAPI(b'770A8A65DA156D24EE2A093277530142',AES.MODE_CFB)
#Encrypting file with the diverse modes
enc_cbc_2.encrypt_file("linux-icon.png")
enc_ecb_1.encrypt_file("linux-icon.png")
enc_cfb_3.encrypt_file("linux-icon.png")

# enc_cbc_2.decrypt_file("linux-icon_enc_2.png")
# enc_ecb_1.decrypt_file("linux-icon_enc_1.png")
# enc_cfb_3.decrypt_file("linux-icon_enc_3.png")
