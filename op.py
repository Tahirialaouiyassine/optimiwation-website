import pybase64
import streamlit as st
import nbformat
st.title("Optimization by the Passing Vehicle Search method with Python ")
st.header("A Practical Application for Portfolio Management")
st.subheader("Introduction")
st.write('''Welcome to our application dedicated to financial optimization using Python. This end-of-year project illustrates the practical application of advanced optimization techniques in portfolio management. In a financial world where decisions must be made quickly and efficiently, optimization plays a crucial role in maximizing returns while minimizing risks. This project presents a new optimization method called Passing Vehicle Search (PVS), integrated into an interactive tool for portfolio management.''')
st.subheader("Presentation of the Passing Vehicle Search Optimization Method")
st.write(''' Passing Vehicle Search (PVS) is a recent and innovative optimization method inspired by the movements of vehicles passing through checkpoints. Unlike traditional methods, PVS stands out for its ability to efficiently explore the search space and avoid the pitfalls of local optima. It models the search process as a vehicle passing through different points, adjusting its trajectory to find the optimal solution more quickly and accurately.

Applying this method in finance allows for solving complex portfolio management problems, where the objective is to maximize returns while adhering to risk constraints. With PVS, we can navigate the vast space of available financial assets, identifying combinations that offer the best balance between risk and return.''')
st.write("The attached report details all of our work, including theoretical concepts, methodology, and obtained results. If you are interested in an in-depth analysis of our project and the financial optimization techniques used, we invite you to read this report.")

file = "Passing_Vehicle_Search.pdf"
# Opening file from file path
with open(file, "rb") as f:
    base64_pdf = pybase64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)
# Save this code in a file named `app.py`

# Chemin du fichier
fichier = 'pvs_application_in_finance.ipynb'

# Fonction pour lire le contenu d'un notebook Jupyter et extraire le code Python
def lire_code_notebook(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        code = ""
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                code += ''.join(cell['source']) + '\n'
        return code
    except FileNotFoundError:
        return "Fichier non trouvé. Veuillez vérifier le chemin du fichier."
    except Exception as e:
        return f"Une erreur est survenue lors de la lecture du fichier : {e}"

# Titre de l'application
st.title('Displaying Python Code')

# Afficher le code contenu dans le fichier notebook
code = lire_code_notebook(fichier)

# Afficher le code dans un composant de texte avec un formatage en style code
st.code(code, language='python')

# Exécution conditionnelle pour les tests
if st.button('Run the code'):
    try:
        # Exécuter le code Python (non recommandé pour des raisons de sécurité, à utiliser avec précaution)
        exec(code)
        st.success('The code has been executed successfully.')

        image_path = "outputcode.png"
        st.image(image_path, caption="figure", width=600)

    except Exception as e:
        st.error(f'An error has occurred. : {e}')
