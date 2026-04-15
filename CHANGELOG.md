# 📜 Diario de Cambios - Al-Andalus Meta-Agent

Este archivo registra la evolución del proyecto y permite la trazabilidad de las decisiones de diseño y arquitectura.

## [2026-04-15] - Versión Inicial (Estructura de Control)

### 🚀 Añadido
- **Interfaz Base (v1):** Creación del `index.html` con diseño glassmorphism, selector de siglos y categorías.
- **Sistema de Backups:** Creación de la carpeta `_backups` para control de versiones manual.
- **Identificación de Recursos:** Mapeo inicial de los 40 cuadernos de NotebookLM (Siglo X al XIX).

### 🛠️ Arquitectura
- Se ha definido el uso del servidor MCP de NotebookLM para consultas aisladas por siglo/categoría.
- Se ha establecido `index.html` como el "Archivo Madre" en el workspace local.

### 📝 Próximos Pasos
1. Implementar buscador de lenguaje natural.
2. Integrar llamadas reales al servidor MCP desde la interfaz.
3. Evaluar despliegue en la nube para enlace compartible (GitHub Pages).
