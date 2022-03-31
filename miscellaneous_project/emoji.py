def emojis_converter(message):
    words = message.split(' ')
    emojis_library = {

    ":)" : '😁',
    ":(" : '😔',
    ";)" : '😉',
    
    }
    output = ''
    for word in words:
        output += emojis_library.get (word, word) + " "
    return output

        
message = input (">>")
print (emojis_converter(message)) 
