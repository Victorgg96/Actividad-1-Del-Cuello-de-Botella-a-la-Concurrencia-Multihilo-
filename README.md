# Proyecto Redes — Servidor TCP Secuencial vs. Concurrente

## Requisitos

- Python 3.8 o superior (sin dependencias externas).
- Windows 11 / PowerShell (los comandos abajo usan PowerShell).

---

## Estructura del proyecto

```
proyecto-redes/
├── fase1_servidor_secuencial.py   # Servidor bloqueante (un cliente a la vez)
├── fase2_servidor_concurrente.py  # Servidor con threading (thread-per-client)
├── cliente_prueba.py              # Cliente TCP de prueba
├── README.md                      # Este archivo
├── REPORTE.md                     # Cuerpo del informe académico
└── evidencias/                    # Carpeta para capturas de pantalla
```

---

## Fase 1 — Servidor Secuencial

### 1. Consola A — Iniciar el servidor

```powershell
python fase1_servidor_secuencial.py
```

### 2. Consola B — Primer cliente (lanzar de inmediato)

```powershell
python cliente_prueba.py
```

### 3. Consola C — Segundo cliente (lanzar ~1 s después del primero)

```powershell
python cliente_prueba.py
```

**Resultado esperado:** el segundo cliente tarda ≈ 20 s porque espera que el
primero termine sus 10 s de procesamiento. El servidor solo atiende uno a la vez.

---

## Fase 2 — Servidor Concurrente

Detén el servidor anterior con `Ctrl+C` y repite el mismo procedimiento:

### 1. Consola A

```powershell
python fase2_servidor_concurrente.py
```

### 2. Consola B

```powershell
python cliente_prueba.py
```

### 3. Consola C (casi simultáneo con B)

```powershell
python cliente_prueba.py
```

**Resultado esperado:** ambos clientes terminan en ≈ 10 s porque cada uno
corre en un hilo independiente.

---

## Alternativa con ncat (Nmap) o telnet

```powershell
# ncat
ncat 127.0.0.1 8000

# telnet (si está habilitado en Windows)
telnet 127.0.0.1 8000
```

Escribe cualquier texto y presiona Enter para enviar.

---

## Exportar REPORTE.md a PDF

**Opción 1 — Pandoc (recomendado):**

```powershell
pandoc REPORTE.md -o reporte.pdf
```

**Opción 2 — VS Code:**  
Abre `REPORTE.md` → clic derecho → *Open Preview* → desde el preview imprime
con `Ctrl+P` y elige "Guardar como PDF".

**Opción 3 — Markdown to PDF (extensión VS Code):**  
Instala la extensión *Markdown PDF* y usa el comando *Markdown PDF: Export (pdf)*.

---

## Subir a GitHub (opcional)

```powershell
cd "C:\Users\vican\OneDrive\Escritorio\Claude Code\proyecto-redes"
git init
git add .
git commit -m "Proyecto redes: servidor TCP secuencial vs concurrente"
git remote add origin https://github.com/TU_USUARIO/proyecto-redes.git
git push -u origin main
```

Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub y actualiza la URL
del repo en `REPORTE.md`.
