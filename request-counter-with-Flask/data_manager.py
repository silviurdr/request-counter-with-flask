

def read_stats_from_file():

    f = open("stats_data/request_counts.txt", "r")
    all_stats = f.read().splitlines()
    return all_stats


def write_stats_to_file(dictionary):

    f = open("stats_data/request_counts.txt", "w+")

    for key, value in dictionary.items():
        f.writelines(f"{key}:{value}\n")
    f.close()
