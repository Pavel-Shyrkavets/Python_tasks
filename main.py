from tasks.longest_word import get_longest_word
from tasks.palindrome import check_str
from tasks.school_member import Teacher, Student
from tasks.time_decorator import time_decorator, print_execution_time
from tasks.epam_plot import plot

if __name__ == '__main__':
    phrase = "short longer longest"
    print(f"The longest word from '{phrase}' is '{get_longest_word(phrase)}'.\n")

    palindrome = "top spot"
    another_palindrome = "123 321"
    print(f"Is '{palindrome}' a palindrome? => {check_str(palindrome)}")
    print(f"Is '{another_palindrome}' a palindrome? => {check_str(another_palindrome)}\n")

    teacher = Teacher("John Doe", 50, 5000.00)
    student = Student("Peter Parker", 18, 85)
    print("Teacher => " + teacher.show())
    print("Student => " + student.show() + "\n")

    @time_decorator
    def func_add(a, b):
        return a + b
    x, y = 10, 20
    result = func_add(x, y)
    print_execution_time()
    print(f"{x} + {y} = {result}")

    plot()
