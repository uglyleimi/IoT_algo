import unittest
import tempfile
import os
from collections import defaultdict
from max_flow import read_roads, build_graph, bfs, edmonds_karp, solve


def write_csv(lines: list[str]) -> str:
    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8')
    tmp.write('\n'.join(lines))
    tmp.close()
    return tmp.name


class TestReadRoads(unittest.TestCase):

    def test_normal_read(self):
        path = write_csv(["F1,F2", "S1,S2", "F1,X1,5", "X1,S1,3"])
        farms, shops, edges = read_roads(path)
        self.assertEqual(farms, ["F1", "F2"])
        self.assertEqual(shops, ["S1", "S2"])
        self.assertEqual(edges, [("F1", "X1", 5), ("X1", "S1", 3)])
        os.unlink(path)

    def test_ignores_blank_lines(self):
        path = write_csv(["F1", "S1", "", "F1,S1,7", ""])
        _, _, edges = read_roads(path)
        self.assertEqual(len(edges), 1)
        os.unlink(path)

    def test_raises_on_bad_edge_format(self):
        path = write_csv(["F1", "S1", "F1,S1"])
        with self.assertRaises(ValueError):
            read_roads(path)
        os.unlink(path)

    def test_raises_when_too_few_lines(self):
        path = write_csv(["F1"])
        with self.assertRaises(ValueError):
            read_roads(path)
        os.unlink(path)


class TestBuildGraph(unittest.TestCase):

    def test_simple_edges(self):
        g = build_graph([("A", "B", 5), ("B", "C", 3)])
        self.assertEqual(g["A"]["B"], 5)
        self.assertEqual(g["B"]["C"], 3)

    def test_parallel_edges_are_summed(self):
        g = build_graph([("A", "B", 4), ("A", "B", 6)])
        self.assertEqual(g["A"]["B"], 10)

    def test_reverse_edge_starts_at_zero(self):
        g = build_graph([("A", "B", 5)])
        self.assertEqual(g["B"]["A"], 0)


class TestBFS(unittest.TestCase):

    def test_finds_direct_path(self):
        g = defaultdict(lambda: defaultdict(int))
        g["S"]["T"] = 10
        parent = {}
        self.assertTrue(bfs(g, "S", "T", parent))
        self.assertEqual(parent["T"], "S")

    def test_no_path_when_capacity_zero(self):
        g = defaultdict(lambda: defaultdict(int))
        g["S"]["T"] = 0
        self.assertFalse(bfs(g, "S", "T", {}))

    def test_finds_multi_hop_path(self):
        g = defaultdict(lambda: defaultdict(int))
        g["S"]["M"] = 5
        g["M"]["T"] = 3
        parent = {}
        self.assertTrue(bfs(g, "S", "T", parent))
        self.assertEqual(parent["M"], "S")
        self.assertEqual(parent["T"], "M")

    def test_no_path_in_disconnected_graph(self):
        g = defaultdict(lambda: defaultdict(int))
        g["S"]["A"] = 5
        g["B"]["T"] = 5
        self.assertFalse(bfs(g, "S", "T", {}))


class TestEdmondsKarp(unittest.TestCase):

    def test_single_path(self):
        g = build_graph([("S", "A", 7), ("A", "T", 7)])
        self.assertEqual(edmonds_karp(g, "S", "T"), 7)

    def test_bottleneck(self):
        g = build_graph([("S", "A", 10), ("A", "T", 3)])
        self.assertEqual(edmonds_karp(g, "S", "T"), 3)

    def test_two_parallel_paths(self):
        g = build_graph([
            ("S", "A", 4), ("A", "T", 4),
            ("S", "B", 6), ("B", "T", 6),
        ])
        self.assertEqual(edmonds_karp(g, "S", "T"), 10)

    def test_diamond_graph(self):
        g = build_graph([
            ("S", "A", 3), ("A", "T", 3),
            ("S", "B", 4), ("B", "T", 4),
        ])
        self.assertEqual(edmonds_karp(g, "S", "T"), 7)

    def test_zero_flow_when_no_path(self):
        g = build_graph([("S", "A", 5)])
        self.assertEqual(edmonds_karp(g, "S", "T"), 0)

    def test_classic_example(self):
        g = build_graph([
            ("S", "A", 10), ("S", "B", 10),
            ("A", "C", 4),  ("A", "B", 2),
            ("B", "D", 9),
            ("C", "T", 10), ("C", "D", 6),
            ("D", "T", 10),
        ])
        self.assertEqual(edmonds_karp(g, "S", "T"), 13)


class TestSolveEndToEnd(unittest.TestCase):

    def test_direct_farm_to_shop(self):
        path = write_csv(["F1", "S1", "F1,S1,5"])
        self.assertEqual(solve(path), 5)
        os.unlink(path)

    def test_two_farms_one_shop(self):
        path = write_csv(["F1,F2", "S1", "F1,S1,3", "F2,S1,4"])
        self.assertEqual(solve(path), 7)
        os.unlink(path)

    def test_bottleneck_in_middle(self):
        path = write_csv(["F1", "S1", "F1,X1,10", "X1,S1,2"])
        self.assertEqual(solve(path), 2)
        os.unlink(path)

    def test_multiple_farms_shops_and_intersections(self):
        path = write_csv([
            "F1,F2,F3",
            "S1,S2,S3,S4,S5",
            "F1,X1,10", "F1,X2,8",
            "F2,X2,6",  "F2,X3,7",
            "F3,X3,9",  "F3,X4,5",
            "X1,X5,6",  "X1,X6,4",
            "X2,X5,8",  "X2,X6,5",
            "X3,X6,7",  "X3,X7,6",
            "X4,X7,8",
            "X5,S1,5",  "X5,S2,6",
            "X6,S2,4",  "X6,S3,7",  "X6,S4,3",
            "X7,S3,5",  "X7,S4,6",  "X7,S5,8",
        ])
        self.assertEqual(solve(path), 36)
        os.unlink(path)

    def test_farm_not_connected_to_any_shop(self):
        path = write_csv(["F1", "S1", "F1,X1,10"])
        self.assertEqual(solve(path), 0)
        os.unlink(path)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            solve("this_file_does_not_exist.csv")


if __name__ == "__main__":
    unittest.main(verbosity=2)