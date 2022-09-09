from typing import Generic, NewType, Protocol, overload, TypeVar, Type, Any, Callable, Iterable, Union
from argparse import Namespace, ArgumentParser, Action, FileType
import argparse
import functools
from datetime import datetime
NewType
PT = NewType("PT",type["Parser"])
class NamedParser:
    def parse_args(self) -> PT:...

def argument_parser(ap:ArgumentParser):

    @functools.wraps(ap)
    def wraps() -> NamedParser:
        parser = ArgumentParser()
        for k,v in ap.__annotations__.items():
            if isinstance(v, Callable) and v.__name__ == "__add_argument__":
                v(parser)

            else:
                print(k,v)


        return parser
    return wraps

@overload
def argument(*name_or_flags: str, action: str | Type[Action] = ..., nargs: int | str | bool = ..., const: Any = ..., default: Any = ..., type: Callable[[str], Callable] | FileType = ..., choices: Iterable[Callable] | None = ..., required: bool = ..., help: str | None = ..., metavar: str | tuple[str, ...] | None = ..., dest: str | None = ..., version: str = ..., **kwargs: Any) -> Action:...
def argument(*args, **kwargs):
    def __add_argument__(parser:ArgumentParser):
        parser.add_argument(*args, **kwargs)    
    return __add_argument__
from pathlib import Path

# @argument_parser
T = TypeVar('T')

class Base(Generic[T]):
    @classmethod
    def create(cls, *args: tuple) -> T: ...

class Child(Base['Child']): ...


class BaseParser(ArgumentParser, Generic[T]):
    def __init__(self) -> None:
        baseags = dir(self)
        print(baseags)
        super().__init__()
        for key, value in self.__annotations__.items():
            super().add_argument(f"--{key}", required=False)


    def parse_args(self)->T:
        args =  super().parse_args()
        for key, value in self.__annotations__.items():
            if value ==  datetime:
                setattr(args,key, datetime.fromisoformat(getattr(args,key)))
            if value == Path:
                setattr(args,key, Path(getattr(args,key)))

        return args

class Parser(BaseParser["Parser"]):
    date:datetime =argument()
    file:Path

parser = Parser()

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
