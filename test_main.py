import unittest
from main import TaskManager
import datetime

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    # Testes Unitários
    def test_create_task(self):
        """Testa a criação de uma nova tarefa."""
        task_id = self.task_manager.create_task("Task 1", "Description 1")
        self.assertEqual(task_id, 1)

    def test_update_task(self):
        """Testa a atualização de uma tarefa existente."""
        self.task_manager.create_task("Task 1", "Description 1")
        update_result = self.task_manager.update_task(1, "Task 1 Updated", "Description 1 Updated")
        self.assertEqual(update_result, "Tarefa com ID 1 atualizada com sucesso")

    def test_delete_task(self):
        """Testa a exclusão de uma tarefa existente."""
        self.task_manager.create_task("Task 1", "Description 1")
        delete_result = self.task_manager.delete_task(1)
        self.assertEqual(delete_result, "Tarefa com ID 1 excluída com sucesso")

    def test_empty_task_list(self):
        """Testa se a lista de tarefas está vazia após a criação do objeto TaskManager."""
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_create_task_with_empty_name(self):
        """Testa o comportamento da função create_task quando o nome da tarefa é uma string vazia."""
        task_id = self.task_manager.create_task("", "Description")
        self.assertEqual(task_id, 0)

    # Testes de Função

    def test_update_non_existing_task(self):
        """Testa a atualização de uma tarefa que não existe."""
        update_result = self.task_manager.update_task(1, "Task 1 Updated", "Description 1 Updated")
        self.assertEqual(update_result, "Tarefa não encontrada")

    def test_delete_non_existing_task(self):
        """Testa a exclusão de uma tarefa que não existe."""
        delete_result = self.task_manager.delete_task(1)
        self.assertEqual(delete_result, "Tarefa não encontrada")

    def test_update_task_with_empty_name(self):
        """Testa a atualização de uma tarefa com nome vazio."""
        task_id = self.task_manager.create_task("Task 1", "Description 1")
        update_result = self.task_manager.update_task(task_id, "", "Description 1 Updated")
        self.assertEqual(update_result, "Nome da tarefa não pode ser vazio")

    def test_delete_task_with_invalid_id(self):
        """Testa a exclusão de uma tarefa com ID inválido."""
        delete_result = self.task_manager.delete_task(-1)
        self.assertEqual(delete_result, "ID da tarefa inválido")

    def test_create_multiple_tasks_and_check_list(self):
        """Testa a criação de múltiplas tarefas e verifica a lista de tarefas."""
        for i in range(1, 6):
            self.task_manager.create_task(f"Task {i}", f"Description {i}")
        
        self.assertEqual(len(self.task_manager.tasks), 5)
        for i, task in enumerate(self.task_manager.tasks):
            self.assertEqual(task["id"], i + 1)
            self.assertEqual(task["name"], f"Task {i + 1}")
            self.assertEqual(task["description"], f"Description {i + 1}")

    def test_update_task_description_only(self):
        """Testa a atualização apenas da descrição de uma tarefa."""
        task_id = self.task_manager.create_task("Task 1", "Description 1")
        update_result = self.task_manager.update_task(task_id, "Task 1", "Description 1 Updated")
        self.assertEqual(update_result, "Tarefa com ID 1 atualizada com sucesso")

    def test_delete_task_leaves_other_tasks_intact(self):
        """Testa se a exclusão de uma tarefa não afeta outras tarefas na lista."""
        for i in range(1, 4):
            self.task_manager.create_task(f"Task {i}", f"Description {i}")

        task_id_to_delete = 2
        self.task_manager.delete_task(task_id_to_delete)
        remaining_tasks = [task["id"] for task in self.task_manager.tasks]
        self.assertEqual(remaining_tasks, [1, 3])

if __name__ == '__main__':
    # Executa os testes
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskManager)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    # Salva os resultados em um arquivo de texto
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"test_results_{current_datetime}.txt"
    with open(log_filename, 'w') as file:
        file.write("Resultados dos Testes:\n")
        for test in test_result.failures:
            file.write(f"Teste {test[0].id()} falhou: {test[1]}\n")
        for test in test_result.errors:
            file.write(f"Erro no teste {test[0].id()}: {test[1]}\n")
        file.write(f"\n{test_result.testsRun} testes realizados.\n")

    print(f"Resultados dos testes salvos em '{log_filename}'.")
