from airflow.lineage.backend import LineageBackend


class ExampleBackend(LineageBackend):

    def send_lineage(self, operator, inlets=None, outlets=None, context=None):
        print('test')

