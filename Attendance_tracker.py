def calc_attendance(total, attended):
    return (attended / total) * 100


def can_skip_classes(total, attended):
    skips = 0
    
    # keep checking until attendance drops below 75%
    while (attended / (total + skips)) * 100 >= 75:
        skips += 1

    return skips - 1


def classes_to_attend(total, attended):
    extra = 0

    # keep adding classes until attendance reaches 75%
    while ((attended + extra) / (total + extra)) * 100 < 75:
        extra += 1

    return extra


def main():
    print("=== Attendance Calculator ===")

    try:
        total = int(input("Total classes: "))
        attended = int(input("Classes attended: "))

        # basic checks
        if total <= 0 or attended < 0:
            print("Numbers should be positive.")
            return

        if attended > total:
            print("Attended can't be more than total.")
            return

        percent = calc_attendance(total, attended)

        print("\n--- Result ---")
        print(f"Attendance: {percent:.2f}%")

        if percent >= 75:
            print("You're safe 👍")
            skips = can_skip_classes(total, attended)
            print(f"You can skip {skips} more classes.")
        else:
            print("Below 75% ⚠️")
            needed = classes_to_attend(total, attended)
            print(f"You need to attend {needed} more classes in a row.")

    except ValueError:
        print("Enter valid numbers only.")


if __name__ == "__main__":
    main()
