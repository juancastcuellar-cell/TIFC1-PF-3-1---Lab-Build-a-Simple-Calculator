def main():
  first = float(input("Enter the first number: "))
  second = float(input("Enter the second number: "))

  result = first + second
  if result.is_integer():
    result = int(result)

  print(result)


if __name__ == "__main__":
  main()