import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp

st.sidebar.image('DMC.png')
app_mode = st.sidebar.selectbox('_Secciones_',['Home','Ejercicio 1','Ejercicio 2','Ejercicio 3','Ejercicio 4'])

if app_mode == 'Home':
  st.title ('Proyecto N°1 de la Especialización de Python')
  st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
  st.image('Python_logo.png')
  st.markdown(
    '''
    Estudiante: Alexander Alcantara Lara
    
    Modulo 1: Python Fundamentals
    
    Información General: Profesional de Minas con experiencia en gestion de flota, gestion minera y operaciones mina en mineria a cielo abierto
    a gran escala
    
    Descripción: Desarrollo de una Aplicación con Streamlit
    '''
    )
elif app_mode == 'Ejercicio 1':
    
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 1 - Flujo de Caja", page_icon="💰")
  
  # --- Descripción del ejercicio ---
  st.markdown("""
  ## Flujo de caja con listas
  Este módulo permite registrar movimientos financieros. 
  Puedes ingresar el **concepto**, el **tipo** (Ingreso/Gasto) y el **valor**. 
  Al finalizar, verás el historial, los totales y el estado actual de tu flujo.
  """)
  
  st.divider()
  
  # --- Inicialización del estado (Session State) ---
  if "historial" not in st.session_state:
      st.session_state.historial = []
  
  # --- Interfaz de entrada de datos ---
  col1, col2, col3 = st.columns([2, 1, 1])
  
  with col1:
      concepto = st.text_input("Concepto", placeholder="Ej: Pago de luz")
  
  with col2:
      tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
  
  with col3:
      valor = st.number_input("Valor", min_value=0.0, step=1.0)
  
  # Botón para agregar
  if st.button("Agregar movimiento"):
      if concepto.strip() == "":
          st.error("Por favor, ingresa un concepto.")
      elif valor <= 0:
          st.error("El valor debe ser mayor a 0.")
      else:
          # Guardar en la lista
          registro = {
              "Concepto": concepto,
              "Tipo": tipo,
              "Valor": valor
          }
          st.session_state.historial.append(registro)
          st.success(f"Registrado: {concepto}")
  
  st.divider()
  
  # --- Cálculos y Resultados ---
  if st.session_state.historial:
      # Convertir a DataFrame para facilitar cálculos
      df = pd.DataFrame(st.session_state.historial)
      
      # Calcular totales
      total_ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
      total_gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
      saldo_final = total_ingresos - total_gastos
  
      # Mostrar Tabla
      st.subheader("Lista de movimientos registrados")
      st.dataframe(df, use_container_width=True, hide_index=True)
  
      # Mostrar Métricas
      c1, c2, c3 = st.columns(3)
      c1.metric("Total Ingresos", f"S/{total_ingresos:,.2f}")
      c2.metric("Total Gastos", f"S/{total_gastos:,.2f}")
      c3.metric("Saldo Final", f"S/{saldo_final:,.2f}")
  
      # Mostrar Estado del flujo
      if saldo_final >= 0:
          st.success(f"### El flujo de caja está **A FAVOR** 📈")
      else:
          st.error(f"### El flujo de caja está **EN CONTRA** 📉")
      
      # Botón para reiniciar
      if st.button("Limpiar todo"):
          st.session_state.historial = []
          st.rerun()
  else:
      st.info("Aún no hay movimientos registrados.")

elif app_mode == 'Ejercicio 2':
    # --- Configuración de la página ---
    st.set_page_config(page_title="Ejercicio 2 - Formulario")
    st.markdown("""
    ## Formulario
    Este módulo registrar la venta de accesorios o dispositivos de entrada/salida usando arreglos de NumPy.
    """)
    st.divider()
  
    if "registros" not in st.session_state:
        st.session_state.registros = []
    st.title("Registro con NumPy, arrays y DataFrame")
    producto =  st.text_input('Producto', placeholder="Ej: Ingrese producto")
    categoria = st.selectbox('Categoría',['Computadoras','Entrada','Salida','Almacenamiento'])
    precio_unitario = st.number_input('Precio Unitario', min_value=0.0, step=1.0)
    cantidad = st.number_input("Cantidad", min_value=0, step=1)
    total = cantidad*precio_unitario
    # Botón para agregar
    if st.button('agregar registro'):
        if producto.strip()=="":
          st.error('ingresar un producto')
        elif precio_unitario <0:
          st.error ('el precio debe ser mayor a cero')
        elif cantidad <0:
          st.error ('la cantidad debe ser mayor a cero')
        else: 
          registro = {
          'producto': producto,
          'categoria' : categoria,
          'precio unitario' : precio_unitario,
          'cantidad' : cantidad,
          'total': total
        }
        st.session_state.registros.append(registro)
        st.success("Agregado")
      
    if st.session_state.registros:
       df = pd.DataFrame(st.session_state.registros)
       st.dataframe(df,use_container_width=True, hide_index=True)
       
       # Botón para reiniciar
       if st.button("Limpiar todo"):
           st.session_state.registros = []
           st.rerun()
    else:
        st.info("Aún no hay registros.")
