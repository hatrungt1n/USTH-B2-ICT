import main

choices = 1
while choices:
    choices = int(
        input(
            "If you want to see courses list, please type 1, students list, type 2, student marks, type 3, average marks for any students, type 4, another number to quit: "
        )
    )

    # List courses
    if choices == 1:
        main.listCourses()

    # List students
    elif choices == 2:
        main.listStudents()

    # Show student marks for a given course
    elif choices == 3:
        main.showMarks()

    # Show student average marks
    elif choices == 4:
        main.showAverageMarks()

    else:
        break