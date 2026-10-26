from multiprocessing import Process


def data(name, course, course2):
    print(
        f"Welcome, dear {name.title()}! "
        f"Let's begin your {course2.title()} journey in learning {course.title()}."
    )

def duration(enroll,left,name, course, course2):
    print(
        f"Dear {name.title()}! "
        f"you have enrolled in {enroll}"
        f"you have left {left} in {course2.title()} journey in learning {course.title()}."
    )


if __name__ == "__main__":
    name = input("Enter your name here: ")
    course = input("Enter your course name here: ")
    course2 = input("Enter what subject you are learning: ")
    enroll = "1-8-2026"
    left = "6 months"

    p1 = Process(target=data, args=(name, course, course2))
    p2 = Process(target=duration, args=(enroll,left,name, course, course2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")
