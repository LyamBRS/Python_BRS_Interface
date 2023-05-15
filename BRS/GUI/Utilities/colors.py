#====================================================================#
# File Information
#====================================================================#
"""_summary_
    This file contains GUI color classes. Such as statesColors or
    UIcolors.

    The classes contained in this file are references only. Do not
    construct them
"""
#====================================================================#
# Imports
#====================================================================#
from ...Debug.LoadingLog import LoadingLog
from ...Debug.consoleLog import Debug
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
LoadingLog.Start("colors.py")

#====================================================================#
# Functions
#====================================================================#
def GetAccentColor(variant:str = "500") -> None:
    """
        GetAccentColor:
        ===============
        Summary:
        --------
        This function returns the accent color
        of the application.

        Returns:
        --------
        - (0,0,0) to (1,1,1)
    """
    Debug.Start("GetAccentColor")

    try:
        color = MDApp.get_running_app().theme_cls.accent_palette
        color = get_color_from_hex(colors[color][variant])
    except:
        Debug.Error("Failed to get accent color.")
        Debug.Log("Returning red")
        color = (1,0,0)
    Debug.End()
    return color

#====================================================================#
# Classes
#====================================================================#
class GUIColors:
    #region   --------------------------- DOCSTRING
    '''
        This is a reference style class which means you should only reference
        it and get data from it. See it like an enum in C#.

        This class contains the colors used for standard GUI applications.
        - Window Color
        - Card Color
    '''
    #endregion
    #region   --------------------------- MEMBERS
    Card = (255/255., 255/255., 255/255., 1.)
    '''RGBA color to use with Card layouts'''

    CardShadow = (0,0,0,1.)
    """RGBA color used for the cards layouts shadows."""

    Window = (255/255., 255/255., 255/255., 1.)
    """RGBA color used as the application's background color."""
    #endregion
    #region   --------------------------- METHODS
    #endregion
    #region   --------------------------- CONSTRUCTOR
    #endregion
    pass

LoadingLog.End("colors.py")