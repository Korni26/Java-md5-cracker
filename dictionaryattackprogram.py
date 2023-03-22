import hashlib
from unittest import result

md5_hash_to_crack = 'dc647eb65e6711e155375218212b3964'

wordlist = open('norwegian.txt').readlines()


for word in wordlist:
    word = word.strip()
    bigWord = word.capitalize()
    bigNumberWord = word.capitalize() + "123"
    result = hashlib.md5(word.encode()).hexdigest()
    bigResult = hashlib.md5(bigWord.encode()).hexdigest()
    bigNumberResult = hashlib.md5(bigNumberWord.encode()).hexdigest()
    

    if result == md5_hash_to_crack:
        print('Found password: ' + word)
    if bigResult == md5_hash_to_crack:
        print('Found password: ' + bigWord)
    if bigNumberResult == md5_hash_to_crack:
        print('Found password: ' + bigNumberWord)

print('Searched through ' + str(len(wordlist)) + ' words') 