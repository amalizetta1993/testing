import pytest

@pytest.fixture
def dismissal_teachers_test():
    return ['Иван Петров', 'Юлия Савина'], ['Глеб Орлов', 'Юлия Савина']

@pytest.fixture
def get_teacher_data_test():
    return f'Иван Петров, образование РГУ, опыт работы 4 года. Предмет Химия, должность Учитель 1 категории'


@pytest.fixture
def give_a_consultation_test():
    return 'Иван Петров провел консультацию в классе 9Б. По предмету Химия как Учитель 1 категории'

@pytest.fixture
def remove_mark_test():
    return 'Иван Петров удалил оценку 5 студенту Ангелина Скрябина. Предмет: Химия'

@pytest.fixture
def add_mark_test():
    return 'Иван Петров поставил оценку 5 студенту Ангелина Скрябина. Предмет: Химия'
    