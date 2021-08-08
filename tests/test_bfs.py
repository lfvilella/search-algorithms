import unittest

from application import graph, bfs


class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.parser = graph.PARSER
        self.graph = graph.GRAPH

    def _parse_shortest_path(self, results):
        shortest_path = []
        for item in results:
            node = item
            if isinstance(item, tuple):
                node, _ = item

            shortest_path.append(self.parser[node])

        return shortest_path

    def test_sao_paulo_to_ipaussu(self):
        results = bfs.bfs(self.graph, 0, 33)
        assert results == [0, (11, 543), (22, 566), (33, 385)]
        assert self._parse_shortest_path(results) == [
            'SÃO PAULO',
            'BURITAMA',
            'SÃO LOURENÇO DA SERRA',
            'IPAUSSU',
        ]

    def test_sao_paulo_to_ipaussu_with_uniform_weight(self):
        results = bfs.bfs(self.graph, 0, 33, uniform_weight=True)
        assert results == [0, (11, 1), (22, 1), (33, 1)]
        assert self._parse_shortest_path(results) == [
            'SÃO PAULO',
            'BURITAMA',
            'SÃO LOURENÇO DA SERRA',
            'IPAUSSU',
        ]


if __name__ == '__main__':
    unittest.main()
