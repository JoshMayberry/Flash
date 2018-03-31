import wx
 
class MyTree(wx.TreeCtrl):
 
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
 
 
class TreePanel(wx.Panel):
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
 
        self.tree = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                           wx.TR_HAS_BUTTONS)    
 
        self.root = self.tree.AddRoot('Something goes here')
        self.tree.SetPyData(self.root, ('key', 'value'))
        os = self.tree.AppendItem(self.root, 'Operating Systems')
        os = self.tree.AppendItem(os, 'Lorem Systems')
        self.tree.Expand(self.root)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)
 
 
class MainFrame(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='TreeCtrl Demo')
        panel = TreePanel(self)
        self.Show()
 
 
if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()