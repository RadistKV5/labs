import doctest


class Truck:
    """
    Определение и подготовка к работе экземпляра класса "Грузовик"

    :param model_year: Год выпуска
    :param make: Производитель
    :param model: Модель

    Примеры:
    >>> truck = Truck(1986, "Kenworth", "W900B")
    """

    def __init__(self, model_year: int, make: str, model: str):
        self.model_year_ = model_year
        self.make_ = make
        self.model_ = model

    @property
    def model_year(self):
        """
                Инкапсуляция переменной model_year для упрощения дальнейшего написания программы и предотвращения
                возможных проблем в работе дочернего класса
            """
        return self.model_year_

    @property
    def make(self):
        """
                Инкапсуляция переменной make для упрощения дальнейшего написания программы и предотвращения
                возможных проблем в работе дочернего класса
            """
        return self.make_

    @property
    def model(self):
        """
                Инкапсуляция переменной model для упрощения дальнейшего написания программы и предотвращения
                возможных проблем в работе дочернего класса
            """
        return self.model_

    def __str__(self):
        """
            Метод, позволяющий вывести всю основную информацию о грузовике

            :return: Производитель, модель и год выпуска грузовика в одной строке

            Примеры:
            >>> truck = Truck(1986, "Kenworth", "W900B")
            >>> truck.__str__()
            'Производитель Kenworth. Модель W900B. Год выпуска 1986.'
        """
        return f'Производитель {self.make}. Модель {self.model}. Год выпуска {self.model_year}.'

    def __repr__(self):
        """
                    Метод, позволяющий вывести всю основную информацию о грузовике в консоль

                    :return: Производитель, модель и год выпуска грузовика в одной строке

                    Примеры:
                    >>> truck = Truck(1986, "Kenworth", "W900B")
                    >>> truck.__repr__()
                    "Truck(make='Kenworth', model='W900B', model_year=1986)"
                """
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, model_year={self.model_year!r})"

    def needs_repairs(self, current_year: int) -> bool:
        """
        Определяет нужен ли грузовику ремонт основываясь на его возрасте. Ремонт проводится каждые 7 лет за исключением
         новых машин

         :param current_year: Текущий год для определения возраста грузовика

         :return: Булевская переменная отражающая необходимость ремонта

         Примеры:
         >>> truck = Truck(1986, "Kenworth", "W900B")
         >>> truck.needs_repairs(2007)
         True
        """
        if current_year <= self.model_year:
            raise ValueError("Год должен быть больше года выпуска")
        if type(current_year) != int and type(current_year) != float:
            raise TypeError("Год должен быть числом")
        self.current_year = current_year
        if current_year - self.model_year != 0:
            return (current_year-self.model_year) % 7 == 0
        else:
            return False

    def is_old(self, current_year: int) -> bool:
        """
        Определяет, изношен ли грузовик основываясь на его возрасте. Грузовик считается изношенным, если ему не меньше
         15 лет

        :param current_year: Текущий год для определения возраста грузовика

        :return: Булевская переменная отражающая высокую степень износа

        Примеры:
         >>> truck = Truck(1986, "Kenworth", "W900B")
         >>> truck.is_old(2007)
         True
        """
        if current_year <= self.model_year:
            raise ValueError("Год должен быть больше года выпуска")
        if type(current_year) != int and type(current_year) != float:
            raise TypeError("Год должен быть числом")
        self.current_year = current_year
        return current_year - self.model_year >= 15


