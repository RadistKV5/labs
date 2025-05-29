# TODO: Подробно описать три произвольных класса
import doctest


class Parallelepiped:
    def __init__(self, height: float, width: float, length: float):
        """
        Создание и подготовка к работе объекта "Параллелепипед"

        :param height: Высота параллелепипеда
        :param width: Ширина параллелепипеда
        :param length: Длина параллелепипеда

        Примеры:
        >>> figure = Parallelepiped(15, 10, 13)
        """
        if type(height) != int and type(height) != float:
            raise TypeError("Сторона должна быть числом")
        elif height <= 0:
            raise ValueError("Сторона должна быть больше нуля")
        self.height = height
        if type(width) != int and type(width) != float:
            raise TypeError("Сторона должна быть числом")
        elif width <= 0:
            raise ValueError("Сторона должна быть больше нуля")
        self.width = width
        if type(length) != int and type(length) != float:
            raise TypeError("Сторона должна быть числом")
        elif length <= 0:
            raise ValueError("Сторона должна быть больше нуля")
        self.length = length

    def volume_missing_height(self, missing: float) -> float:
        """Функция, вычисляющая объём параллелепипеда с уменьшенной высотой

        :param missing: Часть высоты, на которую требуется уменьшить параллелепипед

        :raise ValueError: Если часть missing больше высоты, вызываем ошибку

        Примеры:
        >>> figure = Parallelepiped(15, 10, 13)
        >>> figure.volume_missing_height(5)
        1300
        """
        if type(missing) != int and type(missing) != float:
            raise TypeError("Сторона должна быть числом")
        elif missing <= 0:
            raise ValueError("Сторона должна быть больше нуля")
        else:
            self.missing = missing
        if self.height > missing:
            return self.width * self.length * (self.height - missing)
        else:
            return ValueError("Высота изначальная меньше отнимаемой")

    def sq(self) -> float:
        """Функция, вычисляющая площадь параллелепипеда с заранее заданной высотой равной 7

        Примеры:
        >>> figure = Parallelepiped(15, 10, 13)
        >>> figure.sq()
        650
                """
        length = 7
        return 2 * ((length * self.width)+(length * self.height)+(self.height * self.width))


class Cat:
    def __init__(self, weight: float, length: float):
        """
        Создание и подготовка к работе объекта "Кот"

        :param weight: Вес кота
        :param length: Длина кота от кончика носа до кончика хвоста

        Примеры:
        >>> cat = Cat(4, 60)
        """
        if type(weight) != int and type(weight) != float:
            raise TypeError("Вес должен быть числом")
        elif weight <= 0.1:
            raise ValueError("Вес должен быть больше 0,1")
        else:
            self.weight = weight
        if type(length) != int and type(length) != float:
            raise TypeError("Длина должна быть числом")
        elif length <= 10:
            raise ValueError("Длина должна быть больше 10 см")
        else:
            self.length = length

    def is_old(self, age: float) -> str:
        """
        Функция, которая выводит на экран надпись о том, старый ли кот или нет основываясь на возрасте, при этом возраст
         по умолчанию приравнивается к 13 годам

        :param age: Возраст кота

        :return: Является ли кот старым

        Примеры:
        >>> cat = Cat(4, 60)
        >>> cat.is_old(3)
        'Старичок уже'
        """
        if type(age) != int and type(age) != float:
            raise TypeError("Возраст должен быть числом")
        elif age <= 0:
            raise ValueError("Возраст должен быть больше нуля")
        else:
            age = 13
        if age >= 8:
            return "Старичок уже"
        else:
            return "Ещё молодой"

    def is_big_boy(self) -> str:
        """
        Функция проверяет, является ли кот большим основываясь на его размере и весе, нужно ли ему садиться на диету или же стоит покормить

        :return: Является ли кот большим, нужно ли ему садиться на диету или стоит покормить

        Примеры:
        >>> cat = Cat(4, 60)
        >>> cat.is_big_boy()
        'Ну покорми!'
        """
        if self.weight > 9 and self.length > 70:
            return "Здоровяк!"
        elif self.weight >= 8 and self.length < 70:
            return "Пора садиться на диету"
        elif self.weight < 8:
            return "Ну покорми!"


class FuelStation:
    def __init__(self, fuel_left: float, tank_capacity: float):
        """
        Создание и подготовка к работе объекта "Заправка"

        :param fuel_left: Количество оставшегося в хранилище топлива
        :param tank_capacity: Объём бака машины

        Примеры:
        >>> fuel_station = FuelStation(500, 60)
        """
        if type(fuel_left) != int and type(fuel_left) != float:
            raise TypeError("Количество оставшегося в хранилище топлива должно быть числом")
        elif fuel_left < 0:
            raise ValueError("Количество оставшегося в хранилище топлива неотрицательно")
        else:
            self.fuel_left = fuel_left
        if type(tank_capacity) != int and type(tank_capacity) != float:
            raise TypeError("Ёмкость бака должна быть числом")
        elif tank_capacity <= 0:
            raise ValueError("Ёмкость бака должна быть больше нуля")
        else:
            self.tank_capacity = tank_capacity

    def is_enough_to_fill(self) -> str:
        """
        Функция проверяет, хватит ли топлива для запрвки полного бака, объём топлива по умолчанию считается равным 1000
         литров

        :return: Хватит ли топлива и можно ли залить полный бак

        Примеры:
        >>> fuel_station = FuelStation(500, 60)
        >>> fuel_station.is_enough_to_fill()
        'Топлива хватит, лей до полного'
        """
        fuel_left = 1000
        if fuel_left >= self.tank_capacity:
            return "Топлива хватит, лей до полного"
        else:
            return "Топлива не хватит"

    def price_to_fill_up(self, price: float) -> float:
        """
        Сколько будет стоить заправка полного бака с текущими ценами

        :param price: Цена за литр топлива

        :return: Цена полного бака топлива

        Примеры:
        >>> fuel_station = FuelStation(500, 60)
        >>> fuel_station.price_to_fill_up(50)
        3000
                """
        if type(price) != int and type(price) != float:
            raise TypeError("Цена должна быть числом")
        elif price < 0:
            raise ValueError("Цена неотрицательна")
        else:
            self.price = price
        return price * self.tank_capacity

    def supplies(self, add_fuel: float) -> float:
        """
        Добавление топлива в хранилище
        :param add_fuel: Количество залитого топлива

        :return: Количество топлива в хранилище после добавления

        Примеры:
        >>> fuel_station = FuelStation(500, 60)
        >>> fuel_station.supplies(100)
        600
        """
        if type(add_fuel) != int and type(add_fuel) != float:
            raise TypeError("Количество залитого топлива должно быть числом")
        elif add_fuel <= 0:
            raise ValueError("Количество залитого топлива боольше нуля")
        else:
            self.add_fuel = add_fuel
        fuel_left_ = self.fuel_left + add_fuel
        self.fuel_left = fuel_left_
        return self.fuel_left


if __name__ == "__main__":
    doctest.testmod()
