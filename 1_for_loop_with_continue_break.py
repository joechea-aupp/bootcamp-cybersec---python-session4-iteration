# Example using both break and continue in a for loop
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print("Checking", i, "...")
    if i == 7:
        print("Found 7! Stopping the loop.")
        break  # Stop the loop when 7 is found
    print(i, "is not 7.")



