# Monorepo HW-05 - Arquitectura de Sistemas

Proyecto desarrollado con **Turborepo, pnpm, Next.js, Express y TypeScript**. El objetivo es organizar varias aplicaciones y paquetes compartidos dentro de un solo repositorio.

## 1. Estructura del proyecto

```text
monorepo-hw05/
├── apps/
│   ├── web/                 # Aplicación frontend
│   ├── api/                 # API backend con Express
│   └── docs/                # Aplicación de documentación
├── packages/
│   ├── shared/              # Librería compartida
│   ├── ui/                  # Componentes de interfaz
│   ├── eslint-config/       # Configuración de ESLint
│   └── typescript-config/   # Configuración de TypeScript
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
├── turbo.json
└── README.md
```

## 2. Requisitos previos

Instalar:

- Node.js (versión 20.9 o superior).
- pnpm.
- Git.

Verificar las instalaciones:

```bash
node -v
pnpm -v
git --version
```

## 3. Instalación desde cero

Clonar el repositorio:

```bash
git clone https://github.com/DiegoUmeso/Arquitectura-de-sistemas.git
cd Arquitectura-de-sistemas
```

Cambiar a la rama de la tarea:

```bash
git switch hw-05
```

Instalar las dependencias:

```bash
pnpm install
```

## 4. Ejecutar las aplicaciones

Para iniciar las aplicaciones y servicios que tienen configurada la tarea `dev`:

```bash
pnpm dev
```

Direcciones locales:

- Frontend: http://localhost:3000
- API backend: http://localhost:3001
- Documentación: http://localhost:3002

Para detener los servicios, presionar `Ctrl + C` en la terminal.

### Ejecutar una aplicación individualmente

Frontend:

```bash
pnpm --filter web dev
```

Backend:

```bash
pnpm --filter @repo/api dev
```

Documentación:

```bash
pnpm --filter docs dev
```

## 5. Librería compartida

La librería se encuentra en `packages/shared`.

Incluye la función `getWelcomeMessage(appName)`, que genera un mensaje reutilizable. El frontend y el backend importan esta función desde `@repo/shared`, evitando duplicar la misma lógica.

Ejemplo:

```typescript
import { getWelcomeMessage } from "@repo/shared";

const message = getWelcomeMessage("Frontend");
```

## 6. Comandos generales

Ejecutar desde la raíz del repositorio:

| Comando | Descripción |
|---|---|
| `pnpm dev` | Inicia las aplicaciones configuradas para desarrollo. |
| `pnpm build` | Construye los proyectos que tienen la tarea `build`. |
| `pnpm test` | Ejecuta las tareas de prueba configuradas. |
| `pnpm lint` | Ejecuta las tareas de análisis de código configuradas. |
| `pnpm check-types` | Ejecuta las comprobaciones de tipos configuradas. |
| `pnpm format` | Formatea los archivos TypeScript, TSX y Markdown. |

### Construir una aplicación individual

```bash
pnpm --filter @repo/api build
pnpm --filter web build
pnpm --filter docs build
```

Las pruebas incluidas son comprobaciones básicas configuradas en los paquetes; no representan una suite completa de pruebas unitarias.

## 7. Uso de Turborepo

Turborepo permite ejecutar tareas de varios paquetes desde la raíz, organizar sus dependencias y reutilizar resultados mediante su sistema de caché.

El archivo `turbo.json` define las tareas del proyecto y `pnpm-workspace.yaml` registra las aplicaciones y paquetes del monorepo.

## 8. Ventajas del monorepo

- Centraliza el código de varias aplicaciones en un repositorio.
- Permite compartir funciones y componentes.
- Facilita la instalación y ejecución de tareas desde la raíz.
- Mantiene las configuraciones comunes organizadas.
- Permite coordinar las tareas mediante Turborepo.

## 9. Evidencias

Las capturas de pantalla de la ejecución y las pruebas del proyecto se encuentran en:

`packages/Screenshoot/`

## 10. Flujo de trabajo con Git

Se recomienda utilizar mensajes de commit con el formato Conventional Commits.

Ejemplos:

```bash
git add .
git commit -m "feat: agregar libreria compartida"
git commit -m "docs: actualizar instrucciones del proyecto"
```
