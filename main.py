import pandas as pd
import plotly.express as px


def draw_part_assignment_horizontal_stacked_bar_chart(df):
    long_df = px.data.medals_long()

    # fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
    fig = px.bar(df, x="size", y="part", color="item", orientation='h', text="item")
    fig.update_traces(textfont_size=24, textposition=['inside'],
                      insidetextanchor="middle")  # , 'bottom center'])
    # レイアウトを設定する
    fig.update_layout(
        title='Part Assignment Chart',
        xaxis_title='Size',
        yaxis_title='Part',
    )
    fig.show()


if __name__ == '__main__':
    # df = pd.read_csv('item_part_def2.csv')
    df = pd.read_csv('myFile0.csv')
    draw_part_assignment_horizontal_stacked_bar_chart(df)
