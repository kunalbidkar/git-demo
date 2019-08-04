from datetime import datetime


def curr_time():
    print(__name__)
    return datetime.now()


if __name__ == "__main__":
    print("Pranay")
    print(curr_time())
