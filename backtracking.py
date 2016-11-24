def edge_exists(i, j):
    return M[i][j] != 0


def visited(path, node):
    return node in path


def generate_loops(path, n):
    if len(path) == n:
        if edge_exists(path[-1], path[0]):
            path.append(path[0])
            print(path)
    else:
        for node in range(0, n):
            if not (visited(path, node) and edge_exists(path[-1], node)):
                temp_path = list(path)
                temp_path.append(node)
                generate_loops(temp_path, n)


def generate_all_loops(start_node, n):
    path = list()
    path.append(start_node)
    generate_loops(path, n)


if __name__ == '__main__':
    # graph example
    M = [[0 for j in range(0, 4)] for i in range(0, 4)]
    M[0][1] = 2
    M[1][0] = 1
    M[1][2] = 6
    M[2][1] = 7
    M[0][2] = 9
    M[2][3] = 8
    M[1][3] = 4
    M[3][1] = 3
    M[3][0] = 6
    # path example
    chemin = [0, 1]

    generate_all_loops(1, 4)
