class QuestRoom:
    def __init__(self, name: str, difficulty: int, player_limit: int):
        self.name = name
        self.difficulty = difficulty
        self.player_limit = player_limit
        self.players = []
        self.status = "waiting"
        self.events_log = []

    """Додає гравця, якщо є вільні місця."""
    def add_player(self, name: str):
        if len(self.players) >= self.player_limit:
            return "No free slots!"
        self.players.append(name)
        self.events_log.append(f"Player {name} joined")
        return True

    """Видаляє гравця."""
    def remove_player(self, name: str):
        if name in self.players:
            self.players.remove(name)
            self.events_log.append(f"Player {name} left")
            return True
        return "Player not found!"

    """Перевіряє, чи кімната повна."""
    def is_full(self) -> bool:
        return len(self.players) >= self.player_limit

    """Кількість вільних місць."""
    def free_slots(self) -> int:
        return self.player_limit - len(self.players)

    """Запускає квест."""
    def start(self):
        if not self.players:
            return "Room is empty!"
        self.status = "active"
        self.events_log.append("Quest started")
        return f"Quest '{self.name}' started with {len(self.players)} players!"

    """Скидає кімнату."""
    def reset_room(self):
        self.events_log.append("Room reset")
        self.players.clear()
        self.status = "waiting"
        return "Room reset!"

    """Повертає список гравців."""
    def players_list(self):
        if not self.players:
            return "No players in the room"
        return self.players[:]

    """Повертає історію подій."""
    def show_log(self):
        return self.events_log[:]

    def __str__(self):
        return f"QuestRoom: {self.name} | Difficulty: {self.difficulty} | Players: {len(self.players)}/{self.player_limit}"
    
room = QuestRoom("Піратський острів", 3, 4)
print(room)

room.add_player("Олег")
room.add_player("Даша")
print(room.start())
print(room)

print("Гравці:", room.players_list())
print("Вільних місць:", room.free_slots())
print("Лог:", room.show_log())



import unittest

class TestQuestRoom(unittest.TestCase):

    def setUp(self):
        self.room = QuestRoom("Підземелля дракона", 4, 5)

    # === Конструктор ===
    def test_constructor(self):
        self.assertEqual(self.room.name, "Підземелля дракона")
        self.assertEqual(self.room.difficulty, 4)
        self.assertEqual(self.room.player_limit, 5)
        self.assertEqual(self.room.players, [])
        self.assertEqual(self.room.status, "waiting")
        self.assertEqual(self.room.events_log, [])

    # === Додавання гравців ===
    def test_add_player(self):
        self.assertTrue(self.room.add_player("Андрій"))
        self.assertIn("Андрій", self.room.players)
        self.assertEqual(len(self.room.events_log), 1)

    def test_add_player_when_full(self):
        for i in range(5):
            self.room.add_player(f"Player{i}")
        result = self.room.add_player("Extra")
        self.assertEqual(result, "No free slots!")
        self.assertEqual(len(self.room.players), 5)

    # === Видалення гравців ===
    def test_remove_player(self):
        self.room.add_player("Олег")
        self.assertTrue(self.room.remove_player("Олег"))
        self.assertNotIn("Олег", self.room.players)

    def test_remove_nonexistent_player(self):
        self.assertEqual(self.room.remove_player("Ghost"), "Player not found!")

    # === Перевірка заповненості ===
    def test_is_full_and_free_slots(self):
        self.assertFalse(self.room.is_full())
        self.assertEqual(self.room.free_slots(), 5)

        for i in range(5):
            self.room.add_player(f"P{i}")
        self.assertTrue(self.room.is_full())
        self.assertEqual(self.room.free_slots(), 0)

    # === Старт кімнати ===
    def test_start_empty_room(self):
        self.assertEqual(self.room.start(), "Room is empty!")

    def test_start_success(self):
        self.room.add_player("Маша")
        self.room.add_player("Костя")
        result = self.room.start()
        self.assertIn("started with 2 players", result)
        self.assertEqual(self.room.status, "active")

    # === Скидання кімнати ===
    def test_reset_room(self):
        self.room.add_player("Олег")
        self.room.start()
        self.room.reset_room()

        self.assertEqual(len(self.room.players), 0)
        self.assertEqual(self.room.status, "waiting")
        self.assertIn("Room reset", self.room.events_log[-1])

    # === Список гравців ===
    def test_players_list(self):
        self.room.add_player("Степан")
        self.room.add_player("Софія")
        self.assertEqual(self.room.players_list(), ["Степан", "Софія"])

        empty_room = QuestRoom("Empty", 1, 3)
        self.assertEqual(empty_room.players_list(), "No players in the room")

    # === Лог подій ===
    def test_log_order(self):
        self.room.add_player("Антон")
        self.room.add_player("Богдан")
        self.room.remove_player("Антон")
        self.room.start()
        self.room.reset_room()

        log = self.room.show_log()
        self.assertEqual(log[0], "Player Антон joined")
        self.assertEqual(log[-1], "Room reset")


if __name__ == '__main__':
    unittest.main()