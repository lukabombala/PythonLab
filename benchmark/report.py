from html import document
from html.tags import body
import benchmark

environment_data = benchmark.environment_data

benchmark_data = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

header = ['Execution:',
          '1 thread (s)',
          '4 threads (s)',
          '4 processes (s)',
          'processes based on number of CPUs (s)']


def run():
    doc = document("page")
    with doc:
        doc.head()
        with body(doc.file) as b:
            b.h1("Multithreading/Multiprocessing benchmark results")
            b.h2("Execution environment")

            for elem in environment_data:
                b.p(f'{elem[0]}: {elem[1]}')

            b.h2('Test results')
            b.p('The following table shows detailed test results:')

            b.data_table(benchmark_data,
                         top_header=False,
                         header=header,
                         style={
                            "width": "50%",
                         }
                         )

            b.h2("Summary")
            b.p("The following table shows the median of all results:")

            data = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

            b.data_table(data,
                         top_header=False,
                         header=header,
                         style={
                             "width": "50%",
                         }
                         )

            b.p("App author: Lukasz Bombala")


if __name__ == '__main__':
    run()
