#Write a program that prints the number of and the list of its arguments.
if __name__ == "__main__":
    import sys 

print(len(sys.argv), "arguments:")
print(sys.argv.pop(0))
#for i in sys.argv:
#    print(i)
