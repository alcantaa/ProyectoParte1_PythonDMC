import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp
import libreria_clases_proyecto1 as lcp

# ------------------------------------------------------------------
# Estado global (histórico / registros de cada ejercicio)
# ------------------------------------------------------------------
if "movimientos_ej1" not in st.session_state:
    st.session_state.movimientos_ej1 = []  # lista de dicts: concepto, tipo, valor
 
if "registros_ej2" not in st.session_state:
    # Se guardan como arrays de NumPy independientes por columna
    st.session_state.registros_ej2 = {
        "nombre_producto": np.array([], dtype=object),
        "categoria": np.array([], dtype=object),
        "precio": np.array([], dtype=float),
        "cantidad": np.array([], dtype=int),
        "total": np.array([], dtype=float),
    }
 
if "historico_ej3" not in st.session_state:
    st.session_state.historico_ej3 = pd.DataFrame(
        columns=[
            "tiempo_operacion_h", "numero_fallas", "tiempo_reparacion_total_h",
            "mtbf_h", "mttr_h", "disponibilidad_pct",
        ]
    )
 
if "proyectos_ej4" not in st.session_state:
    st.session_state.proyectos_ej4 = []

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
    st.title('Ejercicio 3: Indicadores de Mantenimiento')
    st.markdown(
        '''
        Este módulo calcula **MTBF**, **MTTR** y **disponibilidad** a partir del
        tiempo de operación, el número de fallas y el tiempo total de reparación,
        usando la función `calcular_indicadores_mantenimiento` de la librería del proyecto.
        '''
    )
 
    tiempo_operacion_h = st.number_input(
        "Tiempo de operación (horas)", min_value=0.0, value=100.0, step=1.0, key="op_ej3"
    )
    numero_fallas = st.number_input("Número de fallas", min_value=1, value=5, step=1, key="fallas_ej3")
    tiempo_reparacion_total_h = st.number_input(
        "Tiempo total de reparación (horas)", min_value=0.0, value=10.0, step=1.0, key="rep_ej3"
    )
 
    if st.button("Ejecutar cálculo", key="btn_ej3"):
        try:
            resultado = lfp.calcular_indicadores_mantenimiento(
                tiempo_operacion_h=tiempo_operacion_h,
                numero_fallas=int(numero_fallas),
                tiempo_reparacion_total_h=tiempo_reparacion_total_h,
            )
 
            st.success("Cálculo realizado correctamente ✅")
            col1, col2, col3 = st.columns(3)
            col1.metric("MTBF (h)", resultado["mtbf_h"])
            col2.metric("MTTR (h)", resultado["mttr_h"])
            col3.metric("Disponibilidad (%)", resultado["disponibilidad_pct"])
 
            nueva_fila = {
                "tiempo_operacion_h": tiempo_operacion_h,
                "numero_fallas": numero_fallas,
                "tiempo_reparacion_total_h": tiempo_reparacion_total_h,
                **resultado,
            }
            st.session_state.historico_ej3 = pd.concat(
                [st.session_state.historico_ej3, pd.DataFrame([nueva_fila])], ignore_index=True
            )
        except ValueError as e:
            st.error(f"Error en los datos ingresados: {e}")
 
    st.subheader("📋 Histórico de resultados")
    if not st.session_state.historico_ej3.empty:
        st.dataframe(st.session_state.historico_ej3, use_container_width=True)
        if st.button("Limpiar histórico", key="limpiar_ej3"):
            st.session_state.historico_ej3 = st.session_state.historico_ej3.iloc[0:0]
            st.rerun()
    else:
        st.info("Aún no hay resultados calculados. Ejecuta el cálculo para ver el histórico aquí.")
 
