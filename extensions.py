#MKHABELE MMM
#28/06/2023
def main():
    name=input("File name: ")

    def extension_checker(k):
        k=k.lower()
        input_list=(k.split("."))
        if len(input_list)==1 or input_list[-1]=='bin':
            print("application/octet-stream")
        elif input_list[-1]=="jpeg" or  input_list[-1]=="gif" or input_list[-1]=='png' :
            print('image/{}'.format(input_list[-1]))
        elif input_list[-1]=='jpeg':
            print("image/jpeg")
        elif input_list[-1]=="pdf" or input_list[-1]=="zip":
            print("application/{}".format(input_list[-1]))
        elif input_list[-1]=="text":
            print("text/plain")
        else:
            print(input_list[-1])
            
    extension_checker(name)
main()