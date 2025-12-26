target = 5
data_list = [1, 2, 3, 4, 5]

def linear_search(data_list, target):
    for i in len(data_list):
        if data_list[i] == target:
            return i
    return -1

def main():
    print(linear_search(data_list, target))

if __name__ == "__main__":
    main()
