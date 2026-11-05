import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(name: str, data: Media) -> rx.Component:
    return rx.vstack(
        rx.text(name),
        media(data),
        spacing=Size.SMALL.value
    )
