#!/usr/bin/env python3
"""
nueva_propiedad.py — crea la carpeta y el index.qmd de una propiedad nueva.

Uso:
    python3 scripts/nueva_propiedad.py
    (te va preguntando los datos uno por uno)
"""
from pathlib import Path
from datetime import date
import re

ROOT = Path(__file__).resolve().parent.parent


def slugify(texto):
    texto = texto.lower().strip()
    texto = re.sub(r"[áàä]", "a", texto)
    texto = re.sub(r"[éèë]", "e", texto)
    texto = re.sub(r"[íìï]", "i", texto)
    texto = re.sub(r"[óòö]", "o", texto)
    texto = re.sub(r"[úùü]", "u", texto)
    texto = re.sub(r"ñ", "n", texto)
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    return texto.strip("-")


def main():
    print("Nueva propiedad — completá los datos:\n")
    titulo = input("Título (ej: Departamento en Ñuñoa): ")
    direccion = input("Dirección: ")
    comuna = input("Comuna: ")
    operacion = input("Operación (Arriendo/Venta): ")
    precio = input("Precio (ej: $500.000 CLP/mes): ")
    m2 = input("Superficie m²: ")
    dormitorios = input("Dormitorios: ")
    banos = input("Baños: ")
    estacionamientos = input("Estacionamientos: ")
    estado = input("Estado (Disponible/Reservado/Vendido/Arrendado): ")
    descripcion = input("Descripción breve: ")

    slug = slugify(titulo)
    carpeta = ROOT / "propiedades" / slug
    (carpeta / "fotos").mkdir(parents=True, exist_ok=True)

    contenido = f"""---
title: "{titulo}"
subtitle: "{direccion} · {comuna}"
date: {date.today().isoformat()}
image: fotos/foto1.jpg
categories: [{estado}, {operacion}, {comuna}]
description: "{descripcion}"
---

::: {{.gallery}}
![](fotos/foto1.jpg)
:::

::: {{.spec-sheet}}
**Operación**\\
{operacion}

**Precio**\\
{precio}

**Superficie**\\
{m2} m²

**Dormitorios**\\
{dormitorios}

**Baños**\\
{banos}

**Estacionamientos**\\
{estacionamientos}

**Estado**\\
{estado}
:::

{descripcion}

[&larr; Volver al listado](../../index.html)
"""
    (carpeta / "index.qmd").write_text(contenido, encoding="utf-8")

    print(f"\n✅ Creado propiedades/{slug}/")
    print(f"   Agregá las fotos reales en propiedades/{slug}/fotos/")
    print("   (foto1.jpg es la que se usa como portada en el listado)")


if __name__ == "__main__":
    main()
