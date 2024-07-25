from typing import Any, List, Optional, Dict

class MySet:

    hash_table_size = 10000
    
    def __init__(self, ls: Optional[List[Any]] = None) -> None:
        self.hash_table: Dict[int, Any] = {}
        if ls is not None:
            for element in ls:
                self.add(element)

    def __len__(self):
        return len(self.hash_table)

    def add(self, element: Any) -> None:
        if not hasattr(element, '__hash__'):
            raise ValueError("The object can't be hashed")
        
        key = hash(element) // self.hash_table_size
        self.hash_table[key] = element

    def remove(self, element: Any) -> None:
        key = hash(element) // self.hash_table_size
        if key not in self.hash_table:
            raise KeyError("No such element")

        del self.hash_table[key]

    def discard(self, element: Any) -> None:
        key = hash(element) // self.hash_table_size
        if key in self.hash_table:
            del self.hash_table[key]

    def clear(self):
        self.hash_table.clear()

    def copy(self) -> "MySet":
        new_set = MySet()
        for val in self.hash_table.values():
            new_set.add(val)
        return new_set

    def difference(self, *args: "MySet") -> "MySet":
        tmp_set = self.copy()

        for other in args:
            for val in other.hash_table.values():
                tmp_set.discard(val)

        return tmp_set

    def __sub__(self, other: "MySet") -> "MySet":
        return self.difference(other)

    def union(self, *args: "MySet") -> "MySet":
        tmp_set = self.copy()

        for other in args:
            for val in other.hash_table.values():
                tmp_set.add(val)

        return tmp_set

    def __or__(self, other: "MySet") -> "MySet":
        return self.union(other)

    def intersection(self, *args: "MySet") -> "MySet":
        tmp_set = self.copy()

        for other in args:
            tmp_set = tmp_set & other

        return tmp_set

    def __and__(self, other: "MySet") -> "MySet":
        tmp_set = MySet()

        for val in self.hash_table.values():
            if val in other.hash_table.values():
                tmp_set.add(val)

        return tmp_set
                














            

