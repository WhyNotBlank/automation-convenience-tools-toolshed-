print("Hello from rex editor.")
print("put the file u want raw bytes of in the same folder as the script/exe")
print("after you have done that tell me the name of the file(extension(.png/.mp3 etc.) included).")
print("=" * 30)

file = input("say the name of the file : ")

with open(f"{file}", "rb") as fu:
    
    raw_bytes = fu.read()
    binary_representation = '' .join(format(byte, '08b') for byte in raw_bytes)

with open(f"{file}.txt", "w") as ck:

   ck.write(binary_representation)

print("there should be a .txt file in the same folder as the script open it and it should have the")
print("raw bytes of the file.")