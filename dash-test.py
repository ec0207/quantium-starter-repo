from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

from dash_app import update_graph, app

def test_update_graph():
    regions = ["north", "south", "west", "east", "ALL"]
    for region in regions:
        fig = update_graph(region)
        assert fig is not None
        if region != "ALL":
            assert len(fig.data) == 1
        else: 
            assert len(fig.data) > 1

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.wait_for_element("h1")
    assert header.text == "Pink Morsel Sales"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    region_picker = dash_duo.find_element("#region-radio")
    assert region_picker is not None