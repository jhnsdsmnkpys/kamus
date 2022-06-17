#Boa:Frame:Frame1

import wx, Administrator,MainKamus

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BITMAPBUTTON1, wxID_FRAME1BTN_HOME, 
 wxID_FRAME1GUNUNG, wxID_FRAME1NOTEBOOK1, wxID_FRAME1PANEL1, 
 wxID_FRAME1PANEL2, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1TXT_PASSWORD, wxID_FRAME1TXT_USERNAME, 
] = [wx.NewId() for _init_ctrls in range(12)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(420, 101), size=wx.Size(400, 509),
              style=wx.DEFAULT_FRAME_STYLE, title='Login Administrator')
        self.SetClientSize(wx.Size(384, 471))
        self.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 471),
              style=wx.TAB_TRAVERSAL)

        self.gunung = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/kamus/gambar/background login.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1GUNUNG, name='gunung',
              parent=self.panel1, pos=wx.Point(-240, -80), size=wx.Size(1920,
              1080), style=0)

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self.gunung, pos=wx.Point(256, 264), size=wx.Size(352,
              200), style=wx.RAISED_BORDER)
        self.notebook1.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Halaman Login', name='staticText1', parent=self.panel1,
              pos=wx.Point(100, 32), size=wx.Size(194, 39), style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Viner Hand ITC'))
        self.staticText1.SetBackgroundColour(wx.Colour(204, 204, 255))

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(-8, -8), size=wx.Size(352,
              224), style=wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(255, 255, 164))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='UserName', name='staticText2', parent=self.panel2,
              pos=wx.Point(24, 48), size=wx.Size(78, 20), style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tempus Sans ITC'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Password', name='staticText3', parent=self.panel2,
              pos=wx.Point(24, 112), size=wx.Size(67, 20), style=0)
        self.staticText3.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tempus Sans ITC'))

        self.txt_username = wx.TextCtrl(id=wxID_FRAME1TXT_USERNAME,
              name='txt_username', parent=self.panel2, pos=wx.Point(120, 40),
              size=wx.Size(192, 32), style=0, value='')

        self.txt_password = wx.TextCtrl(id=wxID_FRAME1TXT_PASSWORD,
              name='txt_password', parent=self.panel2, pos=wx.Point(120, 104),
              size=wx.Size(192, 32), style=wx.TE_PASSWORD, value='')

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'D:/kamus/gambar/icon login.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BITMAPBUTTON1,
              name='bitmapButton1', parent=self.panel2, pos=wx.Point(272, 152),
              size=wx.Size(72, 48), style=wx.BU_AUTODRAW)
        self.bitmapButton1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bitmapButton1.SetToolTipString('Login Administrator')
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapButton1Button,
              id=wxID_FRAME1BITMAPBUTTON1)

        self.btn_home = wx.BitmapButton(bitmap=wx.Bitmap(u'D:/kamus/gambar/home4.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1BTN_HOME, name='btn_home',
              parent=self.panel2, pos=wx.Point(32, 160), size=wx.Size(64, 40),
              style=wx.BU_AUTODRAW)
        self.btn_home.SetToolTipString('MainKamus')
        self.btn_home.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_home.Bind(wx.EVT_BUTTON, self.OnBtn_homeButton,
              id=wxID_FRAME1BTN_HOME)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def bersih(self):
        self.txt_username.SetValue("")
        self.txt_password.SetValue("")
        self.txt_username.SetFocus()      

    def OnBitmapButton1Button(self, event):
        if self.txt_username.GetValue() == "johanesdesmonkapoyos" and \
        self.txt_password.GetValue() == "johanesdesmonkapoyos007":
            self.main = Administrator.create(None)
            self.main.Show()
            self.bersih()
            self.Close()
        else:
            self.pesan=wx.MessageDialog(self,"Username Atau Password Salah","Failed",wx.OK)
            self.pesan.ShowModal()
            self.bersih()            

    def OnBtn_homeButton(self, event):
        self.main = MainKamus.create(None)
        self.main.Show()
        self.Close()

