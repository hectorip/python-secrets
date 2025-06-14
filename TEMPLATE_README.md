# 🎯 Template de Presentación Reveal.js

Este template está basado en el estilo y estructura de la presentación "Secretos de Python" y te permite crear presentaciones profesionales y atractivas usando Reveal.js.

## 🚀 Inicio Rápido

1. **Copia el archivo template**: `reveal-template.html`
2. **Personaliza el contenido**: Edita los placeholders con tu información
3. **Abre en el navegador**: Directamente o sirve con un servidor local

```bash
# Servidor simple con Python
python -m http.server 8000
# Luego ve a http://localhost:8000/reveal-template.html
```

## 📋 Estructura del Template

### Secciones Incluidas

- **🎯 Slide de Título**: Portada principal con título y subtítulo
- **📋 Agenda**: Lista de temas con emojis
- **🔧 Secciones Principales**: Con introducción y subsecciones
- **💡 Slides de Código**: Con highlighting de sintaxis
- **⚖️ Comparaciones**: Lado a lado (antes/después)
- **📊 Tablas**: Para datos estructurados
- **💎 Mejores Prácticas**: Do's and Don'ts
- **🎯 Casos de Uso**: Ejemplos prácticos
- **🏁 Conclusión**: Resumen y próximos pasos

### Tipos de Contenido

#### 1. Código con Sintaxis Highlighting
```html
<pre><code class="python" data-trim>
def ejemplo():
    return "Hola mundo"
</code></pre>
```

**Lenguajes soportados**: `python`, `javascript`, `bash`, `html`, `css`, `json`, `yaml`, etc.

#### 2. Fragmentos Animados
```html
<ul>
    <li class="fragment">Aparece primero</li>
    <li class="fragment">Aparece segundo</li>
    <li class="fragment">Aparece tercero</li>
</ul>
```

#### 3. Comparaciones Lado a Lado
```html
<div style="display: flex; justify-content: space-between;">
    <div style="width: 45%;">
        <h4>❌ Antes</h4>
        <!-- Contenido -->
    </div>
    <div style="width: 45%;">
        <h4>✅ Después</h4>
        <!-- Contenido -->
    </div>
</div>
```

## 🎨 Personalización

### Cambiar Tema
```html
<!-- En el CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/theme/TEMA.css">
```

**Temas disponibles**:
- `moon` (actual) - Oscuro con fondo lunar
- `black` - Negro elegante
- `white` - Blanco limpio
- `league` - Gris con acentos
- `sky` - Azul cielo
- `night` - Oscuro con azul
- `serif` - Con fuentes serif
- `simple` - Minimalista
- `solarized` - Colores solarized

### Colores y Estilos Personalizados
```html
<style>
.reveal .slides section {
    /* Estilos personalizados */
}
</style>
```

### Configuración de Reveal.js
```javascript
Reveal.initialize({
    // Transiciones
    transition: 'slide', // none/fade/slide/convex/concave/zoom
    
    // Controles
    controls: true,
    progress: true,
    
    // Auto-slide (en ms, 0 = desactivado)
    autoSlide: 0,
    
    // Tema
    theme: 'moon'
});
```

## 🎯 Tips de Diseño

### ✅ Mejores Prácticas

1. **Una idea por slide**: Mantén el foco
2. **Usa emojis consistentemente**: Para categorizar y hacer visual
3. **Código legible**: Con comentarios explicativos
4. **Fragmentos estratégicos**: Para revelar información gradualmente
5. **Colores coherentes**: Stick to the theme

### 📱 Responsividad

El template funciona en:
- 💻 Desktop
- 📱 Móvil
- 📺 Proyectores
- 🖥️ Pantallas grandes

### 🎮 Controles de Navegación

| Tecla | Acción |
|-------|--------|
| `→` `↓` `Space` | Siguiente slide |
| `←` `↑` | Slide anterior |
| `Esc` | Vista general |
| `S` | Notas del presentador |
| `F` | Pantalla completa |
| `O` | Pausa (negro) |
| `B` | Pausa (blanco) |

## 🛠️ Funcionalidades Avanzadas

### Notas del Presentador
```html
<section>
    <h2>Mi Slide</h2>
    <p>Contenido visible</p>
    <aside class="notes">
        Estas notas solo las veo yo al presionar 'S'
    </aside>
</section>
```

### Fondos Personalizados
```html
<section data-background="#ff0000">
    <!-- Fondo rojo -->
</section>

<section data-background="url('imagen.jpg')">
    <!-- Fondo con imagen -->
</section>

<section data-background-video="video.mp4">
    <!-- Fondo con video -->
</section>
```

### Auto-Animaciones
```html
<section data-auto-animate>
    <h1>Título</h1>
</section>
<section data-auto-animate>
    <h1 style="color: red;">Título</h1>
    <p>Nuevo contenido</p>
</section>
```

## 🔧 Personalización del Template

### 1. Información Básica
```html
<!-- Cambiar título -->
<title>Tu Título Aquí</title>

<!-- Slide principal -->
<h1>🎯 Tu Título</h1>
<h3>Tu Subtítulo</h3>
```

### 2. Agenda
```html
<section>
    <h2>Agenda</h2>
    <ul>
        <li>📋 Tu Tema 1</li>
        <li>🔧 Tu Tema 2</li>
        <!-- Añadir más temas -->
    </ul>
</section>
```

### 3. Secciones
```html
<!-- Para cada tema principal -->
<section>
    <section>
        <h2>🔧 Título de Sección</h2>
        <p>Descripción</p>
    </section>
    
    <!-- Subsecciones -->
    <section>
        <h3>Concepto Específico</h3>
        <!-- Contenido -->
    </section>
</section>
```

## 📦 Archivos Necesarios

- `reveal-template.html` - Template principal
- Conexión a internet (para CDN de Reveal.js)
- Navegador moderno

## 🌐 Recursos Adicionales

- [Reveal.js Documentación](https://revealjs.com/)
- [Temas Oficiales](https://revealjs.com/themes/)
- [Plugins](https://revealjs.com/plugins/)
- [Configuración Avanzada](https://revealjs.com/config/)

## 🐛 Solución de Problemas

### El código no se ve bien
- Verifica que uses `data-trim` en `<pre><code>`
- Asegúrate de que el lenguaje esté especificado correctamente

### Los estilos no cargan
- Verifica conexión a internet (CDN)
- Revisa la consola del navegador por errores

### Las transiciones no funcionan
- Verifica que Reveal.js se haya inicializado correctamente
- Revisa la consola por errores de JavaScript

## 📄 Licencia

Este template está basado en Reveal.js (MIT License) y es de uso libre.

---

¡Disfruta creando presentaciones increíbles! 🎉