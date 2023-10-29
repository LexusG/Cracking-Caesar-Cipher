 # Caesar's Cypher BruteForce Cracking Script 

decrtpt_message = input("Input Cypher Here: ").upper()
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# Loop every key 
for key in range(len(SYMBOLS))
converted = ""

    #loop through all message in decrtpt_message
    for symbol in decrtpt_message:
        if symbol in SYMBOLS:=
            symbolIndex = SYMBOLS.find(symbol)
            convertedIndex = symbolIndex - key

            #Handle the SYMBOLS Wraparound:
            if convertedIndex < 0:
                convertedIndex = convertedIndex + len(SYMBOLS)

            #Append the decrypted symbol:
            converted = converted + SYMBOLS[convertedIndex]
        
        else:
            #Append the symbol without encryption/decrypting 
            converted = converted + symbol 