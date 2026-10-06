import pkgutil, importlib
import ips_poc.patterns

# ID of pattern and class for all detected patterns
patterns: dict = {}


def pattern(pattern_id: str):
    def wrapper(cls):
        cls.pattern_id = pattern_id
        global patterns
        patterns[pattern_id] = cls
        return cls

    return wrapper


def reload_patterns() -> None:
    # Imports all modules in the ips_poc.patterns namespace
    for _, name, _ in pkgutil.iter_modules(ips_poc.patterns.__path__, ips_poc.patterns.__name__ + "."):
        importlib.import_module(name)


reload_patterns()
