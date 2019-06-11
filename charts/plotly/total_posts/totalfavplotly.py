
import plotly.graph_objs as go
from plotly.offline import plot
from create.models import Create
from user.models import User
import datetime
total = Create.objects.count()

# date_formated =[]
# for d in create_date:
#     date_formated.append(datetime.datetime.strptime(d, "%B %d, %Y").strftime('%Y-%m-%d'))


def total_fav():
        # Create a trace
    trace = go.Scatter(
        x=['test'],
        y=[total]
    )

    data = [trace]

    fig = go.Figure(data=data)
    plot_div = plot(fig, output_type='div')
    return plot_div

