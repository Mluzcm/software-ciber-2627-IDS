from util.pattern_loader import pattern_dict


def main():
    # Runs every main method
    for name, cls in pattern_dict.items():
        cls().run()


if __name__ == "__main__":
    main()
