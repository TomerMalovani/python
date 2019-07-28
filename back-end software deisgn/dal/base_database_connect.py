from abc import ABC, abstractmethod


class baseDatabas(ABC):
    @abstractmethod
    def add_animal(self, animal):
        pass

    @abstractmethod
    def get_animal(self, id):
        pass

    @abstractmethod
    def get_all_animals(self):
        pass

    @abstractmethod
    def delete_animal(self, id):
        pass

    @abstractmethod
    def update_animal(self, animal_id, animal_to_update):
        pass
