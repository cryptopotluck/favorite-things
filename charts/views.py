from django.shortcuts import render
from create.models import Create
import plotly.graph_objs as go
from plotly.offline import plot
# Create your views here.
from django.views.generic import TemplateView
from charts.plotly.total_posts.totalfavplotly import total_fav
from user.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def charts(request):
    # total = Create.objects.filter(author=request.user).count()
    # date = Create.objects.filter(author=request.user).filter('pub_date')
    config = request.user.username
    usernames = User.objects.filter()
    total = Create.objects.count()

    def total_fav():
        # Create a trace
        trace = go.Scatter(
            x=[config, 'total'],
            y=['test', total]
        )

        data = [trace]

        fig = go.Figure(data=data)
        plot_div = plot(fig, output_type='div')
        return plot_div

    context = {
            'plot': total_fav(),
            'users': usernames,
            'test': 'yes'
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
