import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))

from main import Teacher, teacher1

def test_dismissal_teachers(dismissal_teachers_test):
    Teacher.dismissal_teachers('Глеб Орлов')
    assert Teacher.teachers == dismissal_teachers_test[0]
    assert not Teacher.teachers == dismissal_teachers_test[1]
    Teacher.dismissal_teachers('Вася')
    assert Teacher.teachers == dismissal_teachers_test[0]
       
def test_get_teacher_data(get_teacher_data_test):
    assert ' '.join(teacher1.get_teacher_data()) == get_teacher_data_test
    
def test_give_a_consultation(give_a_consultation_test):   
    assert ' '.join(teacher1.give_a_consultation('9Б')) == give_a_consultation_test
    
def test_add_mark(add_mark_test):
    assert ' '.join(teacher1.add_mark('Ангелина Скрябина', 5)) == add_mark_test
    
def test_remove_mark(remove_mark_test):
    assert ' '.join(teacher1.remove_mark('Ангелина Скрябина', 5)) == remove_mark_test   