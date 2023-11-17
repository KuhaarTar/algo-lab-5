import unittest
from src.dfs_in_dag import dfs_sort, read_from_file


class DfsInDagTest(unittest.TestCase):
    GRAPH_DICT = []

    def setUp(self) -> None:
        self.GRAPH_DICT = {
            "visa": ["foreignpassport", "hotel", "bankstatement"],
            "foreignpassport": ["nationalpassport", "militarycertificate"],
            "hotel": ["creditcard"],
            "bankstatement": ["nationalpassport"],
            "creditcard": ["nationalpassport"],
            "nationalpassport": ["birthcertificate"],
            "militarycertificate": ["nationalpassport"]
        }

    def test_find_path_in_dag_graph(self):
        result = dfs_sort(self.GRAPH_DICT)
        self.assertEqual(result,
                         ['visa', 'bankstatement', 'hotel', 'creditcard', 'foreignpassport', 'militarycertificate',
                          'nationalpassport', 'birthcertificate'])

    def test_read_graph_from_file(self):
        result = read_from_file("C:/Users/taras/PycharmProjects/govern_algo/test/govern.in")
        self.assertEqual(result, self.GRAPH_DICT)


if __name__ == "__main__":
    unittest.main
