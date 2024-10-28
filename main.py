# Quinten Reed
# U3L1
# While vs Recursion

def while_substitute(num):
  num2 = num

  while num2 > 0:
    print(f"Recursing; num = {num2}")
    num2 -= 1
  
  print("\nBASE CASE REACHED\n")

  while num2 < 5:
    num2 += 1
    print(f"Returning; num = {num2}")

def main():
  while_substitute(5)

if __name__ == "__main__":
  main()