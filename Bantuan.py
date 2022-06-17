#Boa:Frame:Frame1

import wx, MySQLdb,MainKamus
import wx.lib.stattext
import wx.lib.masked.timectrl
import wx.lib.masked.textctrl

conn = MySQLdb.connect(host = "localhost", user="root", passwd="", db="kamus")
cur=conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_KIRIM, wxID_FRAME1LC_BALAS, wxID_FRAME1NOTEBOOK1, 
 wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1TOOLBAR1, wxID_FRAME1TXT_TANYA, 
] = [wx.NewId() for _init_ctrls in range(13)]

[wxID_FRAME1TOOLBAR1TOOLS0] = [wx.NewId() for _init_coll_toolBar1_Tools in range(1)]

class Frame1(wx.Frame):
    def _init_coll_lc_balas_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Balasan', width=600)

    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'D:/kamus/gambar/home3.jpg',
              wx.BITMAP_TYPE_JPEG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME1TOOLBAR1TOOLS0, kind=wx.ITEM_NORMAL, label='',
              longHelp='', shortHelp='MainKamus')
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Tools0Tool,
              id=wxID_FRAME1TOOLBAR1TOOLS0)

        parent.Realize()

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(259, 4), size=wx.Size(811, 595),
              style=wx.DEFAULT_FRAME_STYLE, title='Bantuan')
        self.SetClientSize(wx.Size(795, 557))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(795, 557),
              style=wx.TAB_TRAVERSAL)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('D://snow_snowflake_style_winter_background_glare_47385_1920x1080.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(-160, 48),
              size=wx.Size(1920, 800), style=0)

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self.staticBitmap1, pos=wx.Point(216, 40),
              size=wx.Size(696, 432), style=0)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(8, 8), size=wx.Size(680, 416),
              style=wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(183, 183, 255))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Tanya Kepada Admin', name='staticText1',
              parent=self.panel2, pos=wx.Point(24, 56), size=wx.Size(102, 13),
              style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Balasan Admin', name='staticText2', parent=self.panel2,
              pos=wx.Point(24, 200), size=wx.Size(70, 13), style=0)

        self.btn_kirim = wx.Button(id=wxID_FRAME1BTN_KIRIM, label='Kirim',
              name='btn_kirim', parent=self.panel2, pos=wx.Point(544, 176),
              size=wx.Size(75, 23), style=0)
        self.btn_kirim.Bind(wx.EVT_BUTTON, self.OnBtn_kirimButton,
              id=wxID_FRAME1BTN_KIRIM)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Menu Bantuan', name='staticText3', parent=self.panel2,
              pos=wx.Point(224, 8), size=wx.Size(212, 46), style=0)
        self.staticText3.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Curlz MT'))

        self.txt_tanya = wx.TextCtrl(id=wxID_FRAME1TXT_TANYA, name='txt_tanya',
              parent=self.panel2, pos=wx.Point(16, 72), size=wx.Size(640, 96),
              style=wx.TE_MULTILINE, value='')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='#Jangan Lupa Cantumkan Identitas Anda', name='staticText4',
              parent=self.panel2, pos=wx.Point(24, 168), size=wx.Size(235, 13),
              style=0)
        self.staticText4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, True,
              'Tahoma'))

        self.lc_balas = wx.ListCtrl(id=wxID_FRAME1LC_BALAS, name='lc_balas',
              parent=self.panel2, pos=wx.Point(16, 216), size=wx.Size(640, 168),
              style=wx.LC_REPORT)
        self._init_coll_lc_balas_Columns(self.lc_balas)

        self.toolBar1 = wx.ToolBar(id=wxID_FRAME1TOOLBAR1, name='toolBar1',
              parent=self.panel1, pos=wx.Point(0, 0), size=wx.Size(795, 48),
              style=wx.TB_HORIZONTAL | wx.NO_BORDER)

        self._init_coll_toolBar1_Tools(self.toolBar1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.tampil()
    

    def OnBtn_kirimButton(self, event):
        if self.txt_tanya.GetValue()== "":
            self.pesan = wx.MessageDialog(self,"Nama Anda Belum Diisi","Informasi",wx.OK)
            self.pesan.ShowModal()
        
        else:
            sql = "insert into pertanyaan values \
            ('%s')"%(self.txt_tanya.GetValue())
            cur.execute(sql)
            conn.commit()
            self.pesan = wx.MessageDialog(self,"Pertanyaaan Anda Sudah Terkirim ","Informasi",wx.OK)
            self.pesan.ShowModal()
            self.txt_tanya.SetValue("")
            self.txt_tanya.SetFocus()
    
    def tampil(self):
        sql = "select * from balasan"
        cur.execute(sql)
        hasil=cur.fetchall()
        k = self.lc_balas.GetItemCount()
       
        for i in hasil:
            self.lc_balas.InsertStringItem(k,"%s"%i[0])

    def OnToolBar1Tools0Tool(self, event):
        self.main = MainKamus.create(None)
        self.main.Show()
        self.Close()
