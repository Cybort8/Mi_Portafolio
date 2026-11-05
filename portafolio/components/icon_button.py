import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False, label="") -> rx.Component:
    return rx.link(
        rx.button(
            rx.box(class_name=icon) if icon.startswith("devicon-") else rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
            custom_attrs={"aria-label": label} if label else {},
        ),
        href=url,
        is_external=True
    )
