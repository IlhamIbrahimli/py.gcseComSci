lstToSearch = ["Alice", "Bob", "Carl", "Debbie", "Edward", "Florence"]
search = input("Enter item to search for:")
found = False
for i in range(len(lstToSearch)):
    if lstToSearch[i] == search:
        found=True
    
if found == True:
    print(f"{search} is in list")
else:
    print(f"{search} is not in list")