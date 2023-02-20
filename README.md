# 8-Puzzle

Features a walkthrough for the optimal elucidation of [8-Puzzle](https://en.wikipedia.org/wiki/15_puzzle) with [Pygame](https://www.pygame.org/docs/) via [A* Search](https://en.wikipedia.org/wiki/A*_search_algorithm) and [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search) Algorithms.

![image](https://user-images.githubusercontent.com/79562517/200164354-8dc269c3-0146-4d63-9fd2-dbc4ae0802b3.png)

## Customization

[`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__) is a static method with the class as its first argument (`object.__new__(cls[, ...])` the residue are those handed to the object constructor expression), of which we bid an instance.

Typical implementations invoke the superclass's [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__) method — `super().__new__(cls[, ...])` to instantiate an object with appropriate arguments. More than anything else, Python propounded this mechanism (often overridden in custom metaclasses) as a privilege for subclasses of immutable types (as though *int*, *str*, or *tuple*) to tweak instance fabrication prior and deliver it to the caller.

### namedtuple

I employed this factory function to produce *tuple* subclasses with named fields accessible through attribute lookup or index. The `Puzzle` subclass initializes [`__slots__`](https://docs.python.org/3/library/collections.html#collections.namedtuple:~:text=The%20subclass%20shown%20above%20sets%20__slots__%20to%20an%20empty%20tuple.%20This%20helps%20keep%20memory%20requirements%20low%20by%20preventing%20the%20creation%20of%20instance%20dictionaries.) to an empty *tuple* to preserve memory requirements low as it averts the outset of instance dictionaries.

Why? It's [overkill](https://www.accelebrate.com/blog/named-tuples-in-python) to ply a class for this scheme.

## deque

Deques (pronounced “deck” and short for “double-ended queue”) are an abstraction of stacks and queues. It supports thread-safe, memory-efficient, and swift appends and pops on either flank of the [deque](https://docs.python.org/3/library/collections.html#deque-objects) with nigh parallel O(1) performance.

## heapq

[Heaps](https://docs.python.org/3/library/heapq.html) are binary trees for which every parent node boasts a value less than or equal to any of its children. The cogent property of a [heap](https://docs.python.org/3/library/heapq.html#:~:text=property%20of%20a-,heap,-is%20that%20its) is that its smallest element, on all occasions, is the root.

Skim through [here](https://docs.python.org/3/library/heapq.html#:~:text=algorithms%20in%20two-,aspects,-%3A%20(a)%20We%20use) on what its pop method yields and witness the disparity in textbooks.

### Priority Queue

> I devised a priority queue ([abstract data type](https://en.wikipedia.org/wiki/Priority_queue)) with the aid of a [heap](https://docs.python.org/3/library/heapq.html) to encapsulate the node alongside a [heuristic](https://en.wikipedia.org/wiki/Heuristic_(computer_science)), as it is what quantifies the precedence. [How?](https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes:~:text=Priority%20Queue-,Implementation,-Notes%C2%B6)

## Admissible Heuristic

[Manhattan Distance](https://en.wikipedia.org/wiki/Admissible_heuristic#:~:text=The%20Manhattan%20distance%20is%20an,itself%20and%20its%20correct%20position.)

## Ellipsis

An ellipsis operates as a placeholder equivalent to the *pass* keyword. With three dots, it somewhat evokes minimal visual clutter and discards extraneous code.

## How-Tos

### Precursive

As `Makefile` executions call for [py-make](https://github.com/tqdm/py-make),

```bash
$ pip install py-make
```

Clone the repository to your local machine via HTTPS:

```bash
$ git clone https://github.com/jamespatrickryan/8-puzzle.git
```

Navigate to the directory through its relative path:

```bash
$ cd 8-puzzle
```

and

```bash
$ pymake run
```

## An amalgam of Online Resources

- [John Levine](https://en.wikipedia.org/wiki/A*_search_algorithm) - A* Search
- [Abdul Bari](https://www.youtube.com/watch?v=pcKY4hjDrxk) - Graph Traversals
- [Luke Garringan](https://dev.to/lukegarrigan/what-is-bfs-breadth-first-search-nad) - What is BFS? (Breadth-first Search)
- [Aniket Bhattacharyea](https://earthly.dev/blog/python-makefile/) - Makefile
- [MIT OpenCourseWare](https://www.youtube.com/watch?v=gGQ-vAmdAOI&list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi&index=5) - Search: ..., Branch and Bound, A*
- [docs.python.org](https://docs.python.org/3/library/collections.html) - collections — Container
- [docs.python.org](https://docs.python.org/3/library/heapq.html) - heapq — Heap queue algorithm
- [docs.python.org](https://docs.python.org/3/reference/datamodel.html) - Data model
- [pygame.org](https://www.pygame.org/docs/) - Pygame front-page
