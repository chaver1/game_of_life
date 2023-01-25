#import main

def board_generator_test(width, height):
    #generate various boards given a few different w x h combos
    pass

if __name__ == "__main__":
    pass

hashmap = {}
key = "asdb akkasd igmmask laskeuivgyt"
j=0
for i in range(len(key)+1): 
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            print(j)

            if key[i] == ' ':
                continue
            
            else: 
                hashmap[key[i]] = alphabet[j]
                print(hashmap)
                j += 1
