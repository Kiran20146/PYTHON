def main():
    file_format = input("please enter the file format ")
    check_which_format(file_format)


def check_which_format(filename):
    if ".gif" in filename:
        print("images // .gif")
    elif ".jpg" in filename:
        print("images // .jpg")
    elif ".jpeg" in filename:
        print("images // .jpeg")
    elif ".png" in filename:
        print("images // .png")
    elif ".pdf" in filename:
        print("images // .pdf")
    elif ".txt" in filename:
        print("images // .txt") 
    elif ".zip" in filename:
        print("images // .zip")  
    else:
        print("application/octet-stream")

main()                                    

    