elif app_mode == 'Ejercicio 3':
# --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 3 - Cálculo de Disponibilidad") 
# 1. Inicializar el histórico en el session_state
  
  if 'historico_resultados' not in st.session_state:
        st.session_state.historico_resultados = []
    
  st.title("Cálculo de Disponibilidad")
  
  # 2. Selector de función (aunque solo usemos una, el ejercicio lo pide)
  opcion = st.selectbox("Seleccione la función a utilizar", 
                       ["Calcular Disponibilidad de Sistema"])
  
  # 3. Widgets para ingresar parámetros
  st.subheader("Parámetros de entrada")
  col1, col2 = st.columns(2)
  
  with col1:
      t_total = st.number_input("Tiempo Total (horas)", min_value=0.1, value=24.0, step=1.0)
  
  with col2:
      t_caida = st.number_input("Tiempo Caída (horas)", min_value=0.0, value=0.0, step=0.1)
  
  # 4. Botón para ejecutar y mostrar resultado
  if st.button("Ejecutar Función"):
      try:
          # Ejecución de la función desde la librería externa
          # Recordar que devuelve un diccionario: {"disponibilidad_pct": valor}
          resultado_dict = lfp.calcular_disponibilidad_sistema(t_total, t_caida)
          
          # Extraer el valor del diccionario
          valor_dispo = resultado_dict["disponibilidad_pct"]
          
          # 5. Mostrar resultado en pantalla
          st.success(f"La disponibilidad calculada es: {valor_dispo}%")
          st.metric("Resultado", f"{valor_dispo}%")
  
          # 6. Guardar en el histórico para el DataFrame
          registro = {
              "Función": opcion,
              "T. Total (h)": t_total,
              "T. Caída (h)": t_caida,
              "Disponibilidad (%)": valor_dispo
          }
          st.session_state.historico_resultados.append(registro)
  
      except ValueError as e:
          st.error(f"Error en los parámetros: {e}")
  
  # --- Mostrar tabla histórica ---
  st.divider()
  st.subheader("Tabla histórica de resultados")
  
  if st.session_state.historico_resultados:
      df_historico = pd.DataFrame(st.session_state.historico_resultados)
      st.dataframe(df_historico, use_container_width=True, hide_index=True)
  else:
      st.info("Aún no hay registros en el histórico.")
elif app_mode == 'Ejercicio 4':
  # --- Configuración de la página ---
  st.set_page_config(page_title="Ejercicio 4 - CRUD")
  if 'servidores' not in st.session_state:
      st.session_state.servidores = []
  
  st.title("Gestión de Servidores (CRUD)")
  
  # Usamos Tabs para organizar el CRUD
  tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])
  
  # ---------------------------------------------------------
  # C - CREATE (Crear)
  # ---------------------------------------------------------
  with tab_crear:
      st.subheader("Registrar Nuevo Servidor")
      with st.form("form_registro"):
          nombre = st.text_input("Nombre del Servidor")
          t_total = st.number_input("Tiempo Total (h)", min_value=1.0, value=24.0)
          t_caida = st.number_input("Tiempo Caída (h)", min_value=0.0, value=0.0)
          a_total = st.number_input("Almacenamiento Total (GB)", min_value=1.0, value=100.0)
          a_usado = st.number_input("Almacenamiento Usado (GB)", min_value=0.0, value=10.0)
          
          btn_crear = st.form_submit_button("Guardar Servidor")
          
          if btn_crear:
              try:
                  # Instanciamos la clase de la librería
                  nuevo_srv = srv.Servidor(nombre, t_total, t_caida, a_total, a_usado)
                  # Guardamos el resumen (diccionario) en la lista
                  st.session_state.servidores.append(nuevo_srv.resumen())
                  st.success(f"Servidor {nombre} registrado!")
              except ValueError as e:
                  st.error(f"Error: {e}")
  
  # ---------------------------------------------------------
  # R - READ (Leer)
  # ---------------------------------------------------------
  with tab_leer:
      st.subheader("Listado de Servidores")
      if st.session_state.servidores:
          df = pd.DataFrame(st.session_state.servidores)
          st.dataframe(df, use_container_width=True)
      else:
          st.info("No hay servidores registrados.")
  
  # ---------------------------------------------------------
  # U - UPDATE (Actualizar)
  # ---------------------------------------------------------
  with tab_actualizar:
      st.subheader("Modificar Datos")
      if st.session_state.servidores:
          nombres_srv = [s['servidor'] for s in st.session_state.servidores]
          elegido = st.selectbox("Selecciona servidor para editar", nombres_srv)
          
          # Formulario de edición
          nuevo_t_caida = st.number_input("Nuevo Tiempo de Caída", min_value=0.0)
          nuevo_a_usado = st.number_input("Nuevo Almacenamiento Usado", min_value=0.0)
          
          if st.button("Actualizar"):
              for s in st.session_state.servidores:
                  if s['servidor'] == elegido:
                      # Recalculamos usando la clase de nuevo para validar
                      try:
                          # Buscamos datos originales para no perder el nombre y totales
                          # (En un CRUD real guardaríamos el objeto completo)
                          upd = srv.Servidor(elegido, 1000, nuevo_t_caida, 1000, nuevo_a_usado) 
                          s['disponibilidad_pct'] = round(upd.calcular_disponibilidad(), 2)
                          s['uso_almacenamiento_pct'] = round(upd.calcular_uso_almacenamiento(), 2)
                          s['estado'] = upd.estado_servidor()
                          st.success("Actualizado")
                          st.rerun()
                      except ValueError as e:
                          st.error(e)
      else:
          st.write("Nada que actualizar.")
  
  # ---------------------------------------------------------
  # D - DELETE (Eliminar)
  # ---------------------------------------------------------
  with tab_eliminar:
      st.subheader("Eliminar Registros")
      if st.session_state.servidores:
          nombres_eliminar = [s['servidor'] for s in st.session_state.servidores]
          a_borrar = st.selectbox("Selecciona servidor a borrar", nombres_eliminar)
          
          if st.button("Eliminar permanentemente", type="primary"):
              st.session_state.servidores = [s for s in st.session_state.servidores if s['servidor'] != a_borrar]
              st.warning(f"Servidor {a_borrar} eliminado.")
              st.rerun()
 
  
