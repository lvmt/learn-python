from cutecharts.charts import Bar
from cutecharts.faker import Faker

from pywebio import start_server
from pywebio.output import put_html

def bar_base():
    chart = Bar("Bar-基本示例", width="100%")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    put_html(chart.render_notebook())

if __name__ == '__main__':
    start_server(bar_base, debug=True, port=93)