from src.utils import get_sum_of_cols_of_textlines

if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]

    sum_of_cols = get_sum_of_cols_of_textlines(data)
    num_of_lines = len(data)

    gamma_str = "".join("1" if i > num_of_lines // 2 else "0" for i in sum_of_cols)
    epsilon_str = "".join("0" if c == "1" else "1" for c in gamma_str)
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    print("Part 1:", gamma * epsilon)
