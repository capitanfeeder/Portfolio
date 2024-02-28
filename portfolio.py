import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Mi Portfolio",
        page_icon=":rocket:",
        layout="wide"
    )

    # Estilo personalizado
    st.markdown(
        """
        <style>
            .main {
                background-color: #f8f9fa;
            }
            .sidebar .sidebar-content {
                background-color: #343a40;
                color: #ffffff;
            }
            .Widget.stButton {
                background-color: #007bff;
                color: #ffffff;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título
    st.title("Mi Portfolio")

    # Menú de navegación
    navigation = st.sidebar.radio("Navegación", ["Inicio", "Proyectos", "Habilidades", "Contacto"])

    if navigation == "Inicio":
        show_home()
    elif navigation == "Proyectos":
        show_projects()
    elif navigation == "Habilidades":
        show_skills()
    elif navigation == "Contacto":
        show_contact()

def show_home():
    st.header("Bienvenido a mi Portfolio")
    # Agregar la ruta de la imagen de tu foto
    photo_path = "Gabriel.jpg"

    # Mostrar tu foto
    st.image(photo_path, width=500, caption="Gabriel Sosa (Data Engineer)")

    st.write("Hola, soy Gabriel Sosa, un apasionado del análisis y la ingeniería de datos con una sólida formación en la aplicación de técnicas avanzadas de análisis para generar percepciones significativas y guiar la toma de decisiones estratégicas. Mi experiencia abarca desde la manipulación experta de datos utilizando Python y MySQL hasta la creación de visualizaciones impactantes en PowerBI. Mi profundo entendimiento de sistemas Linux y mi habilidad para desarrollar y optimizar algoritmos de Machine Learning complementan mi enfoque integral para abordar desafíos complejos. Además, poseo un conocimiento amplio de AWS y experiencia en la automatización de procesos de ETL (Extract, Transform, Load), lo que me permite diseñar soluciones escalables y eficientes para el manejo de grandes volúmenes de datos.")
def show_projects():
    st.header("Proyectos Destacados")

    # Lista de proyectos con imágenes y enlaces
    projects = [
        {
            "name": "Modelo de ML: Recomendación de juegos en Steam",
            "description": "En este proyecto, apliqué mis conocimientos para desarrollar un modelo de recomendación que considera la similitud entre los juegos consumidos por el usuario. Teniendo en cuenta diversos factores, como géneros y puntuaciones positivas, el modelo se diseñó para proporcionar recomendaciones personalizadas, optimizando así la experiencia del usuario.",
            "image": "steam.png",
            "project_link": "https://github.com/capitanfeeder/Modelo_ML_STEAM"
        },
        {
            "name": "Análisis de datos relacionado a accidentes de tránsito en CABA (Argentina)",
            "description": "Llevé a cabo un análisis de datos sobre accidentes de tránsito en CABA (Argentina), utilizando gráficos y elementos visuales para aplicar storytelling y resaltar puntos clave de esta problemática. Además, contrasté la información obtenida con datos del Catálogo de Datos Abiertos de Montevideo (Uruguay), explorando el marco jurídico para comparar las cifras de accidentes basadas en las disposiciones legales de cada lugar. Finalmente, presenté recomendaciones orientadas a la reducción de los accidentes de tránsito.",
            "image": "accidente.png",
            "project_link": "https://github.com/capitanfeeder/DataAnalytics_Accidentes_en_CABA"
        },
        {
            "name": "Análisis de mercado en Taxis de NYC",
            "description": "Proyecto donde junto a mi equipo, automatizamos el proceso de recolección, exploración, optimización y visualización de datos, como así también el entrenamiento de modelos de Machine Learning para realizar un trabajo óptimo en virtud de la inmensa cantidad de información manipulada. Todo esto con ayuda de los servicios de AWS.",
            "image": "taxis.jpg",
            "project_link": "https://github.com/capitanfeeder/Proyecto-Taxis-NYC"
        },
        {
            "name": "Orquestación Automatizada con Apache Airflow",
            "description": "El proyecto se centra en la automatización de procesos mediante el uso de Apache Airflow. Utilizando este framework de orquestación de flujos de trabajo, se ha desarrollado un sistema para realizar tareas de extracción, transformación y carga de datos de manera automatizada. Esto implica la creación de DAGs (Directed Acyclic Graphs) en Airflow para definir y ejecutar secuencias de tareas, que incluyen la descarga de datos, transformaciones, carga en una base de datos PostgreSQL y validación de la integridad de los datos cargados. El objetivo principal es optimizar y agilizar el flujo de trabajo de procesamiento de datos mediante la automatización de tareas repetitivas y la coordinación eficiente de las diferentes etapas del proceso.",
            "image": "titanic.jpg",
            "project_link": "https://github.com/capitanfeeder/Titanic-Airflow-DAG"
        }
    ]

    # Muestra los proyectos con imágenes y enlaces
    col1, col2, col3 = st.columns(3)
    for project in projects:
        with col1:
            st.subheader(project["name"])
            st.image(project["image"], use_column_width=True)
            st.write(project["description"])
            st.markdown(f"[Ver Proyecto]({project['project_link']})", unsafe_allow_html=True)
            st.markdown("---")


def show_skills():
    st.header("Habilidades técnicas")

    # Etiquetas de habilidades
    skills_tags = [
        "![Python](https://img.shields.io/badge/Python-black?style=flat&logo=python)",
        "![Pandas](https://img.shields.io/badge/Pandas-black?style=flat&logo=pandas)",
        "![Numpy](https://img.shields.io/badge/Numpy-black?style=flat&logo=Numpy)",
        "![Pyarrow](https://img.shields.io/badge/Pyarrow-black?style=flat&logo=python&logoColor=white)",
        "![ScikitLearn](https://img.shields.io/badge/ScikitLearn-black?style=flat&logo=Scikit-Learn)",
        "![XGBoost](https://img.shields.io/badge/XGBoost-black?style=flat&logo=scikit-learn)",
        "![Streamlit](https://img.shields.io/badge/Streamlit-black?style=flat&logo=streamlit)",
        "![FastAPI](https://img.shields.io/badge/FastAPI-black?style=flat&logo=fastapi)",
        "![PyAthena](https://img.shields.io/badge/PyAthena-black?style=flat&logo=python&logoColor=purple)",
        "![Boto3](https://img.shields.io/badge/Boto3-black?style=flat&logo=AWS%20Organizations)",
        "![S3FS](https://img.shields.io/badge/S3FS-black?style=flat&logo=AMAZON%20S3&logoColor=white)",
        "![Tkinter](https://img.shields.io/badge/Tkinter-black?style=flat&logo=python&logoColor=white)",
        "![Pyinstaller](https://img.shields.io/badge/Pyinstaller-black?style=flat&logo=python&logoColor=white)",
        "![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-black?style=flat&logo=coffeescript)",
        "![Plotly](https://img.shields.io/badge/Plotly-black?style=flat&logo=plotly)",
        "![Pydantic](https://img.shields.io/badge/Pydantic-black?style=flat&logo=pydantic)",
        "![Joblib](https://img.shields.io/badge/Joblib-black?style=flat&logo=Python)",
        "![Power BI](https://img.shields.io/badge/Power%20BI-black?style=flat&logo=Power%20bi)",
        "![Amazon S3](https://img.shields.io/badge/AWS%20S3-black?style=flat&logo=Amazon%20S3)",
        "![AWS Athena](https://img.shields.io/badge/AWS%20Athena-black?style=flat&logo=Amazon%20AWS&logoColor=purple)",
        "![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-black?style=flat&logo=AWS%20lambda)",
        "![AWS EventBridge](https://img.shields.io/badge/AWS%20EventBridge-black?style=flat&logo=aws%20lambda&logoColor=%20pink)",
        "![AWS Glue](https://img.shields.io/badge/AWS%20Glue-black?style=flat&logo=AWS%20OrganizationS&logoColor=blue)",
        "![AWS Sagemaker](https://img.shields.io/badge/AWS%20Sagemaker-black?style=flat&logo=AmazonAWS&logoColor=green)",
        "![AWS Quicksight](https://img.shields.io/badge/AWS%20Quicksight-black?style=flat&logo=AmazonAWS&logoColor=yellow)",
        "![Pyspark](https://img.shields.io/badge/Pyspark-black?style=flat&logo=apache%20spark)",
        "![Render](https://img.shields.io/badge/Render-black?style=flat&logo=RENDER)",
        "![Seaborn](https://img.shields.io/badge/Seaborn-black?style=flat&logo=seaborn)",
        "![Matplotlib](https://img.shields.io/badge/Matplotlib-black?style=flat&logo=matplotlib)",
        "![Railway](https://img.shields.io/badge/Railway-black?style=flat&logo=railway)"
    ]

    # Muestra las etiquetas en una fila
    st.markdown(" ".join(skills_tags), unsafe_allow_html=True)

    # Separador entre habilidades técnicas y blandas
    st.markdown("---")

    # Habilidades blandas
    st.header("Habilidades blandas")

    soft_skills = """
    - Comunicación efectiva
    - Trabajo en equipo
    - Resolución de problemas
    - Creatividad
    - Adaptabilidad
    - Gestión del tiempo
    - Empatía
    - Toma de decisiones
    - Liderazgo
    - Colaboración
    - Resiliencia
    - Pensamiento crítico
    - Pensamiento estratégico
    """

    # Muestra las habilidades blandas
    st.write(soft_skills)

    # Idiomas
    st.header("Idiomas")

    # Etiqueta de inglés con enlace al certificado de EF SETS
    english_certificate_link = "https://www.efset.org/cert/HxTKGT"
    st.markdown(f"**Inglés: C1** [Certificado EF SET]({english_certificate_link})")


def show_contact():
    st.header("Contacto")

    # Agrega tus enlaces de redes sociales
    st.write("¡Contáctame en mis redes o por correo!")
    st.markdown("[![linkedin](https://img.shields.io/badge/linkedin-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabriel-sosa26/)", unsafe_allow_html=True)
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/capitanfeeder)", unsafe_allow_html=True)
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gabrielwesker26@gmail.com)", unsafe_allow_html=True)


if __name__ == "__main__":
    main()