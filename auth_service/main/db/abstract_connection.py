from abc import abstractmethod, ABC


class AbstractConnectionManager(ABC):
    '''
    class to open, create, serve and close Postgres connections

    conf -- configuration dependency (most external)

    must implement __init__(self, conf), close(self), get_connection(self)
    '''
    # TODO pool connections
    @abstractmethod
    def __init__(self, conf):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def get_connection(self):
        raise NotImplementedError
