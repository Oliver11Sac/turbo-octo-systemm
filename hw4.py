school = {}

def creat_class(class_name):
    school[class_name] = []

def add_student(class_name, student_name):
    school[class_name].append(student_name)

def del_student(class_name, student_name):
    school[class_name].remove(student_name)

def transfer_student(class_name, new_class, student_name):
    del_student(student_name, class_name)
    add_student(student_name, new_class)

while True:
    admin = input('Выберете действие: ')
    if admin.lower() == 'добавить класс':
        admin = input('Введите класс: ')
        creat_class("admin_class")
        print('Класс успешно добавлен')
    elif admin.lower() == 'Добавить студента':
