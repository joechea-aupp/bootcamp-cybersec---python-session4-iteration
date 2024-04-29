user_input = int(input("Enter number of time you want to say hello: "))

for cycle in range(user_input):
    print(f"Hello! {cycle + 1} time!")



# with error handling
# try:
#     user_input = int(input("Enter number of time you want to say hello: "))
#     for cycle in range(user_input):
#         print(f"Hello! {cycle + 1} time!")
# except ValueError:
#     print("Please enter a valid number!")

