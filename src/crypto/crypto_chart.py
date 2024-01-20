import os
import plotly.graph_objects as go
from utils.utils import ensure_tmp_folder_exists


class CryptoChart:
    def __init__(self, data, coin_id, currency):
        self.data = data
        self.coin_id = coin_id
        self.currency = currency
        self.tmp_folder = "tmp"

    def _create_chart(self):
        timestamps = self.data.get("timestamps")
        values = self.data.get("values")
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=timestamps, y=values, mode="lines", name=self.coin_id)
        )
        fig.update_layout(
            title=f"{self.coin_id.capitalize()} Price Chart",
            xaxis_title="Time",
            yaxis_title=f"Price ({self.currency.upper()})",
            xaxis=dict(showline=True, showgrid=False),
            yaxis=dict(showline=True, showgrid=False),
        )
        return fig

    def _save_chart_as_image(self, filename):
        fig = self._create_chart()
        ensure_tmp_folder_exists()
        file_path = os.path.join(self.tmp_folder, filename)
        fig.write_image(file_path)
        print(f"Chart saved as {file_path}")
