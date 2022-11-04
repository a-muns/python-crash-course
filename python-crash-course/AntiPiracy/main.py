'''This program validates the genuinness of a game disk using the input
name, disk number, and disk serial number. The input values are checked
against the acceptable values, and the result is then printed.'''

print("============================================================")
print("              PythonCo. Disk Validation Checker")
print("============================================================")

disk_name = input("Enter in the name of the disk and press ENTER: ")
disk_number = int(input("Enter in the disk number and press ENTER: "))
disk_serial = int(input("Enter in the disk serial number and press ENTER: "))

acceptable_names = [
  "Pac Man World", "Game of Life", "Call of Duty: Big Red One", "Cardinal Syn",
  "NHL \'99"
]
disk_number_min = int(1496833)
disk_number_max = int(5930214)
verified_count = 0


# Checks disk_name against names in acceptable_names
def name_verify(name):
  global verified_count
  for acceptable_name in acceptable_names:
    if (name == acceptable_name):
      verified_count += 1
      return "TRUE"
  return "FALSE"


# Checks disk_number against min and max disk numbers
def number_verify(number):
  global verified_count
  if (number >= disk_number_min) and (number <= disk_number_max):
    verified_count += 1
    return "TRUE"
  else:
    return "FALSE"


# Checks disk_name, then checks disk_serial against acceptable serial number
def serial_verify(serial, name):
  global verified_count
  if (disk_name == acceptable_names[0]):
    if (disk_serial == 40394):
      verified_count += 1
      return "TRUE"
    else:
      return "FALSE"
  elif (disk_name == acceptable_names[1]):
    if (disk_serial == 69302):
      verified_count += 1
      return "TRUE"
    else:
      return "FALSE"
  elif (disk_name == acceptable_names[2]):
    if (disk_serial == 76034):
      verified_count += 1
      return "TRUE"
    else:
      return "FALSE"
  elif (disk_name == acceptable_names[3]):
    if (disk_serial == 40395):
      verified_count += 1
      return "TRUE"
    else:
      return "FALSE"
  elif (disk_name == acceptable_names[4]):
    if (disk_serial == 22490):
      verified_count += 1
      return "TRUE"
    else:
      return "FALSE"
  else:
    return "FALSE"


print("\n\nRESULTS\n=================================================")
print("On Disk List:                   " + name_verify(disk_name))
print("Disk Number Match:              " + number_verify(disk_number))
print("Disk Serial Number Match:       " +
      serial_verify(disk_serial, disk_name))

# Final verdict
if (verified_count == 3):
  print("\nTHIS IS A GENUINE DISK.")
else:
  print("\nTHIS IS A PIRATED DISK.")
