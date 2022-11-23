from collections import deque

from interface import PriorityQueue
from puzzle import Node


def path(node):
    route = []
    while node is not None:
        route.append(node)
        node = node.parent
    return reversed(route)


def a_star(root):
    frontier = PriorityQueue()
    frontier.push(Node(root))
    explored = set()

    while frontier:
        node = frontier.pop()

        if node.puzzle.solved():
            return path(node)

        explored.add(node.puzzle.board)

        for move in node.puzzle.actions():
            if move.board not in explored:
                frontier.push(Node(move, node))


def bfs(root):
    frontier = deque([Node(root)])
    explored = {root.board}

    if root.solved():
        return path(Node(root, None))

    while frontier:
        node = frontier.pop()

        for move in node.puzzle.actions():
            if move.board not in explored:
                if move.solved():
                    return path(Node(move, node))

                frontier.appendleft(Node(move, node))
                explored.add(move.board)
