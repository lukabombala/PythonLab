from html import document
from html.tags import body
import benchmark

environment_data = benchmark.environment_data

benchmark_data, benchmark_median = benchmark.run()

#benchmark_data = [[13, 13, 4, 4], [13, 13, 4, 3], [13, 13, 4, 4], [12, 13, 4, 4], [13, 13, 4, 5]]
#benchmark_median = [1, 2, 3, 4]

benchmark_median.insert(0, 'Median')
for i, elem in enumerate(benchmark_data):
    elem.insert(0, i+1)

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

            b.data_table(benchmark_median,
                         top_header=False,
                         header=header,
                         style={
                             "width": "50%",
                         }
                         )

            b.p("App author: Lukasz Bombala")


if __name__ == '__main__':
    run()
