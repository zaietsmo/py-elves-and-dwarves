from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def player_info(self) -> int:
        pass

    @abstractmethod
    def get_rating(self) -> str:
        pass