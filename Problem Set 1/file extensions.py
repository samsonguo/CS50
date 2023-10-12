#extensions image': ['gif', 'jpg', 'jpeg', 'png'],
#extensions application': ['pdf', 'zip'],

file = input("Name of the file: ").replace("jpg","jpeg").lower().strip().split(".")
image = ["gif", "png", "jpeg","jpg"]
application = ["zip", "pdf"]

if file[-1] == "txt":
    print("text/plain")
elif file[-1] in application:
    print(f'application/{file[-1]}')
elif file[-1] in image:
    print(f'image/{file[-1]}')
else:
    print("application/octet-stream")