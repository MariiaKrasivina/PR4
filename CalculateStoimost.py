class CalculateStoimost:
    colors = {"Белый": 1, "Синий": 1, "Жёлтый": 1.1, "Красный": 1, "Перламутровый": 1.2, "Серый металлик": 1.3}

    detali = {"Капот": 1, "Передняя дверь": 1.2, "Задняя дверь": 1.1, "Передний бампер": 1, "Задний бампер": 1, "Крыша": 1.1}

    def __init__(self, name_detali):
        self.name = name_detali

    def calculate_stoimost(self, color):
        if color not in self.colors:
            raise ValueError("Неизвестный цвет")
        if self.name not in self.detali:
            raise ValueError("Неизвестная деталь")
        stoimost = int(round(self.colors[color] * self.detali[self.name] * 12000, 0))
        return f"Стоимость покраски детали {self.name.lower()} в {color.lower()} цвет составит {stoimost} рублей."

example = CalculateStoimost("Капот")
print(example.calculate_stoimost("Жёлтый"))