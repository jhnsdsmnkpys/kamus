#Boa:Frame:Frame2

import wx, MySQLdb, MainKamus
conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="kamus")

kursor = conn.cursor()

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BACKGROUND, wxID_FRAME2BTN_BERSIH, 
 wxID_FRAME2BTN_HAPUS, wxID_FRAME2BTN_PROSES, wxID_FRAME2BTN_SIMPAN, 
 wxID_FRAME2BTN_UPDATE, wxID_FRAME2DATEPICKERCTRL1, wxID_FRAME2LC, 
 wxID_FRAME2NOTEBOOK1, wxID_FRAME2NOTEBOOK2, wxID_FRAME2PANEL1, 
 wxID_FRAME2PANEL2, wxID_FRAME2PANEL3, wxID_FRAME2RINDONESIA, 
 wxID_FRAME2RJEPANG, wxID_FRAME2STATICBITMAP1, wxID_FRAME2STATICBITMAP2, 
 wxID_FRAME2STATICTEXT1, wxID_FRAME2STATICTEXT2, wxID_FRAME2STATICTEXT3, 
 wxID_FRAME2STATICTEXT4, wxID_FRAME2STATICTEXT5, wxID_FRAME2TOOLBAR1, 
 wxID_FRAME2TXT_INDO, wxID_FRAME2TXT_INPUT, wxID_FRAME2TXT_JEPANG, 
 wxID_FRAME2TXT_TERJEMAHAN, 
] = [wx.NewId() for _init_ctrls in range(28)]

[wxID_FRAME2TOOLBAR1TOOLS0] = [wx.NewId() for _init_coll_toolBar1_Tools in range(1)]

