from taipy.gui import Gui, navigate,Icon
import taipy.gui.builder as tgb

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

with tgb.Page() as root_page:
    tgb.menu(label="Menu", 
             lov=[('KPI',Icon('/images/stocks.png', 'KPI')), ('Activities',Icon('/images/car.png', 'Activities')), ('Stores', Icon('/images/store.png', 'Stores')), ('Products',Icon('/images/price-tag.png', 'Products'))], 
             on_action=on_menu)

with tgb.Page() as page_1:
    with tgb.part("card"):
            tgb.text("Retail Play", class_name="h2")
    tgb.navbar(lov=["OVERVIEW","ASSORTMENT","SOS","NPD"])
    with tgb.layout("1 1"):
        with tgb.part("card"):
            tgb.text("Retail Play", class_name="h2")
            tgb.text('Quick description here if you like')
        with tgb.part():
            with tgb.layout("1 1"):
                with tgb.part("card"):
                    tgb.text("Retail Play", class_name="h2")
                    tgb.text('Quick description here if you like')
                with tgb.part("card"):
                    tgb.text("Retail Play", class_name="h2")
                    tgb.text('Quick description here if you like')
            with tgb.layout("1"):
                with tgb.part("card"):
                    tgb.text("Retail Play", class_name="h2")
                    tgb.text('Quick description here if you like')

with tgb.Page() as page_2:
    tgb.text("## This is page 2", mode="md")
with tgb.Page() as page_3:
    tgb.text("# **This** is page 3", mode="md")
with tgb.Page() as page_4:
    tgb.text("## This is page 4", mode="md")
with tgb.Page() as OVERVIEW:
    tgb.text("## This is the overview page", mode="md")
with tgb.Page() as ASSORTMENT:
    tgb.text("## This is the assortment page", mode="md")
with tgb.Page() as SOS:
    tgb.text("## This is the sos page", mode="md")
with tgb.Page() as NPD:
    tgb.text("## This is the npd page", mode="md")

pages = {
    "/": root_page,
    "KPI": page_1,
    "Activities": page_2,
    "Stores": page_3,
    "Products": page_4,
    "OVERVIEW":OVERVIEW,
    "ASSORTMENT":ASSORTMENT,
    "SOS":SOS,
    "NPD":NPD
}
Gui(pages=pages).run(port="5000",dark_mode=False,use_reloader=True)