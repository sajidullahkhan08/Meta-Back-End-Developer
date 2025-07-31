# Recursive function for the problem of Tower of Hanoi

def tower_of_hanoi(disks, source, target, helper):
    if disks == 1:
        print('Disk {} moved from {} to {}'.format(disks, source, target))
        return
    tower_of_hanoi(disks - 1, source, target, target)
    print('Disk {} moved from {} to {}'.format(disks, source, target))
    tower_of_hanoi(disks - 1, helper, source, target)

# Example usage
if __name__ == "__main__":
    disks = int(input("Enter the number of disks: "))
    tower_of_hanoi(disks, 'A', 'C', 'B')
