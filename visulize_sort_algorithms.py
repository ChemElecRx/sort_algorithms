import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
import numpy as np

# Ensure the correct backend for matplotlib
plt.switch_backend('TkAgg')

def BubbleSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list.copy()

    fig, ax = plt.subplots()
    ax.set_title('Bubble Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    for i in range(len(sorted_list) - 1):
        for j in range(len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

                for k in range(len(sorted_list)):
                    bar_rects[k].set_height(sorted_list[k])
                plt.pause(0.5)

    plt.close(fig)
    return sorted_list

def InsertionSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list.copy()

    fig, ax = plt.subplots()
    ax.set_title('Insertion Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1
        while j >= 0 and key < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1

            for k in range(len(sorted_list)):
                bar_rects[k].set_height(sorted_list[k])
            plt.pause(0.5)

        sorted_list[j + 1] = key

    plt.close(fig)
    return sorted_list

def SelectionSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list.copy()

    fig, ax = plt.subplots()
    ax.set_title('Selection Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    for i in range(len(sorted_list)):
        min_index = i
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[min_index] > sorted_list[j]:
                min_index = j

        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

        for k in range(len(sorted_list)):
            bar_rects[k].set_height(sorted_list[k])
        plt.pause(0.5)

    plt.close(fig)
    return sorted_list

def ShellSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list.copy()

    fig, ax = plt.subplots()
    ax.set_title('Shell Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    n = len(sorted_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = sorted_list[i]
            j = i
            while j >= gap and sorted_list[j - gap] > temp:
                sorted_list[j] = sorted_list[j - gap]
                j -= gap
            sorted_list[j] = temp

            for k in range(len(sorted_list)):
                bar_rects[k].set_height(sorted_list[k])
            plt.pause(0.5)

        gap //= 2

    plt.close(fig)
    return sorted_list

def MergeSort(input_list):
    def merge_sort(input_list):
        if len(input_list) > 1:
            mid = len(input_list) // 2
            left_half = input_list[:mid]
            right_half = input_list[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    input_list[k] = left_half[i]
                    i += 1
                else:
                    input_list[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                input_list[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                input_list[k] = right_half[j]
                j += 1
                k += 1
            # Visualization code
            for k in range(len(input_list)):
                bar_rects[k].set_height(input_list[k])
            plt.pause(0.5)
            # End of visualization code

    if len(input_list) == 0:
        return []
    sorted_list = input_list.copy()

    fig, ax = plt.subplots()
    ax.set_title('Merge Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    merge_sort(sorted_list)

    plt.pause(0.5)  # Pause at the end to see the final sorted list
    plt.close(fig)  # Close the plot after sorting is complete

    return sorted_list


def QuickSort(input_list):
    def partition(input_list, low, high):
        pivot = input_list[high]
        i = low - 1
        for j in range(low, high):
            if input_list[j] < pivot:
                i += 1
                input_list[i], input_list[j] = input_list[j], input_list[i]
        input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]
        return i + 1

    def quick_sort(input_list, low, high):
        if low < high:
            pi = partition(input_list, low, high)
            # Visualization code
            for k in range(len(input_list)):
                bar_rects[k].set_height(input_list[k])
            plt.pause(0.5)
            # End of visualization code
            quick_sort(input_list, low, pi - 1)
            quick_sort(input_list, pi + 1, high)

    if len(input_list) == 0:
        return []
    sorted_list = input_list.copy()

    fig, ax = plt.subplots()
    ax.set_title('Quick Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    quick_sort(sorted_list, 0, len(sorted_list) - 1)

    plt.pause(0.5)  # Pause at the end to see the final sorted list
    plt.close(fig)  # Close the plot after sorting is complete

    return sorted_list


def RadixSort(input_list):
    def MaxBit(input_list):
        max_data = max(input_list)
        bits_num = 0
        while max_data:
            bits_num += 1
            max_data //= 10
        return bits_num

    def digit(num, d):
        p = 1
        while d > 1:
            d -= 1
            p *= 10
        return num // p % 10

    if len(input_list) == 0:
        return []
    sorted_list = input_list.copy()
    length = len(sorted_list)
    bucket = [0] * length

    fig, ax = plt.subplots()
    ax.set_title('Radix Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    for d in range(1, MaxBit(sorted_list) + 1):
        count = [0] * 10

        for i in range(0, length):
            count[digit(sorted_list[i], d)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(0, length)[::-1]:
            k = digit(sorted_list[i], d)
            bucket[count[k] - 1] = sorted_list[i]
            count[k] -= 1

        for i in range(0, length):
            sorted_list[i] = bucket[i]

        for i in range(len(sorted_list)):
            bar_rects[i].set_height(sorted_list[i])
        plt.pause(0.5)

    plt.close(fig)
    return sorted_list

def BinaryInsertSort(input_list):
    if len(input_list) == 0:
        return []
    
    sorted_list = input_list.copy()
    length = len(sorted_list)
    bucket = [0] * length

    fig, ax = plt.subplots()
    ax.set_title('Binary Insert Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    def BinarySearch(input_list, end, value):
        left = 0
        right = end - 1
        while left <= right:
            middle = left + (right - left) // 2
            if input_list[middle] >= value:
                right = middle - 1
            else:
                left = middle + 1
        return left if left < end else -1

    for i in range(1, len(input_list)):
        j = i - 1
        temp = sorted_list[i]
        insert_index = BinarySearch(sorted_list, i, sorted_list[i])
        if insert_index != -1:
            while j >= insert_index:
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
            sorted_list[j + 1] = temp

            # Visualization code
            for k in range(len(sorted_list)):
                bar_rects[k].set_height(sorted_list[k])
            plt.pause(0.5)

    plt.pause(0.5)  # Pause at the end to see the final sorted list
    plt.close(fig)  # Close the plot after sorting is complete

    return sorted_list

def HeapSort(input_list):
    def HeapAdjust(input_list, parent, length): 
        temp = input_list[parent]
        child = 2 * parent + 1

        while child < length:
            if child + 1 < length and input_list[child] < input_list[child+1]:
                child += 1
            if temp >= input_list[child]:
                break

            input_list[parent] = input_list[child]

            parent = child
            child = 2 * parent + 1
        input_list[parent] = temp

    if len(input_list) == 0:
        return []
    
    sorted_list = input_list.copy()
    length = len(sorted_list)

    fig, ax = plt.subplots()
    ax.set_title('Heap Sort Visualization')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    bar_rects = ax.bar(range(len(sorted_list)), sorted_list, align="edge")

    for i in range(length // 2, -1, -1):
        HeapAdjust(sorted_list, i, length)

    for j in range(1, length)[::-1]:
        temp = sorted_list[j]
        sorted_list[j] = sorted_list[0]
        sorted_list[0] = temp

        HeapAdjust(sorted_list, 0, j)

        # Visualization code
        for k in range(len(sorted_list)):
            bar_rects[k].set_height(sorted_list[k])
        plt.pause(0.5)

    plt.pause(0.5)  # Pause at the end to see the final sorted list
    plt.close(fig)  # Close the plot after sorting is complete

    return sorted_list

if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print('Before sorting:', input_list)

# Display menu options
print("Please select the sorting algorithm you want to visualize:")
print("1. Radix Sort")
print("2. Bubble Sort")
print("3. Quick Sort")
print("4. Merge Sort")
print("5. Shell Sort")
print("6. Selection Sort")
print("7. Insertion Sort")
print("8. Binary Insertion Sort")
print("9. Heap Sort")
print("0. Exit")

while True:
    choice = input("Please enter the sorting algorithm number: ")
    
    if choice == '0':
        print("Program exited.")
        break
    elif choice == '1':
        sorted_list = RadixSort(input_list)
    elif choice == '2':
        sorted_list = BubbleSort(input_list)
    elif choice == '3':
        sorted_list = QuickSort(input_list)
    elif choice == '4':
        sorted_list = MergeSort(input_list)
    elif choice == '5':
        sorted_list = ShellSort(input_list)
    elif choice == '6':
        sorted_list = SelectionSort(input_list)
    elif choice == '7':
        sorted_list = InsertionSort(input_list)
    elif choice == '8':
        sorted_list = BinaryInsertSort(input_list)
    elif choice == '9':
        sorted_list = HeapSort(input_list)
    else:
        print("Invalid choice. Please select again.")
        continue

    print('After sorting:', sorted_list)
    plt.show()  # Show the figure after the sorting algorithm is executed
    
    # Ask if the user wants to see another sorting
    next_action = input("Do you want to visualize another sorting? (Y/N): ").strip().lower()
    plt.close('all')  # Close all figures
    
    if next_action != 'y':
        print("Program exited.")
        break

