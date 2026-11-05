import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                rx.flex(
                    *[
                        rx.badge(
                            rx.box(class_name=technology.icon),
                            technology.name,
                            color_scheme="gray"
                        )
                        for technology in info.technologies
                    ],
                    wrap="wrap",
                    spacing=Size.SMALL.value
                ) if info.technologies else rx.fragment(),
                rx.hstack(
                    icon_button("link", info.url, label="Abrir enlace") if info.url else rx.fragment(),
                    icon_button("devicon-github-original", info.github, label="Ver repositorio") if info.github else rx.fragment()
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.image(
            src=info.image,
            alt=info.title,
            height=IMAGE_HEIGHT,
            width="auto",
            border_radius=EmSize.DEFAULT.value,
            object_fit="cover"
        ) if info.image else rx.fragment(),
        rx.vstack(
            rx.badge(info.date) if info.date else rx.fragment(),
            icon_button(
                "shield-check",
                info.certificate,
                solid=True,
                label="Ver certificado"
            ) if info.certificate else rx.fragment(),
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
