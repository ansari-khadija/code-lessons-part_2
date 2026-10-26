import threading
import time


def data(name, course):
    print(f"📚 {name.title()} has started the {course.title()} session.")

    for i in range(5):
        print(f"⏳ {name.title()} is studying session--> {i + 1}")
        time.sleep(1)

    print(f"✅ {name.title()} completed the {course.title()} session.")


if __name__ == "__main__":

    name = input("Enter your name here: ")
    course = input("Enter your course name here: ")

    t1 = threading.Thread(
        target=data,
        args=(name, course),
        daemon=True
    )

    t1.start()

    time.sleep(2)

    print("🏁 Main program finished!")

