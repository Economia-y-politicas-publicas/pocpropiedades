# Atajos del proyecto (requiere https://github.com/casey/just)
# Uso: just nueva-propiedad

nueva-propiedad:
    python3 scripts/nueva_propiedad.py

preview:
    quarto preview

render:
    quarto render
