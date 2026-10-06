from ips_poc.util.pattern_loader import pattern


@pattern("P002")
class Pattern2():
    def run(self):
        print("Hello from pattern 2")
