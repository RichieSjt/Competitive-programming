class Empleado: 
    def __init__(self, age, direct_manager): 
        self.age = age
        self.direct_manager = direct_manager
        self.parties = 0
        self.subordinados = list()

employees, parties = map(int, input().split())
tree = list()

#Creando los empleados
for i in range(employees):
    age, direct_manager = map(int, input().split())

    empleado = Empleado(age, direct_manager)
    tree.append(empleado)

#Buscando los subordinados de cada empleado
for i in range(employees):
    temp = tree[i].direct_manager-1
    if i != temp:
        tree[temp].subordinados.append(i)

#for empleado in tree:
#    print(empleado.__dict__)

#Creando las fiestas
for _ in range(parties):
    owner, left_range, right_range = map(int, input().split())
    #print(owner)
    queue = list()
    queue.append(owner-1)
    #print(queue)
    
    while queue:
        act = queue.pop(0)
        #print("----Act", act)
        if tree[act].age >= left_range and tree[act].age <= right_range:
            tree[act].parties +=1
            
            direct_manager_age = tree[tree[act].direct_manager-1].age
            if direct_manager_age >= left_range and direct_manager_age <= right_range:
                queue.append(act)
            for subordinate in tree[act].subordinados:
                subordinate_age = tree[subordinate].age
                if subordinate_age >= left_range and subordinate_age <= right_range:
                    queue.append(subordinate)

for empleado in tree:
    print(empleado.parties)
    
#{'age': 8, 'direct_manager': 1, 'parties': 0, 'subordinados': [2, 4, 7]}
#{'age': 3, 'direct_manager': 5, 'parties': 0, 'subordinados': [6, 8, 9]}
#{'age': 5, 'direct_manager': 1, 'parties': 0, 'subordinados': [3, 5]}
#{'age': 2, 'direct_manager': 3, 'parties': 0, 'subordinados': []}
#{'age': 4, 'direct_manager': 1, 'parties': 0, 'subordinados': [1]}
#{'age': 3, 'direct_manager': 3, 'parties': 0, 'subordinados': []}
#{'age': 1, 'direct_manager': 2, 'parties': 0, 'subordinados': []}
#{'age': 7, 'direct_manager': 1, 'parties': 0, 'subordinados': []}
#{'age': 2, 'direct_manager': 2, 'parties': 0, 'subordinados': []}
#{'age': 3, 'direct_manager': 2, 'parties': 0, 'subordinados': []}