# ==================================================================
# EJERCICIO 4 - Proyecto de Inversión (VPN, ROI, Payback) - CRUD
# ==================================================================
elif app_mode == 'Ejercicio 4':
    st.title('Ejercicio 4: Proyecto de Inversión (CRUD)')
    st.markdown(
        '''
        Este módulo usa la clase `ProyectoInversion` (VPN, ROI, Payback simple) de la
        librería del proyecto, con operaciones **CRUD** completas: crear, leer,
        actualizar y eliminar proyectos.
        '''
    )
 
    def _reconstruir_resumen(proy: dict) -> dict:
        obj = lcp.ProyectoInversion(
            nombre_proyecto=proy["nombre_proyecto"],
            inversion_inicial=proy["inversion_inicial"],
            flujos=proy["flujos"],
            tasa_descuento_pct=proy["tasa_descuento_pct"],
        )
        return obj.resumen()
 
    def _tabla_proyectos() -> pd.DataFrame:
        filas = []
        for proy in st.session_state.proyectos_ej4:
            resumen = _reconstruir_resumen(proy)
            filas.append(
                {
                    "nombre_proyecto": proy["nombre_proyecto"],
                    "inversion_inicial": proy["inversion_inicial"],
                    "flujos": proy["flujos"],
                    "tasa_descuento_pct": proy["tasa_descuento_pct"],
                    "vpn": resumen["vpn"],
                    "roi_pct": resumen["roi_pct"],
                    "payback_anios": resumen["payback_anios"],
                    "decision": resumen["decision"],
                }
            )
        return pd.DataFrame(filas)
 
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
        ["➕ Crear", "📋 Leer", "✏️ Actualizar", "🗑️ Eliminar"]
    )
 
    with tab_crear:
        st.write("### Nuevo proyecto de inversión")
        with st.form("form_crear_proyecto", clear_on_submit=True):
            nombre_proyecto = st.text_input("Nombre del proyecto")
            inversion_inicial = st.number_input(
                "Inversión inicial", min_value=0.01, value=1000.0, step=100.0
            )
            flujos_texto = st.text_input(
                "Flujos de caja por periodo (separados por coma)", placeholder="Ej: 300, 300, 400, 500"
            )
            tasa_descuento_pct = st.number_input(
                "Tasa de descuento (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.5
            )
            enviado = st.form_submit_button("Crear proyecto")
 
        if enviado:
            try:
                nombres_existentes = [p["nombre_proyecto"] for p in st.session_state.proyectos_ej4]
                if not nombre_proyecto.strip():
                    raise ValueError("El nombre del proyecto no puede estar vacío.")
                if nombre_proyecto in nombres_existentes:
                    raise ValueError("Ya existe un proyecto con ese nombre.")
 
                flujos = [float(x.strip()) for x in flujos_texto.split(",") if x.strip() != ""]
 
                nuevo = lcp.ProyectoInversion(
                    nombre_proyecto=nombre_proyecto,
                    inversion_inicial=inversion_inicial,
                    flujos=flujos,
                    tasa_descuento_pct=tasa_descuento_pct,
                )
                nuevo.resumen()
 
                st.session_state.proyectos_ej4.append(
                    {
                        "nombre_proyecto": nombre_proyecto,
                        "inversion_inicial": inversion_inicial,
                        "flujos": flujos,
                        "tasa_descuento_pct": tasa_descuento_pct,
                    }
                )
                st.success(f"Proyecto '{nombre_proyecto}' creado correctamente ✅")
            except (ValueError, TypeError) as e:
                st.error(f"Error en los datos ingresados: {e}")
 
    with tab_leer:
        st.write("### Proyectos registrados")
        if st.session_state.proyectos_ej4:
            st.dataframe(_tabla_proyectos(), use_container_width=True)
        else:
            st.info("Aún no hay proyectos registrados. Crea uno en la pestaña 'Crear'.")
 
    with tab_actualizar:
        st.write("### Actualizar proyecto existente")
        if not st.session_state.proyectos_ej4:
            st.info("No hay proyectos para actualizar.")
        else:
            nombres = [p["nombre_proyecto"] for p in st.session_state.proyectos_ej4]
            seleccionado = st.selectbox("Selecciona el proyecto a actualizar", nombres, key="sel_actualizar")
            idx = nombres.index(seleccionado)
            proy_actual = st.session_state.proyectos_ej4[idx]
 
            with st.form("form_actualizar_proyecto"):
                nueva_inversion = st.number_input(
                    "Inversión inicial", min_value=0.01, value=float(proy_actual["inversion_inicial"]), step=100.0
                )
                nuevos_flujos_texto = st.text_input(
                    "Flujos de caja por periodo (separados por coma)",
                    value=", ".join(str(f) for f in proy_actual["flujos"]),
                )
                nueva_tasa = st.number_input(
                    "Tasa de descuento (%)", min_value=0.0, max_value=100.0,
                    value=float(proy_actual["tasa_descuento_pct"]), step=0.5,
                )
                actualizar = st.form_submit_button("Actualizar proyecto")
 
            if actualizar:
                try:
                    nuevos_flujos = [float(x.strip()) for x in nuevos_flujos_texto.split(",") if x.strip() != ""]
                    lcp.ProyectoInversion(
                        nombre_proyecto=proy_actual["nombre_proyecto"],
                        inversion_inicial=nueva_inversion,
                        flujos=nuevos_flujos,
                        tasa_descuento_pct=nueva_tasa,
                    )
                    st.session_state.proyectos_ej4[idx] = {
                        "nombre_proyecto": proy_actual["nombre_proyecto"],
                        "inversion_inicial": nueva_inversion,
                        "flujos": nuevos_flujos,
                        "tasa_descuento_pct": nueva_tasa,
                    }
                    st.success(f"Proyecto '{seleccionado}' actualizado correctamente ✅")
                except (ValueError, TypeError) as e:
                    st.error(f"Error en los datos ingresados: {e}")
 
    with tab_eliminar:
        st.write("### Eliminar proyecto")
        if not st.session_state.proyectos_ej4:
            st.info("No hay proyectos para eliminar.")
        else:
            nombres = [p["nombre_proyecto"] for p in st.session_state.proyectos_ej4]
            a_eliminar = st.selectbox("Selecciona el proyecto a eliminar", nombres, key="sel_eliminar")
 
            if st.button("Eliminar proyecto", key="btn_eliminar_ej4"):
                st.session_state.proyectos_ej4 = [
                    p for p in st.session_state.proyectos_ej4 if p["nombre_proyecto"] != a_eliminar
                ]
                st.success(f"Proyecto '{a_eliminar}' eliminado correctamente 🗑️")
                st.rerun()
