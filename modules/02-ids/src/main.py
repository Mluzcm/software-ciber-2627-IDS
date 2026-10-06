from ips_poc.util.pattern_loader import patterns


def main():
    # Runs every main method
    print(patterns)
    for name, cls in patterns.items():
        cls().run()


if __name__ == "__main__":
    main()
