# installer dans powershell : pip install streamlit-authenticator
# installer dans powershell : pip install streamlit-option-menu

import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()
#créer le bouton deconnexion dans la barre latérale
with st.sidebar :
    if st.session_state["authentication_status"]:
    # Le bouton de déconnexion
     authenticator.logout("Déconnexion")
     st.write('Bienvenue: Root')

# Créer le menu dans la barre latérale
if st.session_state["authentication_status"]:
    with st.sidebar:
        selection = option_menu(
            menu_title=None,  # Pas de titre de menu
            options=["Accueil", "Photos de mon chat"]
    )


if st.session_state["authentication_status"]:
    # On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
                st.title("Bienvenue sur ma page")
                st.image("https://th.bing.com/th/id/R.7e9183f95a1237eed74b6e911f4aa030?rik=6FRjaPSeXY2pUw&riu=http%3a%2f%2fmariepierrem.m.a.pic.centerblog.net%2ffv5s7fd8s6.png&ehk=LJjgr%2bndWf9891%2bDJgWc5f5Gm9ckXgW4Q6RAZC%2b0c%2fA%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1")
    elif selection == "Photos de mon chat":
                st.title("Bienvenue dans l'album de mon Félix :cat: ")
                col1, col2, col3 = st.columns(3)
                with col1:
                        st.image("https://www.starnimo.com/wp-content/uploads/2020/12/chaton-mignon-roux-821x1536.jpg")
                        st.write("Mon chat bébé")
                with col2:
                        st.image("https://th.bing.com/th/id/OIP.t7n2xUAuM3dLpAlvM2rH3wHaEv?rs=1&pid=ImgDetMain")
                        st.write("Le chat en mode détente")
                with col3:
                        st.image("https://th.bing.com/th/id/OIP.eUjoOLdCIHEWmWMpAh2gtwHaEK?rs=1&pid=ImgDetMain")
                        st.write("Mon chat entrain de reviser les cours de machine learning")
                    
                    # ... et ainsi de suite pour les autres pages

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


