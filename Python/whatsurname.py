firstname=input()
lastname=input()
print(f"Hello {firstname} {lastname}! You just delved into python.")

#or
#-------------------------------------------------------------------------
def print_full_name(first_name,last_name):
    print(f'Hello {first_name} {last_name}! You just delved into python.')


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)