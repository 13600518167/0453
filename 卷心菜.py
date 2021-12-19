
import wx
class MyFrname(wx.Frame):
    def __init__(self,parnet,id):
        wx.Frame.__init__(self,parnet,id,title='卷心菜',pos=(100,100),size=(100000,100000))
        panel=wx.Panel(self)
        title=wx.StaticText(panel,label='卷心菜—章雷涛',pos=(10,20))
        font=wx.Font(16,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        title.SetFont(font)
        for i in range(40,1000,70):
            for j in range(50,1000,20):
                wx.StaticText(panel,label='卷心菜章雷涛',pos=(i,j))
if __name__=='__main__':
    app=wx.App()
    frame=MyFrname(parnet=None,id=-1)
    frame.Show()
    app.MainLoop()    