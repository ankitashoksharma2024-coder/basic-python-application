import sys

def main():
    # Fallback default marks for Jenkins automated run if no args are passed
    if len(sys.argv) == 4:
        sub1 = float(sys.argv[1])
        sub2 = float(sys.argv[2])
        sub3 = float(sys.argv[3])
    else:
        print("[CI Mode] No inputs provided. Using automated test marks:")
        sub1, sub2, sub3 = 65.0, 45.0, 78.0

    total = sub1 + sub2 + sub3
    average = total / 3
    
    # Passing criteria: Average mark must be 40 or above
    status = "PASS" if average >= 40 else "FAIL"

    print("\n----- MARKS REPORT -----")
    print(f"Subject 1 : {sub1}")
    print(f"Subject 2 : {sub2}")
    print(f"Subject 3 : {sub3}")
    print("------------------------")
    print(f"Total     : {total}")
    print(f"Average   : {average:.2f}")
    print(f"Result    : {status}")
    print("------------------------")

if __name__ == "__main__":
    main()
