def add_numbers(a, b):
    return a + b


def run_addition():
    if len(sys.argv) < 3:
        print("Usage: python jenkins_pipeline_codes.py <num1> <num2>")
        return

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    result = add_numbers(num1, num2)

    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum         : {result}")
