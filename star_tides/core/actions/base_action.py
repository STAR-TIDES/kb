''' star_tides.core.actions.base_action
'''
from abc import ABCMeta, abstractmethod


class Action(metaclass=ABCMeta):
    '''
    Every action should override the `run()` method.
    Designing actions this way allows for easy request lifecycle logging,
    and a standard invocation following the command pattern.

    Actions should be agnostic of controllers. They can invoke other actions
    or make calls to the service level for DB modifications.


    Invocation:
        resp = ChildClassAction(*args, **kwargs).execute()
    '''
    def execute(self):
        return self.run()

    @abstractmethod
    def run(self):
        ''' Must be implemented on every child class.
        '''
        pass
