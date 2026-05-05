def number_the_tasks(file_path):

    data_from_file = []

    with open(file_path, "r", encoding="utf-8") as f:
        
        for line in f:
            data_from_file.append(line.strip())

    number_todo_list = []
    number = 1

    for element in data_from_file:
        number_line = f"{number}. {element}"
        number_todo_list.append(number_line)
        number += 1 #number = number +1

    with open(file_path, "w", encoding="utf-8") as f:
        for element in number_todo_list:
            f.write(element + "\n")

   

    number_the_tasks(r"data\todo.txt")
