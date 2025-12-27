from random import randint as rd


inp_target = rd(1,10)
inp_list = []
for i in range (10):
    inp_list.append(rd(1,10))
print(f"list for input {inp_list}\ntarget for search = {inp_target}")

def linear_search(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1

def main():
    print(linear_search(inp_list, inp_target))

if __name__ == "__main__":
    main()
