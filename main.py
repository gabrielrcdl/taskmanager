class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, name, description):
        task_id = len(self.tasks) + 1
        task = {"id": task_id, "name": name, "description": description}
        self.tasks.append(task)
        return task_id

    def update_task(self, task_id, name, description):
        if task_id <= 0 or task_id > len(self.tasks):
            return "Tarefa não encontrada"
        self.tasks[task_id - 1]["name"] = name
        self.tasks[task_id - 1]["description"] = description
        return f"Tarefa com ID {task_id} atualizada com sucesso"

    def delete_task(self, task_id):
        if task_id <= 0 or task_id > len(self.tasks):
            return "Tarefa não encontrada"
        deleted_task = self.tasks.pop(task_id - 1)
        return f"Tarefa com ID {task_id} excluída com sucesso"


def main():
    task_manager = TaskManager()

    # Criar uma nova tarefa
    task_id = task_manager.create_task(" ", "Description with empty name")
    print("CRIANDO TAREFA...\n")
    print(" Tarefa criada com ID:", task_id)
    print("\n")
    print("         Tarefa com nome vazio:\n            ", task_manager.tasks[-1])
    print("_____________________________________________________________________________________________________________")
    print("\n")

    # Atualizar uma tarefa existente
    tarefaAntes = task_manager.tasks[-1]

    print("ATUALIZANDO TAREFA...\n")
    print("         Tarefa ANTES:\n             ", tarefaAntes)
    update_result = task_manager.update_task(task_id, "Task 1 Updated", "Description 1 Updated")
    print("\n")

    print(update_result)
    print("\n")

    tarefaDepois = task_manager.tasks[-1]

    print("         Tarefa DEPOIS:\n             ", tarefaDepois)
    print("_____________________________________________________________________________________________________________")
    print("\n")



    # Deletar uma tarefa existente
    tarefaDeletada = task_manager.tasks[-1]
    delete_result = task_manager.delete_task(task_id)
    print("DELETANDO TAREFA...\n\n", delete_result)
    print("\n")
    print("         Tarefa DELETADA:\n             ", tarefaDeletada)



if __name__ == "__main__":
    main()
