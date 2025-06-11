# 🛠️ Proyecto de CI/CD para Ingeniería de Software

Este repositorio tiene como objetivo implementar un entorno completo de **Integración Continua (CI)** y **Despliegue Continuo (CD)** para una API desarrollada en Python con FastAPI. El proyecto fue desarrollado como práctica de la cátedra **Ingeniería de Software**, integrando herramientas modernas utilizadas en la industria.

---

## 🎯 Objetivo

Diseñar un flujo automatizado que permita:

- Ejecutar pruebas automáticamente ante cambios en el repositorio.
- Analizar la calidad del código con herramientas de análisis estático.
- Desplegar automáticamente la aplicación en un entorno accesible por Internet.
- Notificar los resultados del proceso en tiempo real al equipo de desarrollo.

---

## 🧰 Herramientas utilizadas

| Herramienta       	 | Propósito                                 			|
|------------------------|------------------------------------------------------|
| **Git & GitHub**  	 | Control de versiones y hosting del código 			|
| **GitHub Actions**	 | Servidor de CI/CD para automatizar procesos 			|
| **pytest**        	 | Ejecución de pruebas unitarias            			|
| **SonarCloud**    	 | Análisis de calidad y seguridad del código 			|
| **Render**        	 | Despliegue automático de la API en la nube 			|
| **Slack**         	 | Mecanismo de feedback inmediato al equipo 			|
| **FastAPI**       	 | Framework para el desarrollo de la API en Python 	|
| **Visual Studio Code** | Entorno de desarrollo utilizado por el equipo 		|

---

## 🔁 Flujo de trabajo (CI/CD)

1. **Push o Pull Request en `main`**:
   - Se dispara una pipeline en GitHub Actions.
2. **Etapa de Integración Continua (CI)**:
   - Se instalan dependencias y ejecutan los tests con `pytest`.
   - Se realiza análisis de calidad de código en SonarCloud.
3. **Etapa de Despliegue Continuo (CD)**:
   - Si todo es exitoso, se despliega la aplicación en Render.
   - Se realiza un *health-check* para verificar que la app está disponible.
4. **Notificación**:
   - Slack notifica automáticamente al equipo el resultado de cada etapa.
