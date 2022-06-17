#Boa:Frame:Frame1

import wx, MySQLdb, MainKamus

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="kamus")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_BACK, wxID_FRAME1BTN_KIRIM, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICTEXT1, wxID_FRAME1TXT_NAMA, 
 wxID_FRAME1TXT_SARAN, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(-2, 3), size=wx.Size(920, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='Tentang Program')
        self.SetClientSize(wx.Size(904, 412))
        self.SetWindowVariant(wx.WINDOW_VARIANT_NORMAL)
        self.SetMaxSize(wx.Size(920, 450))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(904, 412),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='                         Program Ini Dibuat Dalam Bentuk Pembelajaran\n                                                                Dan\n                                     Bebas digunakan oleh siapa saja \n\n\n\n  Tentang Program \n\n  Tanggal dibuat  : 06 - Oktober - 2017\n\n  Bahasa Pemograman : Python\n\n  library : wx, MySQLdb\n\n\n\n\n\n\n``````````````````````````````````````````````````````````````JhnsDsmn__\n\n',
              name='staticText1', parent=self.panel1, pos=wx.Point(8, 8),
              size=wx.Size(592, 396), style=0)
        self.staticText1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.staticText1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='Kritik Atau Saran', name='staticBox1', parent=self.panel1,
              pos=wx.Point(608, 8), size=wx.Size(288, 392), style=0)
        self.staticBox1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tempus Sans ITC'))

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(624, 72), size=wx.Size(256, 37),
              style=0, value='Nama..')
        self.txt_nama.SetToolTipString('Masukan Nama Anda')
        self.txt_nama.Bind(wx.EVT_SET_FOCUS, self.OnTxt_namaSetFocus)

        self.txt_saran = wx.TextCtrl(id=wxID_FRAME1TXT_SARAN, name='txt_saran',
              parent=self.panel1, pos=wx.Point(616, 128), size=wx.Size(272,
              208), style=0, value='Kritik dan Saran..')
        self.txt_saran.SetToolTipString('Kritik dan Saran')
        self.txt_saran.Bind(wx.EVT_SET_FOCUS, self.OnTxt_saranSetFocus)

        self.btn_kirim = wx.Button(id=wxID_FRAME1BTN_KIRIM, label='Kirim',
              name='btn_kirim', parent=self.panel1, pos=wx.Point(808, 352),
              size=wx.Size(75, 31), style=0)
        self.btn_kirim.Bind(wx.EVT_BUTTON, self.OnBtn_kirimButton,
              id=wxID_FRAME1BTN_KIRIM)

        self.btn_back = wx.BitmapButton(bitmap=wx.Bitmap(u'D:/kamus/gambar/back.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1BTN_BACK, name='btn_back',
              parent=self.panel1, pos=wx.Point(616, 352), size=wx.Size(72, 40),
              style=wx.BU_AUTODRAW)
        self.btn_back.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_back.SetToolTipString('Kembali')
        self.btn_back.Bind(wx.EVT_BUTTON, self.OnBtn_backButton,
              id=wxID_FRAME1BTN_BACK)

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    def bersih(self):
        self.txt_nama.SetValue("")
        self.txt_saran.SetValue("")
        self.txt_nama.SetFocus()
        
    def OnBtn_kirimButton(self, event):
        if self.txt_nama.GetValue()== "":
            self.pesan = wx.MessageDialog(self,"Nama Anda Belum Diisi","Informasi",wx.OK)
            self.pesan.ShowModal()
            self.bersih()
        elif self.txt_saran.GetValue()== "":
            self.pesan = wx.MessageDialog(self,"Anda Belum Memberi Saran","Informasi",wx.OK)
            self.pesan.ShowModal()
            self.bersih()
        
        else:
            sql = "insert into TentangProgram values \
            ('%s','%s')"%(self.txt_nama.GetValue(),self.txt_saran.GetValue())
            cur.execute(sql)
            conn.commit()
            self.pesan = wx.MessageDialog(self,"Terimakasi Atas Saran Yang Anda Berikan Atas Program Ini :)","TerimaKasih",wx.OK)
            self.pesan.ShowModal()
            self.bersih()


    def OnTxt_namaSetFocus(self, event):
        self.txt_nama.SetValue("")

    def OnTxt_saranSetFocus(self, event):
        self.txt_saran.SetValue("")

    def OnBtn_backButton(self, event):
        self.main = MainKamus.create(None)
        self.main.Show()
        self.Close()

