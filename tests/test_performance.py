import time
import unittest

from application import graph, bfs, dfs


class TestPerformance(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.parser = graph.PARSER
        self.graph = graph.GRAPH
        self.graph_to_dfs = graph.GRAPH_TO_DFS

    def _get_execution_period(self, function, **kwargs):
        start = time.time()
        function(**kwargs)
        end = time.time()
        return end - start

    def test_performance(self):
        bfs_period = self._get_execution_period(
            function=bfs.bfs, **{'graph': self.graph, 'start': 0, 'goal': 99},
        )
        bfs_uniform_period = self._get_execution_period(
            function=bfs.bfs,
            **{
                'graph': self.graph,
                'start': 0,
                'goal': 99,
                'uniform_weight': True,
            },
        )
        dfs_period = self._get_execution_period(
            function=dfs.dfs,
            **{'visited': set(), 'graph': self.graph_to_dfs, 'node': 0},
        )
        dfs_limited_period = self._get_execution_period(
            function=dfs.dfs_limited,
            **{
                'visited': set(),
                'graph': self.graph_to_dfs,
                'node': 0,
                'current': 0,
                'limit': 5,
            },
        )
        dfs_iterative_limit_period = self._get_execution_period(
            function=dfs.dfs_iterative_limit,
            **{
                'visited': set(),
                'graph': self.graph_to_dfs,
                'node': 0,
                'current': 0,
                'limit': 5,
            },
        )

        for period in [
            bfs_period,
            bfs_uniform_period,
            dfs_period,
            dfs_iterative_limit_period,
        ]:
            # dfs_limited is lt all because the limit is short
            assert dfs_limited_period < period

        assert dfs_period < bfs_period
        assert dfs_period < bfs_uniform_period
        assert bfs_uniform_period < bfs_period

        for period in [
            bfs_period,
            bfs_uniform_period,
            dfs_period,
            dfs_limited_period,
        ]:
            # dfs_iterative_limit is gt all
            assert dfs_iterative_limit_period > period


if __name__ == '__main__':
    unittest.main()
