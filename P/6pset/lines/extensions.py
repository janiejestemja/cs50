# File Extensions

def main():
	# defining valid extensions 
	accepted_extensions = {
	"gif":"image/gif",
	"jpg":"image/jpeg",
	"jpeg": "image/jpeg",
	"png": "image/png",
	"pdf": "application/pdf",
	"txt": "text/plain",
	"zip": "application/zip",
	}
	# getting user input and extracting extension
	user_input = input("Filename: ").lower()
	filename, extension = user_input.rsplit(".", maxsplit=1)

	if extension in accepted_extensions:
		print(accepted_extensions[extension])

	else:
		print("application/octet-stream")

if __name__ == "__main__":
	main()