class Frame2(wx.Frame):
    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'D:/kamus/gambar/home2.jpg',
              wx.BITMAP_TYPE_JPEG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME2TOOLBAR1TOOLS0, kind=wx.ITEM_NORMAL, label='',
              longHelp='', shortHelp='Main Kamus')
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Tools0Tool,
              id=wxID_FRAME2TOOLBAR1TOOLS0)

        parent.Realize()

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel2, select=True, text='Menu')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Administrator')

    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Jepang',
              width=500)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Indonesia', width=500)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1296, 776),
              style=wx.DEFAULT_FRAME_STYLE, title='Translate Jepang Indonesia')
        self.SetClientSize(wx.Size(1280, 738))
        self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'Tahoma'))

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1280, 738),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(0, 0, 128))

        self.notebook1 = wx.Notebook(id=wxID_FRAME2NOTEBOOK1, name='notebook1',
              parent=self.panel1, pos=wx.Point(144, 120), size=wx.Size(1064,
              584), style=wx.NB_LEFT)
        self.notebook1.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC, wx.BOLD, False,
              'Jokerman'))

        self.panel2 = wx.Panel(id=wxID_FRAME2PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1026,
              576), style=wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.panel3 = wx.Panel(id=wxID_FRAME2PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1026,
              576), style=wx.TAB_TRAVERSAL)
        self.panel3.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.panel3.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC, wx.BOLD, False,
              'Jokerman'))

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Kamus Jepang - Indonesia', name='staticText1',
              parent=self.panel1, pos=wx.Point(504, 48), size=wx.Size(317, 42),
              style=0)
        self.staticText1.SetBackgroundColour(wx.Colour(178, 178, 178))
        self.staticText1.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.BOLD, True,
              'Mistral'))
        self.staticText1.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)

        self.background = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/kamus/gambar/background kamus jepang.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME2BACKGROUND, name='background',
              parent=self.panel2, pos=wx.Point(-176, 0), size=wx.Size(1920,
              1080), style=0)

        self.notebook2 = wx.Notebook(id=wxID_FRAME2NOTEBOOK2, name='notebook2',
              parent=self.background, pos=wx.Point(256, 56), size=wx.Size(840,
              328), style=wx.RAISED_BORDER)

        self.rIndonesia = wx.RadioButton(id=wxID_FRAME2RINDONESIA,
              label='Indonesia - Jepang', name='rIndonesia',
              parent=self.notebook2, pos=wx.Point(80, 32), size=wx.Size(192,
              24), style=0)
        self.rIndonesia.SetValue(True)

        self.rJepang = wx.RadioButton(id=wxID_FRAME2RJEPANG,
              label='Jepang - Indonesia', name='rJepang', parent=self.notebook2,
              pos=wx.Point(568, 32), size=wx.Size(192, 24), style=0)
        self.rJepang.SetValue(True)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/kamus/gambar/icon indo.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self.notebook2, pos=wx.Point(136,
              64), size=wx.Size(53, 33), style=0)

        self.staticBitmap2 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/kamus/gambar/icon jeapng.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME2STATICBITMAP2,
              name='staticBitmap2', parent=self.notebook2, pos=wx.Point(632,
              64), size=wx.Size(53, 36), style=0)

        self.txt_terjemahan = wx.TextCtrl(id=wxID_FRAME2TXT_TERJEMAHAN,
              name='txt_terjemahan', parent=self.notebook2, pos=wx.Point(184,
              184), size=wx.Size(480, 32), style=0, value='')
        self.txt_terjemahan.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.txt_terjemahan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Arial'))

        self.txt_input = wx.TextCtrl(id=wxID_FRAME2TXT_INPUT, name='txt_input',
              parent=self.notebook2, pos=wx.Point(184, 120), size=wx.Size(480,
              32), style=0, value='')
        self.txt_input.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.txt_input.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Arial'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='Terjemahan', name='staticText2', parent=self.notebook2,
              pos=wx.Point(16, 184), size=wx.Size(106, 24), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='Masukan Kata', name='staticText3', parent=self.notebook2,
              pos=wx.Point(16, 120), size=wx.Size(124, 24), style=0)

        self.btn_proses = wx.Button(id=wxID_FRAME2BTN_PROSES, label='Proses',
              name='btn_proses', parent=self.notebook2, pos=wx.Point(224, 240),
              size=wx.Size(101, 35), style=0)
        self.btn_proses.Bind(wx.EVT_BUTTON, self.OnBtn_prosesButton,
              id=wxID_FRAME2BTN_PROSES)

        self.btn_bersih = wx.Button(id=wxID_FRAME2BTN_BERSIH, label='Bersih',
              name='btn_bersih', parent=self.notebook2, pos=wx.Point(520, 240),
              size=wx.Size(104, 35), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAME2BTN_BERSIH)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_FRAME2DATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self.panel1, pos=wx.Point(1176,
              48), size=wx.Size(88, 24), style=wx.DP_SHOWCENTURY)

        self.lc = wx.ListCtrl(id=wxID_FRAME2LC, name='lc', parent=self.panel3,
              pos=wx.Point(8, 280), size=wx.Size(1008, 292),
              style=wx.LC_REPORT)
        self.lc.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Arial Narrow'))
        self._init_coll_lc_Columns(self.lc)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLcListItemSelected,
              id=wxID_FRAME2LC)

        self.staticText4 = wx.StaticText(id=wxID_FRAME2STATICTEXT4,
              label='Indonesia', name='staticText4', parent=self.panel3,
              pos=wx.Point(40, 56), size=wx.Size(86, 24), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME2STATICTEXT5,
              label='Jepang', name='staticText5', parent=self.panel3,
              pos=wx.Point(48, 160), size=wx.Size(68, 24), style=0)

        self.txt_indo = wx.TextCtrl(id=wxID_FRAME2TXT_INDO, name='txt_indo',
              parent=self.panel3, pos=wx.Point(176, 40), size=wx.Size(680, 64),
              style=wx.TE_MULTILINE, value='')
        self.txt_indo.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Arial'))

        self.txt_jepang = wx.TextCtrl(id=wxID_FRAME2TXT_JEPANG,
              name='txt_jepang', parent=self.panel3, pos=wx.Point(176, 152),
              size=wx.Size(680, 64), style=wx.TE_MULTILINE, value='')
        self.txt_jepang.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Arial'))

        self.btn_simpan = wx.Button(id=wxID_FRAME2BTN_SIMPAN, label='Simpan',
              name='btn_simpan', parent=self.panel3, pos=wx.Point(880, 56),
              size=wx.Size(106, 35), style=0)
        self.btn_simpan.Bind(wx.EVT_BUTTON, self.OnBtn_simpanButton,
              id=wxID_FRAME2BTN_SIMPAN)

        self.btn_hapus = wx.Button(id=wxID_FRAME2BTN_HAPUS, label='Hapus',
              name='btn_hapus', parent=self.panel3, pos=wx.Point(880, 112),
              size=wx.Size(105, 35), style=0)
        self.btn_hapus.Bind(wx.EVT_BUTTON, self.OnBtn_hapusButton,
              id=wxID_FRAME2BTN_HAPUS)

        self.btn_update = wx.Button(id=wxID_FRAME2BTN_UPDATE, label='Update',
              name='btn_update', parent=self.panel3, pos=wx.Point(880, 168),
              size=wx.Size(105, 35), style=0)
        self.btn_update.Bind(wx.EVT_BUTTON, self.OnBtn_updateButton,
              id=wxID_FRAME2BTN_UPDATE)

        self.toolBar1 = wx.ToolBar(id=wxID_FRAME2TOOLBAR1, name='toolBar1',
              parent=self.panel1, pos=wx.Point(0, 0), size=wx.Size(1280, 41),
              style=wx.TB_HORIZONTAL | wx.NO_BORDER)

        self._init_coll_notebook1_Pages(self.notebook1)
        self._init_coll_toolBar1_Tools(self.toolBar1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.isilist()
    
    def bersih(self):
        self.txt_indo.SetValue("")
        self.txt_jepang.SetValue("")
        self.txt_indo.SetFocus()
    
    def isilist(self):
        self.lc.DeleteAllItems()
        sql = "select * from translate order by indonesia"
        kursor.execute(sql)
        hasil = kursor.fetchall()
        baris = self.lc.GetItemCount()
        
        for i in hasil:
            self.lc.InsertStringItem(baris,"%s"%i[0])
            self.lc.SetStringItem(baris,1,"%s"%i[1])
            baris = baris + 1

    def OnBtn_simpanButton(self, event):
        if self.txt_indo.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text Indonesia masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        elif self.txt_jepang.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text jepang masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        else:
            
            sql = "select * from translate where indonesia ='%s'"\
            %(self.txt_indo.GetValue())
        
            kursor.execute(sql)
            hasil=kursor.fetchall()
            if kursor.rowcount > 0:
                sql1 = "update translate set jepang = '%s' where indonesia ='%s'"\
                %(self.txt_jepang.GetValue(),self.txt_indo.GetValue())
                kursor.execute(sql1)
                conn.commit()
        
            else:
                sql1 = "insert into translate (indonesia,jepang) values ('%s','%s')"\
                %(self.txt_indo.GetValue(),self.txt_jepang.GetValue())
                kursor.execute(sql1)
                conn.commit()
                self.pesan=wx.MessageDialog(self,"Berhasil Menyimpan","Info",wx.OK)
                self.pesan.ShowModal()
                self.isilist()
                self.bersih()

    def OnBtn_hapusButton(self, event):
        sql1 = "delete from translate where indonesia ='%s'"\
        %(self.txt_indo.GetValue())
        
        kursor.execute(sql1)
        conn.commit()
        self.pesan=wx.MessageDialog(self,"Berhasil Menghapus","Info",wx.OK)
        self.pesan.ShowModal()
        self.isilist()
        self.bersih()
        
    def OnBtn_updateButton(self, event):
        self.isilist()
        self.bersih()

    def OnLcListItemSelected(self, event):
        self.a = event.m_itemIndex
        ind = self.lc.GetItem(self.a,0).GetText()
        self.txt_indo.SetValue(ind)
        jpg = self.lc.GetItem(self.a,1).GetText()
        self.txt_jepang.SetValue(jpg)
#------------------------------------------------------------------------------#
    def bersih2(self):
        self.txt_input.SetValue("")
        self.txt_terjemahan.SetValue("")
        self.txt_input.SetFocus()
            
    def OnBtn_prosesButton(self, event):
        if self.rIndonesia.Value == True:
            
            sql = "select * from translate where Indonesia ='%s'\
            "%(self.txt_input.GetValue())
            
            kursor.execute(sql)
            
            if kursor.rowcount > 0:
                hasil = kursor.fetchall()
                
                for i in hasil:
                    self.txt_terjemahan.SetValue(i[1])
                    
            else:
                self.pesan = wx.MessageDialog(self, "terjemahan kata"\
                +" "+self.txt_input.GetValue()+" "+ "tidak ada","Informasi",wx.OK)
                    
                self.pesan.ShowModal()
                
        else:
                
            sql = "select * from translate where jepang ='%s'\
                "%(self.txt_input.GetValue())
            kursor.execute(sql)
                
            if kursor.rowcount > 0:
                    
                hasil = kursor.fetchall()
                    
                for i in hasil:
                        
                    self.txt_terjemahan.SetValue(i[0])
            else:
                    self.pesan = wx.MessageDialog(self, "terjemahkan kata"\
                    +" "+self.txt_input.GetValue()+" "+ "tidak ada","Informasi",wx.OK)
                    
                    self.pesan.ShowModal()


    def OnBtn_bersihButton(self, event):
        self.bersih2()

    def OnToolBar1Tools0Tool(self, event):
        self.main = MainKamus.create(None)
        self.main.Show()
        self.Close()