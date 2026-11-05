import reflex as rx

config = rx.Config(
    app_name="portafolio",
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="grass",
                radius="full"
            )
        ),
        rx.plugins.SitemapPlugin(),
    ],
)
