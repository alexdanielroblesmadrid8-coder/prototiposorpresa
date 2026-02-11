# 🎁 PROTOTIPO - SORPRESA DE 2 MESES

Este es el prototipo funcional de tu proyecto. Aquí todo está configurado con datos de PRUEBA.

## 📁 ESTRUCTURA DEL PROYECTO

```
prototipo_sorpresa/
│
├── app.py                 # Aplicación principal Flask
├── data/                  # Carpeta donde se guarda el progreso
│   └── progreso.json      # (se crea automáticamente)
├── templates/             # Páginas HTML
│   ├── index.html
│   ├── fase1.html
│   ├── fase2.html
│   ├── fase3.html
│   ├── bloqueado.html
│   └── final.html
└── static/                # Archivos CSS
    └── style.css
```

## 🚀 CÓMO EJECUTAR EL PROTOTIPO

### Paso 1: Instalar Flask
```bash
pip install flask
```

### Paso 2: Ejecutar la aplicación
```bash
cd prototipo_sorpresa
python app.py
```

### Paso 3: Abrir en el navegador
Abre tu navegador y ve a: **http://localhost:5000**

## 🎮 CÓMO PROBAR EL SISTEMA

### DATOS DE PRUEBA CONFIGURADOS:

**Fase 1:**
- Pregunta: "¿Dónde fue nuestra primera cita?"
- Respuesta válida: Cualquier palabra que contenga: `cafe`, `café`, `coffee`, `starbucks`, `cappuccino`
- Ejemplo: Puedes escribir "en un café" o simplemente "café"

**Fase 2:**
- Pregunta: "¿Qué nos gusta hacer en nuestras noches tranquilas?"
- Respuesta válida: `pelicula`, `película`, `netflix`, `cine`, `movie`
- Ejemplo: "ver películas" o "netflix"

**Fase 3:**
- Pregunta: "¿Qué es lo que más esperas de nosotros?"
- Respuesta válida: `siempre`, `forever`, `juntos`, `amor`, `futuro`
- Ejemplo: "estar juntos siempre"
- ⚠️ NOTA: La Fase 3 está configurada para desbloquearse MAÑANA (para probar el bloqueo)

## 📅 CONFIGURACIÓN DE FECHAS (EN app.py)

```python
HOY = date.today()
FASE_1_DATE = HOY            # Disponible HOY
FASE_2_DATE = HOY            # Disponible HOY  
FASE_3_DATE = HOY + timedelta(days=1)  # Disponible MAÑANA
```

### Para desbloquear TODAS las fases inmediatamente:
Cambia en `app.py` la línea:
```python
FASE_3_DATE = HOY + timedelta(days=1)
```
Por:
```python
FASE_3_DATE = HOY
```

## 🎯 FLUJO DEL SISTEMA

1. **Página Principal (index.html)**
   - Muestra el estado de cada fase (bloqueada/desbloqueada/completada)
   - Tiene botones para acceder a cada fase

2. **Fase 1, 2, 3**
   - Si la fase está bloqueada → Muestra "bloqueado.html"
   - Si está desbloqueada → Muestra la pregunta
   - Al responder correctamente → Marca como completada y regresa al inicio

3. **Página Final**
   - Se muestra SOLO al completar la Fase 3
   - Mensaje final con animaciones

## 💾 SISTEMA DE PROGRESO

El progreso se guarda automáticamente en `data/progreso.json`:
```json
{
    "fase1": false,
    "fase2": false,
    "fase3": false
}
```

Cuando completas una fase, cambia a `true`.

### Para RESETEAR el progreso:
Elimina el archivo `data/progreso.json` o cambia todos los valores a `false`.

## 🎨 CARACTERÍSTICAS IMPLEMENTADAS

✅ Sistema de fechas de desbloqueo
✅ Validación flexible de respuestas (acepta variaciones)
✅ Guardado automático de progreso
✅ Animaciones CSS suaves
✅ Diseño responsive
✅ Mensajes de error personalizados por fase
✅ Página de bloqueo elegante
✅ Página final mejorada con animaciones

## 📝 NOTAS IMPORTANTES

1. **Datos de Prueba:** Este prototipo usa preguntas y respuestas genéricas
2. **Para tu versión final:** Cambia las preguntas, respuestas y fechas reales
3. **Personalización:** Puedes cambiar colores, textos, emojis en los archivos HTML/CSS
4. **Hosting:** Para publicarlo online, necesitarás un servicio como Render, Railway, o PythonAnywhere

## 🔧 PRÓXIMOS PASOS

1. ✅ Probar este prototipo completamente
2. 📝 Anotar qué quieres cambiar o mejorar
3. 💕 Personalizar con tus datos reales
4. 🎁 Agregar el "regalo final" especial
5. 🌐 Desplegarlo online antes de la fecha

---

**Creado con ❤️ para sorprender a alguien especial**
