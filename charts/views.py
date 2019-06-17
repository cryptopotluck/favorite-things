from django.shortcuts import render
from create.models import Create
import plotly.graph_objs as go
from plotly.offline import plot
# Create your views here.
from django.views.generic import TemplateView
from user.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def charts(request):
    username = request.user.username
    total = Create.objects.count()
    users_post_total = Create.objects.filter(author=request.user.id).count()

    def total_fav():
        # Create a trace
        trace = go.Bar(
            x=[f'{username.capitalize()} Post\'s', 'Total Posts'],
            y=[users_post_total, total],
            text=[f'Total Favorites added by: {username.capitalize()}', 'Total Favorites added by all Users'],
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5,
                )
            ),
            opacity=0.6
        )

        data = [trace]

        layout = go.Layout(
            title='Showing off a Simple Graph',
        )


        fig = go.Figure(data=data, layout=layout)
        plot_div = plot(fig, output_type='div')
        return plot_div

    context = {
            'plot': total_fav(),
        }
    return render(request, 'charts/charts.html', context)

# class Chart(TemplateView):
#     template_name = 'charts/charts.html'
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(Chart, self).get_context_data(**kwargs)
#         context = {
#             'plot' : total_fav(),
#             'test' : Create.objects.order_by('pub_date'),
#             # 'test2' : User.objects.get(username='username')
#         }
#
#         return context
