import wx  # Import de la bibliothèque wxPython pour les interfaces graphiques natives

# --- Création de l'application ---
# wx.App : point d'entrée de toute application wxPython
# False : on n'utilise pas stdout/stderr redirigés (utile en console)
app = wx.App(False)

# --- Création de la fenêtre principale (frame) ---
# wx.Frame(parent, id, titre, taille)
# parent = None : c’est la fenêtre principale (pas de parent)
# wx.ID_ANY : identifiant automatique
# Titre de la fenêtre = "Ma première application wxPython"
# Taille de la fenêtre : 300x200 pixels
frame = wx.Frame(None, wx.ID_ANY, "Ma première application wxPython", size=(300, 200))

# --- Création d'un panneau (container pour les widgets) ---
# wx.Panel est nécessaire pour accueillir les widgets dans la fenêtre
panel = wx.Panel(frame, wx.ID_ANY)

# --- Ajout d'un champ de texte (non éditable) ---
# wx.TextCtrl(parent, id, valeur_initiale, style)
# wx.TE_READONLY : empêche la modification par l'utilisateur
text_ctrl = wx.TextCtrl(panel, wx.ID_ANY, "Bonjour, wxPython!", style=wx.TE_READONLY)

# --- Gestion de l'agencement des widgets (layout) ---
# wx.BoxSizer(wx.VERTICAL) : agencement vertical (du haut vers le bas)
sizer = wx.BoxSizer(wx.VERTICAL)

# Ajout du champ texte au sizer :
# - proportion 1 (prend toute la place disponible)
# - options : wx.EXPAND (prend toute la largeur), wx.ALL (marges sur les 4 côtés)
# - marge de 10 pixels
sizer.Add(text_ctrl, 1, wx.EXPAND | wx.ALL, 10)

# Affecte le sizer au panneau pour organiser l'affichage
panel.SetSizer(sizer)

# --- Affichage de la fenêtre ---
frame.Show(True)  # Affiche la fenêtre

# --- Lancement de la boucle d'événements ---
# MainLoop() : boucle principale, gère les événements GUI (clics, saisie, etc.)
app.MainLoop()  # Bloque l’exécution jusqu’à fermeture de la fenêtre
