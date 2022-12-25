# Implementing recurssion in python
def print_number(index: int, nums: list):
    """This function print's the elements present in the list """
    if index == len(nums):
        return
    print(nums[index])
    print_number(index + 1, nums)



def main():
    """This is a main function"""
    try:
        # Taking list input
        nums = [eval(i) for i in input("Enter the elements: ").split(",")]
        index = 0
        print_number(index, nums)
    except (KeyboardInterrupt, Exception) as e:
        print("Error occured: " + str(e))

if __name__ == "__main__":
    main()