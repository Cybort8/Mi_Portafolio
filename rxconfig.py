import os

import reflex as rx

# Vercel expone el dominio de producción en esta variable durante el build.
vercel_url = os.getenv("VERCEL_PROJECT_PRODUCTION_URL")
deploy_url = f"https://{vercel_url}" if vercel_url else "http://localhost:3000"

config = rx.Config(
    app_name="portafolio",
    deploy_url=deploy_url,
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="violet",
                radius="medium"
            )
        ),
        rx.plugins.SitemapPlugin(),
    ],
)
