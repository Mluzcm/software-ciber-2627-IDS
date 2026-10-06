import pkgutil, importlib
import patterns

# ID of pattern and class for all detected patterns
pattern_dict: dict = {}


def pattern(pattern_id: str):
    def wrapper(cls):
        cls.pattern_id = pattern_id
        global pattern_dict
        pattern_dict[pattern_id] = cls
        return cls

    return wrapper


def reload_patterns() -> None:
    # Imports all modules in the patterns namespace
    for _, name, _ in pkgutil.iter_modules(patterns.__path__, patterns.__name__ + "."):
        importlib.import_module(name)


reload_patterns()
