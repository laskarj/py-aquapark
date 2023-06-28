<<<<<<< HEAD
from abc import ABC, abstractmethod
from typing import Type
=======
from __future__ import annotations

from abc import ABC
from typing import Type, Optional


class SlideLimitationValidator(ABC):
    def __init__(
            self,
            age: int,
            weight: int,
            height: int,
    ) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class IntegerRange:
    def __init__(
            self,
            min_amount: int,
            max_amount: int,
    ) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(
            self,
            owner: SlideLimitationValidator,
            name: str
    ) -> None:
        self.public_name = name
        self.protected_name = "_" + name

    def __get__(
            self,
            instance: SlideLimitationValidator,
            owner: Optional[SlideLimitationValidator]
    ) -> int:

        return getattr(instance, self.protected_name)

    def __set__(
            self,
            instance: SlideLimitationValidator,
            value: int
    ) -> None:
        setattr(instance, self.protected_name, self.validate(value))

    def validate(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError(
                f"{self.public_name} should be integer."
            )

        if not self.min_amount <= value <= self.max_amount:
            raise ValueError(
                f"{self.public_name} should not be less than "
                f"{self.min_amount} and greater than {self.max_amount}"
            )

        return value
>>>>>>> 6546f13 (Rewrote the code.)


class Visitor:
    def __init__(
            self,
            name: str,
            age: int,
            weight: int,
            height: int,
    ) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


<<<<<<< HEAD
class SlideLimitationValidator(ABC):
    @abstractmethod
    def __init__(self, age: int, weight: int, height: int) -> None:
        self.age = age
        self.weight = weight
        self.height = weight

    @abstractmethod
    def get_access(self) -> bool:
        pass


class IntegerRange:

    def __init__(self, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.status_access = None

    def __set_name__(self,
                     owner: Type[SlideLimitationValidator],
                     name: str) -> None:
        self.status_access = "_" + name

    def __get__(self,
                instance: Type[SlideLimitationValidator],
                owner: Type[SlideLimitationValidator]
                ) -> bool:
        return getattr(instance, self.status_access)

    def __set__(self,
                instance: Type[SlideLimitationValidator],
                value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(
                f"{self.status_access} should be integer,"
                f" not a {type(value)}!"
            )
        setattr(
            instance,
            self.status_access,
            self.min_amount <= value <= self.max_amount
        )


=======
>>>>>>> 6546f13 (Rewrote the code.)
class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(4, 14)
    height = IntegerRange(80, 120)
    weight = IntegerRange(20, 50)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(14, 60)
    height = IntegerRange(120, 220)
    weight = IntegerRange(50, 120)


class Slide:
    def __init__(
            self,
            name: str,
<<<<<<< HEAD
            limitation_class: Type[SlideLimitationValidator]
=======
            limitation_class: Type[SlideLimitationValidator],
>>>>>>> 6546f13 (Rewrote the code.)
    ) -> None:
        self.name = name
        self.limitation_class = limitation_class

<<<<<<< HEAD
    def can_access(self, visitor: Type[Visitor]) -> bool:
        return self.limitation_class(
            age=visitor.age,
            weight=visitor.weight,
            height=visitor.height
        ).get_access()
=======
    def can_access(self, visitor: Visitor) -> bool:
        try:
            self.limitation_class(
                visitor.age,
                visitor.weight,
                visitor.height
            )
            return True

        except ValueError:
            return False
>>>>>>> 6546f13 (Rewrote the code.)
