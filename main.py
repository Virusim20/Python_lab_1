import math
import os  #library for clear console


def cls():  #function for clear console
  os.system(['clear', 'cls'][os.name == 'nt'])


def task_1():
  cls()
  check = True
  while check: # Змінна check вже є логічною, тому не потрібно додатково використовувати логічні оператори
    try:
      print("Do you want exit? Enter > 0\n\n")
      print("1 > Дано двозначне число. Знайти суму і твір його цифр.\n")
      num = int(input("Enter double digit number: "))
      if num < 0:
        print("\nis not a need number")
        input("Press Enter to continue...")
        cls()  #clear console
        continue
      elif num > 99:
        print("\nis not a duble digit number")
        input("Press Enter to continue...")
        cls()
        continue  #loop starts from the beginning
      elif num == 0:
        check = False  #Exit the loop
      else:
        num_1 = num // 10
        num_2 = num % 10
        sum = num_1 + num_2
        mul = num_1 * num_2
        print("Number 1 = ", num_1, "\nNumber 2 = ", num_2, "\nSum = ", sum, "\nMul = ", mul)
        input("Press Enter to continue...")
        cls()  #clear console
    except ValueError:
      print("\nis not a need number")
      input("Press Enter to continue...")
      cls()  #clear console

  input("Press Enter to continue...")
  cls()  #clear console


def task_2():
  cls()
  check = True
  x = 0
  while check:
    try:
      print("2 > Математичний вираз\n\n")
      x = float(input("Enter ""x>0 : ")) 
      if x <= 0:
        print("\nx", "is not a need number")
        input("Press Enter to continue...")
        cls()  #clear console
        continue  #loop starts from the beginning
      check = False  #Exit the loop
    except ValueError:
      print("\nx", "is not a need number")
      input("Press Enter to continue...")
      cls()  #clear console

  y = (2 * math.pi * (math.sin(math.pi + 2 * x)**2) *
       math.pow(abs(3 * x - 5 * pow(math.e, 2 * x)), 1 / 3)) / pow(
           3, x) * math.log2(math.sin(math.radians(17)))
  print("y =", y)
  input("Press Enter to continue...")
  cls()  #clear console

  
def task_3():
  cls()
  check = True
  x = 0
  y = 0
  while check:
    try:
      print("3 > Дано координати поля шахівниці x, y (цілі числа, що лежать в діапазоні 1-8). З огляду на, що ліве нижн поле дошки (1, 1)  чорним, перевірити істинність висловлювання: «Дане поле  білим».\n\n")

      print("Do you want exit? Enter > x = 0, y = 0\n\n")
      x = int(input("Enter "
                    "x > 0 AND x < 8: "))
      y = int(input("Enter "
                    "y > 0 AND y < 8: "))
      if x < 0 or y < 0 or x > 8 or y > 8:
        print("\nis not a need number")
        input("Press Enter to continue...")
        cls()  #clear console
        continue  #loop starts from the beginning
      elif x == 0 and y == 0:
        check = False  #Exit the loop
      elif x % 2 == 0 and y % 2 != 0:
        print("\nThis area is white")
        input("Press Enter to continue...")
        cls()  #clear console
      elif x % 2 != 0 and y % 2 == 0:
        print("\nThis area is white")
        input("Press Enter to continue...")
        cls()  #clear console
      elif x % 2 == 0 and y % 2 == 0:
        print("\nThis area is black")
        input("Press Enter to continue...")
        cls()  #clear console
      elif x % 2 != 0 and y % 2 != 0:
        print("\nThis area is black")
        input("Press Enter to continue...")
        cls()  #clear console
    except ValueError:
      print("\nis not a need number")
      input("Press Enter to continue...")
      cls()  #clear console
  input("Press Enter to continue...")
  cls()  #clear console


if __name__ == "__main__":
  #Choice var
  cls()
  choice = 0
  check = True
  
  while check:
    try:
      print("Do you want exit? Enter > 0\n\n")
      print("1 > Дано двозначне число. Знайти суму і твір його цифр.")
      print("\n2 > Математичний вираз")
      print(
          "\n3 > Дано координати поля шахівниці x, y\n(цілі числа, що лежать в діапазоні 1-8). З огляду на,\nщо ліве нижнє поле дошки (1, 1) є чорним,\nперевірити істинність висловлювання: «Дане поле є білим».\n"
      )
  
      choice = int(input("Select a task to test (1-3): "))
      if choice < 0 or choice >= 4:
        print("There is no task number", choice)
        input("Press Enter to continue...")
        cls()  #clear console
        continue
      elif choice == 1:
        task_1()
      elif choice == 2:
        task_2()
      elif choice == 3:
        task_3()
      elif choice == 0:
        check = False  #Exit the loop
    except ValueError:
      print("There is no task number", choice)
      input("Press Enter to continue...")
      cls()  #clear console
  
  cls()  #clear console
  
  print("Good luck!")