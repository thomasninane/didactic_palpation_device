########################################################################################################################
# IMPORTS
########################################################################################################################

import tkinter as tk

import GlobalConfig

LARGE_FONT = ("Verdana", 12)


########################################################################################################################
# CLASS: FILE CONTENT WINDOW
########################################################################################################################

class DataOutputWindow(tk.Tk):

    def __init__(self, root, parent):
        """
        Creates a window which displays the data contained in the data frame.
        The geometry of this window is set by GlobalConfig.OUTPUT_WINDOW_GEOMETRY.
        A horizontal scrollbar is also created as the data frame contains too many columns.
        """
        self.parent = parent

        self.root = root
        self.root.title("DATA OUTPUT")
        self.root.geometry(GlobalConfig.OUTPUT_WINDOW_GEOMETRY)

        # FRAME TITLE
        tk.Label(self.root, text="DATA OUTPUT WINDOW", font=LARGE_FONT, bg='red').pack(pady=5)

        # SELECTED FILE NAME
        if self.parent.real_time == 0:
            tk.Label(self.root, text=self.parent.selectedFileVar.get()).pack(pady=10)

        # OUTPUT FRAME (LOWER RIGHT)
        self.outputFrame = tk.LabelFrame(self.root, text="OUTPUT")
        self.outputFrame.pack(padx=10, pady=5)

        # OUTPUT TEXT (IN OUTPUT FRAME)
        self.outputText = tk.Text(self.outputFrame,
                                  width=GlobalConfig.OUTPUT_TEXT_WIDTH,
                                  height=GlobalConfig.OUTPUT_TEXT_HEIGHT,
                                  wrap=tk.NONE)
        self.outputText.pack(padx=10, pady=10)

        # PRINT FILE DATA TO OUTPUT FRAME
        self.outputText.delete(1.0, tk.END)
        string = self.parent.df.to_string(index=False, columns=GlobalConfig.DATA_FRAME_COLUMNS, col_space=8)
        self.outputText.insert(tk.END, string + "\n")

        # HORIZONTAL SCROLL BAR
        scroll_horizontal = tk.Scrollbar(self.outputFrame, orient=tk.HORIZONTAL)
        scroll_horizontal.config(command=self.outputText.xview)
        self.outputText.configure(xscrollcommand=scroll_horizontal.set)
        scroll_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

        # # VERTICAL SCROLL BAR
        # # DISPLAY BUG
        # scroll_vertical = tk.Scrollbar(self.outputFrame, orient=tk.VERTICAL)
        # scroll_vertical.config(command=self.outputText.yview)
        # self.outputText.configure(yscrollcommand=scroll_vertical.set)
        # scroll_vertical.pack(side=tk.RIGHT, fill=tk.Y)

        ################################################################################################################
        # END OF __INIT__
        ################################################################################################################

