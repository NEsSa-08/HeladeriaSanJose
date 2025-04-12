import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Conexión a MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # ← Cambia esto
        password="12345678", # ← Y esto
        database="HeladeriaSanJose"
    )

# Estructura de las tablas
tablas = {
    "clientes": ["id", "nombre", "telefono", "email"],
    "pedidos": ["id", "cliente_id", "fecha", "total"],
    "productos": ["id", "nombre", "precio", "descripcion", "tipo"],
    "detalle_pedido": ["id", "pedido_id", "producto_id", "cantidad", "subtotal"]
}

#  Actualizar formulario al cambiar tabla
def cambiar_tabla(event=None):
    for widget in frame_campos.winfo_children():
        widget.destroy()
    campos.clear()

    tabla = combo_tablas.get()
    for i, campo in enumerate(tablas[tabla]):
        tk.Label(frame_campos, text=campo).grid(row=i, column=0, sticky="w")
        entry = tk.Entry(frame_campos)
        entry.grid(row=i, column=1, padx=5, pady=2, sticky="ew")
        if campo == "id":
            entry.config(state="disabled")
        campos[campo] = entry
    mostrar_datos()

#  Agregar registro
def agregar():
    tabla = combo_tablas.get()
    datos = []
    columnas = []

    for campo in tablas[tabla]:
        if campo == "id":
            continue
        if tabla == "pedidos" and campo == "fecha":
            continue  # que MySQL la llene con CURRENT_TIMESTAMP
        valor = campos[campo].get()
        if not valor and campo != "fecha":
            messagebox.showwarning("Campo vacío", f"{campo} es obligatorio")
            return
        columnas.append(campo)
        datos.append(valor if valor else None)

    placeholders = ", ".join(["%s"] * len(datos))
    columnas_str = ", ".join(columnas)

    conn = conectar()
    cursor = conn.cursor()
    query = f"INSERT INTO {tabla} ({columnas_str}) VALUES ({placeholders})"
    cursor.execute(query, datos)
    conn.commit()
    conn.close()
    mostrar_datos()
    limpiar()

#  Actualizar registro
def actualizar():
    tabla = combo_tablas.get()
    id_val = campos["id"].get()
    if not id_val:
        messagebox.showerror("Error", "Selecciona un registro")
        return

    datos = []
    for campo in tablas[tabla]:
        if campo != "id":
            datos.append(campos[campo].get())
    columnas = ", ".join([f"{c}=%s" for c in tablas[tabla] if c != "id"])

    conn = conectar()
    cursor = conn.cursor()
    query = f"UPDATE {tabla} SET {columnas} WHERE id=%s"
    cursor.execute(query, (*datos, id_val))
    conn.commit()
    conn.close()
    mostrar_datos()
    limpiar()

# Eliminar registro
def eliminar():
    tabla = combo_tablas.get()
    id_val = campos["id"].get()
    if not id_val:
        messagebox.showerror("Error", "Selecciona un registro")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tabla} WHERE id=%s", (id_val,))
    conn.commit()
    conn.close()
    mostrar_datos()
    limpiar()

# Limpiar campos
def limpiar():
    for entry in campos.values():
        entry.config(state="normal")
        entry.delete(0, tk.END)
    campos["id"].config(state="disabled")

# Mostrar registros en listbox
def mostrar_datos():
    tabla = combo_tablas.get()
    listbox.delete(0, tk.END)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    for fila in cursor.fetchall():
        listbox.insert(tk.END, fila)
    conn.close()

# Cargar registro desde listbox
def seleccionar(event):
    if not listbox.curselection():
        return
    index = listbox.curselection()[0]
    valores = listbox.get(index)

    for i, campo in enumerate(tablas[combo_tablas.get()]):
        entry = campos[campo]
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, valores[i])
        if campo == "id":
            entry.config(state="disabled")

#  Interfaz principal
root = tk.Tk()
root.title("CRUD - Heladería San José")
root.geometry("750x500")

# Menu de tablas
tk.Label(root, text="Seleccionar tabla:").pack(pady=5)
combo_tablas = ttk.Combobox(root, values=list(tablas.keys()), state="readonly")
combo_tablas.pack()
combo_tablas.bind("<<ComboboxSelected>>", cambiar_tabla)
combo_tablas.set("clientes")  # default

#  Frame de campos
frame_campos = tk.Frame(root)
frame_campos.pack(pady=10, fill="x", padx=20)
campos = {}

#  Botones
frame_botones = tk.Frame(root)
frame_botones.pack()
tk.Button(frame_botones, text="Agregar", command=agregar).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Actualizar", command=actualizar).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Eliminar", command=eliminar).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar).grid(row=0, column=3, padx=5)

# Lista
listbox = tk.Listbox(root, width=100, height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", seleccionar)

# Inicializar
cambiar_tabla()

root.mainloop()
