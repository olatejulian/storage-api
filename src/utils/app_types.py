from pydantic import NewType, Union

Id = NewType('Id', Union(int, str))