class Heavy(Truck):
    """
        Определение и подготовка к работе экземпляра подкласса "Тяжёлый грузовик"

        :param model_year: Год выпуска
        :param make: Производитель
        :param model: Модель
        :param cargo_capacity: Грузоподъёмность в тоннах
        :param mileage: Пробег в километрах

        Примеры:
        >>> truck = Heavy(1986, "Kenworth", "W900B", 25, 2300000)
        """
    def __init__(self, model_year, make, model, cargo_capacity: float, mileage: int):
        super().__init__(model_year, make, model)
        self.cargo_capacity_ = cargo_capacity
        self.mileage_ = mileage

    @property
    def cargo_capacity(self):
        """
        Инкапсуляция переменной cargo_capacity для упрощения дальнейшего написания программы и предотвращения
        возможных сбоев в работе программы
        """
        return self.cargo_capacity_

    @cargo_capacity.setter
    def cargo_capacity(self, value):
        """
        Инкапсуляция переменной cargo_capacity для упрощения дальнейшего написания программы и предотвращения
        возможных сбоев в работе программы
        """
        if value <= 0:
            raise ValueError("Грузоподъёмность должна быть больше нуля")
        if type(value) != int and type(value) != float:
            raise TypeError("Грузоподъёмность должна быть числом")
        self.cargo_capacity_ = value

    @property
    def mileage(self):
        """
        Инкапсуляция переменной mileage для упрощения дальнейшего написания программы и предотвращения
        возможных сбоев в работе программы
        """
        return self.mileage_

    @mileage.setter
    def mileage(self, value):
        """
        Инкапсуляция переменной mileage для упрощения дальнейшего написания программы и предотвращения
        возможных сбоев в работе программы
        """
        if value < 0:
            raise ValueError("Пробег должен быть не меньше нуля")
        if type(value) != int and type(value) != float:
            raise TypeError("Пробег должен быть числом")
        self.mileage_ = value

    def can_haul_cargo(self, cargo: float) -> bool:
        """
        Определяет, может ли грузовик увезти некоторый груз

        :param cargo: Масса груза в тоннах

        :return: Булевская переменная, показывающая может ли грузовик увезти груз

        Примеры:
        >>> truck = Heavy(1986, "Kenworth", "W900B", 25, 2300000)
        >>> truck.can_haul_cargo(20)
        True
        """
        if cargo <= 0:
            raise ValueError("Масса груза должна быть больше нуля")
        if type(cargo) != int and type(cargo) != float:
            raise TypeError("Масса груза должна быть числом")
        self.cargo = cargo
        return cargo <= self.cargo_capacity

    def __str__(self):
        """
        Перегрузка метода __str__ для упрощения написания кода
        Метод, позволяющий вывести всю основную информацию о грузовике

            :return: Производитель, модель, год выпуска, грузоподъёмность и пробег грузовика в одной строке

            Примеры:
            >>> truck = Heavy(1986, "Kenworth", "W900B", 25, 2300000)
            >>> truck.__str__()
            'Производитель Kenworth. Модель W900B. Год выпуска 1986. Грузоподъёмность 25 т. Пробег 2300000 км.'
        """
        return f'Производитель {self.make}. Модель {self.model}. Год выпуска {self.model_year}.' \
               f' Грузоподъёмность {self.cargo_capacity} т. Пробег {self.mileage} км.'

    def __repr__(self):
        """
        Перегрузка метода __repr__ для упрощения написания кода
        Метод, позволяющий вывести всю основную информацию о грузовике в консоль

        :return: Производитель, модель и год выпуска грузовика в одной строке

        Примеры:
        >>> truck = Heavy(1986, "Kenworth", "W900B", 25, 2300000)
        >>> truck.__repr__()
        "Heavy(make='Kenworth', model='W900B', model_year=1986, cargo_capacity=25, mileage=2300000)"
        """
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, model_year={self.model_year!r}," \
               f" cargo_capacity={self.cargo_capacity!r}, mileage={self.mileage!r})"

    def needs_repairs(self, current_year: int) -> bool:
        """
        Определяет нужен ли грузовику ремонт основываясь на его возрасте или пробеге. Ремонт проводится каждые 10 лет
        1000000 км пробега

         :param current_year: Текущий год для определения возраста грузовика

         :return: Булевская переменная отражающая необходимость ремонта

         Примеры:
         >>> truck = Heavy(1986, "Kenworth", "W900B", 25, 2300000)
         >>> truck.needs_repairs(2009)
         True
        """
        if current_year <= self.model_year:
            raise ValueError("Год должен быть больше года выпуска")
        if type(current_year) != int and type(current_year) != float:
            raise TypeError("Год должен быть числом")
        self.current_year = current_year
        if (current_year-self.model_year) % 10 != 0 or current_year-self.model_year < 10:
            return self.mileage >= 1000000
        else:
            return True

    def is_old(self, current_year: int) -> bool:
        """
        Определяет, изношен ли грузовик основываясь на его возрасте. Грузовик считается изношенным, если ему не меньше
         20 лет

        :param current_year: Текущий год для определения возраста грузовика

        :return: Булевская переменная отражающая высокую степень износа

        Примеры:
         >>> truck = Truck(1986, "Kenworth", "W900B")
         >>> truck.is_old(2007)
         True
        """
        if current_year <= self.model_year:
            raise ValueError("Год должен быть больше года выпуска")
        if type(current_year) != int and type(current_year) != float:
            raise TypeError("Год должен быть числом")
        self.current_year = current_year
        return current_year - self.model_year >= 20


if __name__ == "__main__":
    doctest.testmod()
