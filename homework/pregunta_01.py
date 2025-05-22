# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo files//shipping-data.csv contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * Warehouse_block

    * Mode_of_Shipment

    * Customer_rating

    * Weight_in_gms

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta data.

    * Todos los archivos debe ser creados en la carpeta docs.

    * Su código debe crear la carpeta docs si no existe.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path

    docs_path = Path("docs")
    docs_path.mkdir(exist_ok=True)

    def load_data():
        return pd.read_csv("files/input/shipping-data.csv")

    def create_visual_for_shipping_per_warehouse(df):
        plt.figure()
        df["Warehouse_block"].value_counts().plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse Block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig(docs_path / "shipping_per_warehouse.png")

    def create_visual_for_mode_of_shipment(df):
        plt.figure()
        df["Mode_of_Shipment"].value_counts().plot.pie(
            title="Mode of Shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.savefig(docs_path / "mode_of_shipment.png")

    def create_visual_for_average_customer_rating(df):
        plt.figure()
        grouped = df[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe()
        grouped.columns = grouped.columns.droplevel()
        grouped = grouped[["mean", "min", "max"]]
        plt.barh(
            y=grouped.index,
            width=grouped["max"] - 1,
            left=grouped["min"],
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colors = ["tab:green" if v >= 3.0 else "tab:orange" for v in grouped["mean"]]
        plt.barh(
            y=grouped.index,
            width=grouped["mean"] - 1,
            left=grouped["min"],
            color=colors,
            height=0.5,
            alpha=1.0,
        )
        plt.title("Average Customer Rating")
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig(docs_path / "average_customer_rating.png")

    def create_visual_for_weight_distribution(df):
        plt.figure()
        df["Weight_in_gms"].plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig(docs_path / "weight_distribution.png")

    def generate_html():
        html_content = """
        <!DOCTYPE html>
        <html>
            <body>
                <h1>Shipping Dashboard Example</h1>
                <div style="width:45%;float:left">
                    <img src="shipping_per_warehouse.png" alt="Fig 1">
                    <img src="mode_of_shipment.png" alt="Fig 2">
                </div>
                <div style="width:45%;float:left">
                    <img src="average_customer_rating.png" alt="Fig 3">
                    <img src="weight_distribution.png" alt="Fig 4">
                </div>
            </body>
        </html>
        """
        with open(docs_path / "index.html", "w", encoding="utf-8") as f:
            f.write(html_content)

    df = load_data()
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)
    generate_html()

if __name__ == "__main__":
    pregunta_01()


