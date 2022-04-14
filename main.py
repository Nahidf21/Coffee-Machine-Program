def main():
    count="yes"
    new_list=[]
    while count=="yes":
        print("What would you like? ")
        input_data=input("Type the name what you want: ")
        new_list.append(input_data)
        print(new_list)
        loop_end=input("Are you want to continue the process yes or no")
        count=loop_end

    

main()