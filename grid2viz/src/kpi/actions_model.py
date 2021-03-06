import pandas as pd
import plotly.graph_objects as go

from grid2viz.src.utils.graph_utils import layout_no_data, layout_def


def get_action_per_line(new_episode):
    data = get_action_table_data(new_episode)
    # Below to flatten the series of lists "lines_modified"
    try:
        s = data[(data["action_line"] > 0)]["lines_modified"].apply(pd.Series).stack()
        count = s.value_counts()
    except (IndexError, AttributeError):
        count = pd.Series()
    return [go.Bar(x=count.index, y=count.values)]


def get_action_table_data(new_episode):
    return new_episode.action_data_table


def get_action_per_sub(new_episode):
    data = get_action_table_data(new_episode)
    # Below to flatten the series of lists "subs_modified"
    try:
        s = data[(data["action_subs"] > 0)]["subs_modified"].apply(pd.Series).stack()
        count = s.value_counts()
    except (IndexError, AttributeError):
        count = pd.Series()
    return [go.Bar(x=count.index, y=count.values)]


def update_layout(predicate, msg):
    if predicate:
        figure_layout = layout_no_data(msg)
    else:
        figure_layout = layout_def

    return figure_layout


def get_actions_sum(new_episode):
    return new_episode.action_data_table.set_index("timestamp")[[
        'action_line', 'action_subs'
    ]].sum(axis=1).to_frame(name="Nb Actions")
