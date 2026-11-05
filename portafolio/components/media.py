import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True,
            "Enviar correo"
        ),
        rx.hstack(
            icon_button(
                "file-text",
                data.cv,
                label="Ver hoja de vida"
            ),
            icon_button(
                "devicon-github-original",
                data.github,
                label="GitHub"
            ),
            icon_button(
                "devicon-linkedin-plain",
                data.likedin,
                label="LinkedIn"
            ),
            icon_button(
                "message-circle",
                f"https://wa.me/{data.phone.replace(' ', '').replace('+', '')}",
                label="WhatsApp"
            ) if data.phone else rx.fragment(),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )
