file_name = input("Welcome, tell me the name of the converted .txt file you want to restore To origenal form : ")

bit_string = open(f"{file_name}", "r", encoding="utf-8").read().strip()
bytes_data = bytes(int(bit_string[i:i+8], 2) for i in range(0, len(bit_string), 8))

next_name = input("Name the file(use the extension that the origenal file had) : ")

open(f"{next_name}", "wb").write(bytes_data)

print("Done")