from cryptography.fernet import Fernet

key='8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='
f = Fernet(key)
print(key)

#message = 'gAAAAABc8Wf3rxaime-363wbhCaIe1FoZUdnFeIXX_Nh9qKSDkpBFPqK8L2HbkM8NCQAxY8yOWbjxzMC4b5uCaeEpqDYCRNIhnqTK8jfzFYfPdozf7NPvGzNBwuuvIxK5NZYJbxQwfK72BNrZCKpfp6frL8m8pdgYbLNFcy6jCJBXATR3gHBb0Y='
message = b'encrypting is just as useful'

cipher_text = f.encrypt(message)
print(cipher_text)

# decrypt_text = f.decrypt(message)
# print(decrypt_text)