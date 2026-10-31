from operator import itemgetter
class Conductor:
    def __init__(self, id: int, surname: str, salary: int, orchestra_id: int):
        self.id = id
        self.surname = surname
        self.salary = salary
        self.orchestra_id = orchestra_id

class Orchestra:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class ConductorOrchestra:
    def __init__(self, conductor_id: int, orchestra_id: int):
        self.conductor_id = conductor_id
        self.orchestra_id = orchestra_id

orchestras = [
    Orchestra(id=1, name="Государственный симфонический оркестр"),
    Orchestra(id=2, name="Камерный ансамбль"),
    Orchestra(id=3, name="Национальный филармонический оркестр")
]

conductors = [
    Conductor(id=1, surname="Алексеев", salary=85000, orchestra_id=1),
    Conductor(id=2, surname="Светланов", salary=120000, orchestra_id=1),
    Conductor(id=3, surname="Абрамов", salary=75000, orchestra_id=2),
    Conductor(id=4, surname="Гергиев", salary=150000, orchestra_id=3),
    Conductor(id=5, surname="Темирканов", salary=135000, orchestra_id=3)
]

conductor_orchestra = [
    ConductorOrchestra(conductor_id=1, orchestra_id=1),
    ConductorOrchestra(conductor_id=2, orchestra_id=1),
    ConductorOrchestra(conductor_id=2, orchestra_id=2),
    ConductorOrchestra(conductor_id=3, orchestra_id=2),
    ConductorOrchestra(conductor_id=4, orchestra_id=3),
    ConductorOrchestra(conductor_id=5, orchestra_id=3),
    ConductorOrchestra(conductor_id=1, orchestra_id=3)
]

one_to_many = [(o.name, c.surname, c.salary)
               for o in orchestras
               for c in conductors
               if c.orchestra_id == o.id]

many_to_many_term = [(o.name, co.orchestra_id, co.conductor_id)
                     for o in orchestras
                     for co in conductor_orchestra
                     if o.id == co.orchestra_id]
many_to_many = [(c.surname, c.salary, orch_name)
                for orch_name, orch_id, cond_id in many_to_many_term
                for c in conductors
                if c.id == cond_id]

print("Оркестры, у которых в названии присутствует слово «оркестр», и их дирижеры")
res_1 = {}
for orch_name, cond_surname, _ in one_to_many:
    if 'оркестр' in orch_name.lower():
        if orch_name not in res_1:
            res_1[orch_name] = []
        res_1[orch_name].append(cond_surname)
print(res_1)


print("\nОркестры со средней зарплатой дирижеров, отсортированные по средней зарплате (один-ко-многим)")
res_2_unsorted = []
for o in orchestras:
    # Фильтруем дирижеров для конкретного оркестра
    o_conds = list(filter(lambda x: x[0] == o.name, one_to_many))
    if o_conds:
        salaries = [salary for _, _, salary in o_conds]
        # Вычисляем среднюю зарплату и округляем до 2 знаков
        avg_salary = round(sum(salaries) / len(salaries), 2)
        res_2_unsorted.append((o.name, avg_salary))

# Сортировка по средней зарплате (второй элемент кортежа)
res_2 = sorted(res_2_unsorted, key=itemgetter(1))
print(res_2)


print("\nДирижеры, фамилия которых начинается на «А», и названия их оркестров")
res_3 = {}
for cond_surname, _, orch_name in many_to_many:
    if cond_surname.startswith('А'):
        if cond_surname not in res_3:
            res_3[cond_surname] = []
        res_3[cond_surname].append(orch_name)
print(res_3)
