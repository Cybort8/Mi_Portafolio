# Portafolio de Keneth Rojas

Portafolio personal de **Keneth Jassir Rojas Díaz**, ingeniero de sistemas y desarrollador de software.

🚀 **[Visita el portafolio en producción](https://portafolio-keneth-rojas.vercel.app/)**

Sitio estático generado con [Python](https://python.org) y [Reflex](https://reflex.dev).

## Requisitos

- Python 3.11 o superior

## Desarrollo local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
reflex run
```

El sitio queda disponible en [http://localhost:3000](http://localhost:3000).

## Contenido

Toda la información del portafolio vive en [`assets/data/data.json`](assets/data/data.json): datos personales, contacto, tecnologías, experiencia, proyectos y formación. Las imágenes y el CV están en `assets/`.

- Iconos generales: [Lucide](https://lucide.dev/icons/).
- Iconos de tecnologías: [Devicon](https://devicon.dev/).
- Un elemento es opcional cuando su campo es `""` o una lista vacía; la sección se omite.

## Build y despliegue

```bash
bash build.sh
```

Genera el sitio estático en `public/`. El proyecto está configurado para desplegarse en [Vercel](https://vercel.com) mediante `vercel.json` y `build.sh`.

El dominio de producción se toma automáticamente de `VERCEL_PROJECT_PRODUCTION_URL` y se usa para el `og:image` y el `sitemap.xml`. Para forzarlo manualmente, define `REFLEX_DEPLOY_URL`.

## Créditos

Basado en [portafolio-template](https://github.com/mouredev/portafolio-template) de Brais Moure, bajo licencia Apache 2.0 (ver [`LICENSE`](LICENSE)).
