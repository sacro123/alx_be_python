hours = 2

seconds = hours * 3600

assert seconds == 7200, f"Calculation error: {hours} hours should be 7200 seconds, but got {seconds}"

# Print the result in the specified format
print(f"{hours} hour(s) is {seconds} seconds.")
