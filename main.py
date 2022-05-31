from IPython.display import display, HTML
import pandas as pd
import pygal
from sklearn.cluster import DBSCAN


base_html = """
<!DOCTYPE html>
<html>
  <head>
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
  <script type="text/javascript" src="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js""></script>
  </head>
  <body>
    <figure>
      {rendered_chart}
    </figure>
  </body>
</html>
"""

dataFrame = pd.read_json(r"MOCK_DATA.json")
print(dataFrame.head())


disp_dict = {}
for index, row in dataFrame.iterrows():
    if row['User'] not in disp_dict.keys():
        disp_dict[row['User']] = [(row['Latitude'], row['Longitude'])]
    else:
        disp_dict[row['User']].append((row['Latitude'], row['Longitude']))
xy_chart = pygal.XY(stroke=False)
[xy_chart.add(k,v) for k,v in sorted(disp_dict.items())]
display(HTML(base_html.format(rendered_chart=xy_chart.render(is_unicode=True))))