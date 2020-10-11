#!/usr/bin/env python
import wx
import images


class Hello(wx.Frame):
    def __init__(self, *args, **kw):
        super(Hello, self).__init__(*args, **kw)
        self.SetIcon(images.wxicon.Icon)

        panel = wx.Panel(self)
        stext = wx.StaticText(panel, label="こんにちは、世界！")
        font = stext.GetFont()
        font.PointSize = 24
        stext.SetFont(font)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(stext, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App()
    hello = Hello(None, title='wxPython edition')
    hello.Show()
    app.MainLoop()
