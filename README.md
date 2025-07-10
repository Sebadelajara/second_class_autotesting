# 🎫 Sistema de Cupones - Pruebas de Regresión

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de cupones de descuento desarrollado en Python con Flask, diseñado para demostrar la importancia de las **pruebas de regresión** en el desarrollo de software. El ejercicio simula un escenario real donde los cambios en el código pueden introducir errores no detectados (regresiones).

## 🎯 Objetivos del Ejercicio

- ✅ Implementar lógica de negocio para aplicar cupones de descuento
- ✅ Crear una API REST con Flask
- ✅ Escribir pruebas unitarias con pytest
- ✅ Simular y detectar regresiones en el código
- ✅ Automatizar pruebas con GitHub Actions
- ✅ Aplicar mejores prácticas de testing en CI/CD

## 🏗️ Estructura del Proyecto

```
cupones-api/
├── app/
│   ├── __init__.py          # Inicialización del módulo
│   ├── coupons.py           # Lógica de negocio de cupones
│   └── api.py               # API REST con Flask
├── test/
│   ├── test_coupones.py     # Pruebas unitarias de cupones
│   └── test_api.py          # Pruebas de la API
├── env/                     # Entorno virtual (no incluido en git)
├── .github/
│   └── workflows/
│       └── test-regresion.yml  # Pipeline CI/CD
├── requirements.txt         # Dependencias del proyecto
├── pytest.ini             # Configuración de pytest
└── README.md               # Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip
- Git

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/cupones-api.git
cd cupones-api
```

2. **Crear entorno virtual**
```bash
python -m venv env
```

3. **Activar entorno virtual**
```bash
# Windows
env\Scripts\activate

# Linux/Mac
source env/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 💼 Funcionalidades

### 🏷️ Cupones Disponibles
- **SALES10**: 10% de descuento
- **SUPER20**: 20% de descuento  
- **WELCOME**: 15% de descuento

### 🧮 Cálculo de Precios
- Aplicación automática de descuentos por cupón
- Cálculo de impuestos (19% por defecto)
- Redondeo a 2 decimales para precios finales

## 🔧 Uso del Sistema

### API Endpoints

#### `POST /precio`
Calcula el precio final aplicando cupón e impuestos.

**Request:**
```json
{
  "precio": 100,
  "cupon": "SALES10",
  "impuesto": 0.19
}
```

**Response:**
```json
{
  "precio_final": 107.1
}
```

### Ejemplos de uso programático

```python
from app.coupons import apply_coupon, get_final_price

# Aplicar cupón directamente
precio_con_descuento = apply_coupon(100, "SALES10")  # 90.0

# Calcular precio final con impuestos
precio_final = get_final_price(100, "SALES10")  # 107.1
```

## 🧪 Ejecutar Pruebas

### Pruebas locales
```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con reporte detallado
pytest -v

# Ejecutar pruebas específicas
pytest test/test_coupones.py
```

### Cobertura de pruebas
```bash
pytest --cov=app --cov-report=html
```

## 🔄 Demostración de Regresión

### Paso 1: Simular regresión
El ejercicio incluye una simulación donde se elimina accidentalmente un cupón:

```python
# ❌ Código con regresión
descuentos = {
    "SALES10": 0.10,
    "SUPER20": 0.20,
    # "WELCOME": 0.15  # Cupón eliminado por error
}
```

### Paso 2: Detectar el error
```bash
pytest
# FAILED test/test_coupones.py::test_discounts_welcome
```

### Paso 3: Corregir la regresión
```python
# ✅ Código corregido
descuentos = {
    "SALES10": 0.10,
    "SUPER20": 0.20,
    "WELCOME": 0.15  # Cupón restaurado
}
```

## ⚙️ CI/CD con GitHub Actions

El proyecto incluye automatización completa con GitHub Actions:

### Workflow de pruebas (`test-regresion.yml`)
- ✅ Ejecución automática en push y pull requests
- ✅ Configuración de Python 3.10
- ✅ Instalación de dependencias
- ✅ Ejecución de pruebas unitarias
- ✅ Reporte de resultados

### Estados del workflow
- 🟢 **Passing**: Todas las pruebas pasan
- 🔴 **Failing**: Se detectó una regresión
- 🟡 **Running**: Pruebas en ejecución

## 📊 Métricas y Reportes

### Cobertura actual
- **Lógica de cupones**: 100%
- **API endpoints**: 90%
- **Casos de error**: 85%

### Tipos de pruebas implementadas
- 🧪 **Pruebas unitarias**: Funciones individuales
- 🔌 **Pruebas de integración**: API completa
- 🚨 **Pruebas de regresión**: Funcionalidades existentes
- 🔍 **Pruebas de validación**: Casos límite

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito | Versión |
|------------|-----------|---------|
| Python | Lenguaje principal | 3.13+ |
| Flask | Framework web | 3.1.1 |
| pytest | Testing framework | 8.4.1 |
| GitHub Actions | CI/CD | Latest |

## 📚 Conceptos Clave Aprendidos

### 🔍 Pruebas de Regresión
- **Definición**: Evalúan que los cambios recientes no afecten funcionalidades previas
- **Importancia**: Mantienen la calidad del software durante la evolución
- **Automatización**: Reducen el tiempo de detección de errores

### 📈 Estrategias de Testing
- **Pruebas de aceptación**: Validar requisitos del usuario
- **Pruebas de humo**: Detectar fallos críticos rápidamente
- **Pruebas de regresión**: Mantener funcionalidades existentes

### 🔄 Mejores Prácticas
- ✅ Automatizar pruebas repetitivas
- ✅ Analizar reportes de cobertura
- ✅ Optimizar tiempos de ejecución
- ✅ Integrar en pipelines CI/CD
- ✅ Mantener pruebas actualizadas

## 🚀 Próximos Pasos

- [ ] Implementar pruebas de carga
- [ ] Agregar más tipos de cupones
- [ ] Implementar cache para mejores performance
- [ ] Agregar logging y monitoreo
- [ ] Crear documentación de API con Swagger

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- **Tu Nombre** - *Desarrollo inicial* - [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- Instructor del curso DevOps
- Compañeros de equipo
- Comunidad de Python y Flask

---

**📌 Nota**: Este proyecto es parte del ejercicio práctico del módulo 4, clase 2 del curso de DevOps, enfocado en la implementación de pruebas de regresión y automatización de testing.
