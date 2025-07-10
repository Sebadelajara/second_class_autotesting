# 🎫 Sistema de Cupones - Pruebas de Regresión Automatizadas

[![Tests](https://github.com/Sebadelajara/second_class_autotesting/actions/workflows/python-app.yml/badge.svg)](https://github.com/Sebadelajara/second_class_autotesting/actions/workflows/python-app.yml)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/Sebadelajara/second_class_autotesting)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.1.1-orange.svg)](https://flask.palletsprojects.com/)

## 📋 Descripción del Proyecto

Este repositorio implementa un **sistema completo de cupones de descuento** desarrollado en Python con Flask, diseñado específicamente para demostrar la importancia de las **pruebas de regresión automatizadas** en el desarrollo de software moderno. El proyecto simula escenarios reales donde cambios en el código pueden introducir errores no detectados (regresiones) y cómo la automatización de pruebas puede prevenirlos.

### 🎯 **¿Por qué este proyecto?**
- Demuestra conceptos clave de **testing automatizado**
- Implementa **CI/CD con GitHub Actions**
- Alcanza **100% de cobertura de código**
- Utiliza **mejores prácticas de desarrollo**
- Simula **casos reales de regresión**

## 🏗️ Arquitectura del Sistema

```
cupones-api/
├── 📁 app/                          # Aplicación principal
│   ├── __init__.py                  # Inicialización del módulo
│   ├── coupons.py                   # 🎫 Lógica de negocio de cupones
│   └── api.py                       # 🌐 API REST con Flask
├── 📁 tests/                        # Suite de pruebas
│   ├── test_coupones.py             # 🧪 Pruebas unitarias de cupones (5 tests)
│   └── test_api.py                  # 🔌 Pruebas de API REST (7 tests)
├── 📁 .github/workflows/            # Automatización CI/CD
│   └── python-app.yml               # 🚀 Pipeline de GitHub Actions
├── 📁 env/                          # Entorno virtual (gitignored)
├── requirements.txt                 # 📦 Dependencias (21 packages)
├── pytest.ini                      # ⚙️ Configuración de pytest
├── .gitignore                       # 🚫 Archivos ignorados (93 líneas)
├── .coverage                        # 📊 Base de datos de cobertura
└── README.md                        # 📖 Esta documentación
```

## 🎯 Objetivos Pedagógicos Alcanzados

- ✅ **Lógica de negocio robusta**: Sistema de cupones con validaciones
- ✅ **API REST funcional**: Endpoint POST `/precio` con manejo de errores
- ✅ **Suite de pruebas completa**: 12 tests unitarios + integración
- ✅ **Cobertura 100%**: Todas las líneas de código probadas
- ✅ **CI/CD automatizado**: Pipeline con GitHub Actions
- ✅ **Detección de regresiones**: Simulación y corrección de errores
- ✅ **Mejores prácticas**: Estructura, documentación y código limpio

## 💼 Funcionalidades del Sistema

### 🏷️ **Cupones Implementados**
| Código | Descuento | Uso Típico |
|--------|-----------|------------|
| `SALES10` | 10% | Ventas generales |
| `SUPER20` | 20% | Ofertas especiales |
| `WELCOME` | 15% | Nuevos clientes |

### 🧮 **Motor de Cálculo**
- ✅ **Aplicación de descuentos** por código de cupón
- ✅ **Cálculo de impuestos** (19% por defecto, personalizable)
- ✅ **Redondeo a 2 decimales** para montos finales
- ✅ **Validación de cupones** inválidos
- ✅ **Manejo de casos edge** (precio 0, impuestos personalizados)

## 🔧 API REST Endpoints

### `POST /precio`
Calcula el precio final aplicando cupón de descuento e impuestos.

**Request Example:**
```bash
curl -X POST http://localhost:5000/precio \
  -H "Content-Type: application/json" \
  -d '{
    "price": 100,
    "coupon": "SALES10",
    "tax_rate": 0.19
  }'
```

**Response Example:**
```json
{
  "final_price": 107.1
}
```

**Parámetros:**
- `price` (number): Precio base del producto
- `coupon` (string): Código del cupón de descuento
- `tax_rate` (number, opcional): Tasa de impuesto (default: 0.19)

## 🚀 Guía de Instalación y Ejecución

### **Prerrequisitos**
- Python 3.10+ 
- pip (package manager)
- Git

### **Instalación Paso a Paso**

1. **Clonar el repositorio**
```bash
git clone https://github.com/Sebadelajara/second_class_autotesting.git
cd second_class_autotesting
```

2. **Crear y activar entorno virtual**
```bash
# Crear entorno virtual
python -m venv env

# Activar entorno virtual
# Windows:
env\Scripts\activate
# Linux/Mac:
source env/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Verificar instalación**
```bash
# Ejecutar pruebas
pytest --cov=app --cov-report=term tests/

# Resultado esperado: 12 passed, 100% coverage
```

### **Ejecutar la Aplicación**
```bash
# Modo desarrollo
python -m flask --app app.api run --debug

# Modo producción
python -m flask --app app.api run --host=0.0.0.0 --port=5000
```

## 🧪 Suite de Pruebas Completa

### **Estadísticas Actuales**
- 📊 **12 pruebas totales** (5 unitarias + 7 integración)
- 📈 **100% cobertura** de código
- ⚡ **Tiempo ejecución**: ~0.5 segundos
- 🔍 **0 fallos** detectados

### **Ejecutar Pruebas**

```bash
# Ejecutar todas las pruebas
pytest

# Pruebas con cobertura detallada  
pytest --cov=app --cov-report=term-missing tests/

# Generar reporte HTML interactivo
pytest --cov=app --cov-report=html tests/
# Abrir: htmlcov/index.html

# Ejecutar pruebas específicas
pytest tests/test_coupones.py::test_discounts_sales10 -v
```

### **Casos de Prueba Implementados**

#### **Pruebas Unitarias (test_coupones.py)**
1. ✅ `test_discounts_sales10` - Cupón SALES10 (10%)
2. ✅ `test_discounts_super20` - Cupón SUPER20 (20%)  
3. ✅ `test_discounts_welcome` - Cupón WELCOME (15%)
4. ✅ `test_invalid_coupon` - Cupón inválido
5. ✅ `test_final_price_with_tax` - Precio final con impuestos

#### **Pruebas de Integración (test_api.py)**
1. ✅ `test_calcular_precio_endpoint_sales10` - API con SALES10
2. ✅ `test_calcular_precio_endpoint_super20` - API con SUPER20
3. ✅ `test_calcular_precio_endpoint_welcome` - API con WELCOME
4. ✅ `test_precio_sin_cupon_valido` - API con cupón inválido
5. ✅ `test_precio_con_impuesto_personalizado` - API con tax customizado
6. ✅ `test_precio_sin_impuesto_especificado` - API con tax por defecto
7. ✅ `test_precio_cero` - API con precio 0

## 🔄 Demostración de Pruebas de Regresión

### **Scenario: Eliminación Accidental de Cupón**

**1. Estado inicial (funcional)**
```python
# app/coupons.py
discounts = {
    "SALES10": 0.10,
    "SUPER20": 0.20,
    "WELCOME": 0.15  # ✅ Cupón presente
}
```

**2. Introducir regresión**
```python
# app/coupons.py - Error accidental
discounts = {
    "SALES10": 0.10,
    "SUPER20": 0.20,
    # "WELCOME": 0.15  # ❌ Comentado por error
}
```

**3. Detectar automáticamente**
```bash
pytest tests/
# FAILED tests/test_coupones.py::test_discounts_welcome - AssertionError
# FAILED tests/test_api.py::test_calcular_precio_endpoint_welcome - AssertionError
```

**4. Corregir y verificar**
```python
# Restaurar cupón
"WELCOME": 0.15,

# Verificar corrección
pytest tests/
# ✅ 12 passed in 0.49s
```

## ⚙️ CI/CD con GitHub Actions

### **Pipeline Automatizado**
- 🚀 **Trigger**: Push/PR a rama `main`
- 🐍 **Entorno**: Ubuntu + Python 3.10
- 🔍 **Linting**: flake8 para calidad de código
- 🧪 **Testing**: pytest con cobertura
- 📊 **Artifacts**: Reportes HTML descargables

### **Configuración del Workflow**

```yaml
name: 🧪 Coupon API - Regression Tests

on:
  push: { branches: [main] }
  pull_request: { branches: [main] }

jobs:
  test:
    name: ✅ Run Tests and Coverage
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout Repository
      - name: 🐍 Set up Python 3.10  
      - name: 📦 Install Dependencies
      - name: 🔍 Lint with flake8
      - name: 🧪 Test with pytest and coverage
      - name: 📤 Upload Coverage Report
```

### **Estados del Pipeline**
- 🟢 **Success**: Todas las pruebas pasan (objetivo actual)
- 🔴 **Failed**: Regresión detectada
- 🟡 **Running**: Pipeline en ejecución

## 📊 Métricas de Calidad

### **Cobertura de Código (100%)**
```
Name              Stmts   Miss  Cover
-------------------------------------
app/__init__.py       0      0   100%
app/api.py           13      0   100%
app/coupons.py        8      0   100%
-------------------------------------
TOTAL                21      0   100%
```

### **Distribución de Pruebas**
- 🧪 **41.7%** Pruebas unitarias (5/12)
- 🔌 **58.3%** Pruebas de integración (7/12)
- 🚨 **100%** Cobertura de regresión
- 🔍 **100%** Validación de casos edge

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión | Propósito |
|------------|------------|---------|-----------|
| **Backend** | Python | 3.13+ | Lenguaje principal |
| **Web Framework** | Flask | 3.1.1 | API REST |
| **Testing** | pytest | 8.4.1 | Framework de pruebas |
| **Coverage** | pytest-cov | 6.2.1 | Análisis de cobertura |
| **Linting** | flake8 | Latest | Calidad de código |
| **CI/CD** | GitHub Actions | Latest | Automatización |
| **Package Manager** | pip | Latest | Gestión dependencias |

### **Dependencias Completas (requirements.txt)**
```
Flask==3.1.1          # Web framework
pytest==8.4.1         # Testing framework  
pytest-cov==6.2.1     # Coverage analysis
coverage==7.9.2       # Coverage core
requests==2.32.4      # HTTP client (testing)
+ 16 dependencias adicionales
```

## 📚 Conceptos DevOps Demostrados

### **🔍 Testing Strategies**
- **Unit Testing**: Funciones individuales aisladas
- **Integration Testing**: API endpoints completos
- **Regression Testing**: Prevención de errores pasados
- **Edge Case Testing**: Validación de límites

### **📈 Quality Assurance**
- **Code Coverage**: 100% líneas ejecutadas
- **Linting**: Estándares de código Python (PEP8)
- **Automated Testing**: Ejecución automática en CI/CD
- **Documentation**: README completo y mantenido

### **🔄 CI/CD Best Practices**
- **Continuous Integration**: Tests en cada commit
- **Automated Deployment**: Pipeline declarativo
- **Artifact Management**: Reportes descargables
- **Branch Protection**: Requerimiento de tests passing

## 🎓 Aprendizajes Clave

### **1. Importancia de las Pruebas de Regresión**
> Las pruebas automatizadas detectaron la eliminación accidental del cupón WELCOME en 0.49 segundos, evitando que llegara a producción.

### **2. Valor del 100% de Cobertura**
> Cada línea de código está probada, garantizando que cualquier cambio sea validado automáticamente.

### **3. CI/CD como Safety Net**
> El pipeline de GitHub Actions actúa como una red de seguridad, ejecutando 12 pruebas en cada cambio de código.

### **4. Diseño Testeable**
> La separación entre lógica de negocio (coupons.py) y API (api.py) facilitó la creación de pruebas independientes.

## 🚀 Próximas Mejoras

- [ ] **Load Testing**: Pruebas de rendimiento con múltiples usuarios
- [ ] **API Documentation**: Swagger/OpenAPI para documentación interactiva
- [ ] **Database Integration**: Persistencia de cupones y transacciones
- [ ] **Authentication**: Sistema de usuarios y autenticación
- [ ] **Monitoring**: Métricas de uso y alertas
- [ ] **Containerization**: Docker para deployment consistente

## 🤝 Contribución

Este proyecto está abierto a contribuciones. Por favor:

1. **Fork** el repositorio
2. **Crea una rama** para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Escribe pruebas** para tu código nuevo
4. **Asegúrate** de mantener 100% cobertura
5. **Commit** tus cambios (`git commit -m 'Add: nueva funcionalidad'`)
6. **Push** a tu rama (`git push origin feature/nueva-funcionalidad`)
7. **Abre un Pull Request**

### **Estándares de Contribución**
- ✅ Todas las pruebas deben pasar
- ✅ Cobertura debe mantenerse en 100%
- ✅ Código debe pasar linting (flake8)
- ✅ Documentación debe actualizarse

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver archivo [LICENSE](LICENSE) para más detalles.

## 👥 Equipo

- **Sebastian de la Jara** - *Desarrollo e Implementación* - [@Sebadelajara](https://github.com/Sebadelajara)

## 🙏 Agradecimientos

- **Instructor DevOps**: Por la metodología de pruebas de regresión
- **Compañeros de curso**: Por feedback y colaboración
- **Comunidad Python**: Por las excelentes herramientas y documentación
- **GitHub**: Por la plataforma de CI/CD gratuita

---

## 📌 Nota Académica

Este proyecto forma parte del **ejercicio práctico del Módulo 4, Clase 2** del curso de DevOps, con enfoque específico en:

- ✅ **Implementación de pruebas de regresión**
- ✅ **Automatización de testing con CI/CD**
- ✅ **Aplicación de mejores prácticas de desarrollo**
- ✅ **Demostración de detección y corrección de regresiones**

**Objetivo cumplido**: Crear un sistema completo que demuestre cómo las pruebas automatizadas previenen regresiones en software real.

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
