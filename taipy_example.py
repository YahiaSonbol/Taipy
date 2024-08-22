from taipy.gui import Gui, navigate
import taipy.gui.builder as tgb
from taipy.gui.icon import Icon

stylekit = {
    "color_primary": "#f6f60c",
    "color_secondary": "#e45d22",  
}


# Define the menu and page content
root_md = "<|menu|label=Menu|lov={[('KPI',Icon('/images/stocks.png', 'KPI')), ('Activities',Icon('/images/car.png', 'Activities')),('Stores',Icon('/images/store.png', 'Stores')),('Products',Icon('/images/price-tag.png', 'Products'))]}|on_action=on_menu|>"


page1_md = '''
    <|card card-bg |
    Hello to Taipy mr.Hussein
    |>
'''

page2_md = '''
<div class="page-background">
   <h1 class="custom_text">This is page 2</h1>
</div>
'''

page3_md = '''
<div class="page-background">
    <h1 class="custom_text">This is page 3</h1>
</div>
'''

page4_md = '''
<div class="page-background">
    <h1 class="custom_text">This is page 4</h1>
</div>
'''

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

pages = {
    "/": root_md,
    "KPI": page1_md,
    "Activities": page2_md,
    "Stores": page3_md,
    "Products": page4_md
}

# Run the GUI application with the updated stylekit
Gui(pages=pages).run(port=5001,dark_mode=False)