from abc import ABC, abstractmethod

# ממשק בסיסי עבור מחזורי סטודנטים
class StudentBatch(ABC):
    @abstractmethod
    def students_entered(self):
        pass

    @abstractmethod
    def students_in_army(self):
        pass

    @abstractmethod
    def students_in_cyber(self):
        pass

    @abstractmethod
    def expected_salary(self):
        pass


# מימוש עבור מחזור 1
class Batch1(StudentBatch):
    def students_entered(self):
        return 100

    def students_in_army(self):
        return 50

    def students_in_cyber(self):
        return 30

    def expected_salary(self):
        return 1200000  # סכום משוער בשוק העבודה


# מימוש עבור מחזור 2
class Batch2(StudentBatch):
    def students_entered(self):
        return 120

    def students_in_army(self):
        return 60

    def students_in_cyber(self):
        return 40

    def expected_salary(self):
        return 1300000  # סכום משוער בשוק העבודה


# השוואה בסיסית בין מחזורים
def compare_batches(batch1, batch2):
    print(f"מחזור 1 - סטודנטים נכנסו: {batch1.students_entered()}, סך הכל בצבא: {batch1.students_in_army()}, סך הכל בסייבר: {batch1.students_in_cyber()}, שכר משוער: {batch1.expected_salary()}")
    print(f"מחזור 2 - סטודנטים נכנסו: {batch2.students_entered()}, סך הכל בצבא: {batch2.students_in_army()}, סך הכל בסייבר: {batch2.students_in_cyber()}, שכר משוער: {batch2.expected_salary()}")


# יצירת אובייקטים וקריאה לפונקציות
batch1 = Batch1()
batch2 = Batch2()

compare_batches(batch1, batch2)

