from abc import ABCMeta, abstractmethod


class Action(metaclass=ABCMeta):
    def execute(self):
        return self.run()

    @abstractmethod
    def run(self):
        pass
