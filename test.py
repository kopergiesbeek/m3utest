import os
import wx

import wx.lib.agw.multidirdialog as MDD

# Our normal wxApp-derived class, as usual
app = wx.App(0)

dlg = MDD.MultiDirDialog(None, title="Custom MultiDirDialog", defaultPath=os.getcwd(),
                         agwStyle=MDD.DD_MULTIPLE|MDD.DD_DIR_MUST_EXIST)

if dlg.ShowModal() != wx.ID_OK:
    print("You Cancelled The Dialog!")
    dlg.Destroy()
    

paths = dlg.GetPaths()
for indx, path in enumerate(paths):
    print("Path %d: %s"%(indx+1, path))

dlg.Destroy()

app.MainLoop()

en nu een regel
en nog een regel
# 