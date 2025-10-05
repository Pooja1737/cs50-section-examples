filename = input("File name: ")
file_lower = filename.strip().lower()
if file_lower.endswith(".gif"):
    print("image/gif")
elif file_lower.endswith(".jpg") or file_lower.endswith(".jpeg"):
    print("image/jpeg")
elif file_lower.endswith(".png"):
    print("image/png")
elif file_lower.endswith(".pdf"):
    print("application/pdf")
elif file_lower.endswith(".txt"):
    print("text/plain")
elif file_lower.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
