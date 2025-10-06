def high_and_low(numbers: str) -> str:
    # Split the string into a list of integers
    nums = list(map(int, numbers.split()))
    # Find the highest and lowest numbers
    highest = max(nums)
    lowest = min(nums)
    # Return them as a formatted string
    return f"{highest} {lowest}"

# Example usage
if __name__ == "__main__":
    print(high_and_low("1 2 3 4 5"))  # Output: "5 1"
    print(high_and_low("1 2 -3 4 5"))  # Output: "5 -3"
    print(high_and_low("1 9 3 4 -5"))  # Output: "9 -5"
