import threading
import time


def data(name, course):
    print(f"📚 {name.title()} has started the {course.title()} session.")
    time.sleep(3)
    print(f"✅ {name.title()} completed the {course.title()} session.")


if __name__ == "__main__":

    name = input("Enter your name here: ")
    course = input("Enter your course name here: ")

    t1 = threading.Thread(target=data, args=(name, course))

    print(f"🔐 {name.title()} logged in to the {course.title()} course.")

    # start()
    t1.start()

    # is_alive() → used only once
    print(f"📊 Is {name.title()} currently attending? {t1.is_alive()}")

    # join()
    t1.join()

    print(f"🎉 {name.title()} has completed the session!")

    print("Done!")
