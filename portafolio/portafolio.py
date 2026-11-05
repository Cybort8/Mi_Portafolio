import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack

DATA = data.data


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            info("Formación", DATA.training),
            extra(DATA.extras) if DATA.extras else rx.fragment(),
            rx.divider(),
            footer(DATA.name, DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
)
# Sitio estático sin backend: evita el toast de "Cannot connect to server".
app.app_wraps.pop((5, "Overlay"), None)

title = DATA.title
description = DATA.description
image = f"{rx.config.get_config().deploy_url.rstrip('/')}{DATA.image}"

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description}
    ]
)
