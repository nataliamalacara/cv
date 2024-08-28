

import streamlit as st

# Columna izquierda: Foto y contacto
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("""
    **Estudiante de Finanzas en la Universidad Panamericana**, destacada por la
    resolución ágil de problemas y habilidades para trabajar en equipo. Comprometida con la excelencia,
    estoy entusiasmada por aplicar mis conocimientos en un entorno profesional.
    """)
    st.markdown("### CONTACTO")
    st.markdown("""
    - **Celular:** 33 2254 0418  
    - **Correo:** nmalacaraj@gmail.com
    """)

    st.markdown("### EDUCACIÓN")
    st.markdown("""
    - **Universidad Panamericana**  
      Finanzas | 2020 - Presente  
    - **Preparatoria | Colegio Los Altos**  
      Generación 2020 | Mención de honor  
    """)

# Columna derecha: Habilidades y experiencia
with col2:
    st.markdown("## NATALIA MALACARA")
    st.markdown("### ESTUDIANTE UNIVERSITARIA EN FINANZAS")

    st.markdown("### HABILIDADES Y COMPETENCIAS")
    st.markdown("""
    - **Idiomas**:  
        - Inglés (Certificación TOEFL C1)  
        - Francés (Avanzado)
    - Dominio de Excel
    - Trabajo en Equipo
    - Comunicación oral y escrita
    - Resolución de problemas
    - Creatividad
    - Determinación para lograr mis objetivos
    - Sentido de responsabilidad
    - Facilidad de aprendizaje
    """)

    st.markdown("### EXPERIENCIA LABORAL")
    st.markdown("""
    - **Mala Effortless Wear**  
      Asistente comercial y financiera | 2021 - Feb 2023  
      - Resumen de ventas. Manejo de redes sociales. Atención al cliente. Contabilidad. Enlace entre proveedores y puntos de venta.
    
    - **Trabajo de verano**  
      Blen | 2018  
      - Área de pedidos y empacado.
    """)

    st.markdown("### INTERESES Y LOGROS ADICIONALES")
    st.markdown("""
    - **Estudiante de intercambio en Austria**  
      IMC Krems | Febrero - Junio 2023  
    
    - **Voluntariado**  
      Promoción rural familiar
    
    - **Curso de SAP**  
      2023
    """)

# Línea divisoria y espacio en blanco al final
st.write("---")