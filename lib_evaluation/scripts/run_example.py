import sys
print(sys.path)
[print(element) for element in sys.path]


from lib_evaluation import lib_a, lib_b

def main():
    print(lib_a.get_df())
    print(lib_b.call_me())
    

if __name__ == "__main__":
    main()