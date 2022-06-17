#Boa:Frame:Frame2

import wx, MySQLdb, MainKamus

conn = MySQLdb.connect(host="localhost",user="root",passwd="",db ="kamus")

kursor = conn.cursor()

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BTN_BERSIH2, wxID_FRAME2DATEPICKERCTRL1, 
 wxID_FRAME2LC, wxID_FRAME2NOTEBOOK1, wxID_FRAME2PANEL1, wxID_FRAME2PANEL2, 
 wxID_FRAME2PANEL3, wxID_FRAME2RADIOBUTTON1, wxID_FRAME2RINGGRIS, 
 wxID_FRAME2STATICLINE1, wxID_FRAME2STATICTEXT1, wxID_FRAME2STATICTEXT2, 
 wxID_FRAME2STATICTEXT3, wxID_FRAME2STATICTEXT4, wxID_FRAME2STATICTEXT5, 
 wxID_FRAME2TMBBERSIH, wxID_FRAME2TMBHAPUS, wxID_FRAME2TMBSIMPAN, 
 wxID_FRAME2TMBTERJEMAHKAN, wxID_FRAME2TOOLBAR1, wxID_FRAME2TXT_IGG, 
 wxID_FRAME2TXT_IND, wxID_FRAME2TXT_KATA, wxID_FRAME2TXT_TERJEMAHAN, 
] = [wx.NewId() for _init_ctrls in range(25)]

[wxID_FRAME2TOOLBAR1TOOLS0] = [wx.NewId() for _init_coll_toolBar1_Tools in range(1)]

class Frame2(wx.Frame):
    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'D:/kamus/gambar/home.jpg',
              wx.BITMAP_TYPE_JPEG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME2TOOLBAR1TOOLS0, kind=wx.ITEM_NORMAL, label='',
              longHelp='', shortHelp='Main Kamus')
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Tools0Tool,
              id=wxID_FRAME2TOOLBAR1TOOLS0)

        parent.Realize()

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel2, select=True, text='Kamus')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Input Data')

    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Inggris', width=270)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Indonesia', width=270)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1296, 776),
              style=wx.DEFAULT_FRAME_STYLE, title='Kamus Inggris - Indonesia')
        self.SetClientSize(wx.Size(1280, 738))
        self.SetFont(wx.Font(16, wx.SWISS, wx.ITALIC, wx.BOLD, False,'Vivaldi'))

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1280, 738),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Kamus Inggris - Indonesia', name='staticText1',
              parent=self.panel1, pos=wx.Point(400, 64), size=wx.Size(446, 57),
              style=0)
        self.staticText1.SetFont(wx.Font(26, wx.SWISS, wx.ITALIC, wx.BOLD,
              False, 'Viner Hand ITC'))

        self.notebook1 = wx.Notebook(id=wxID_FRAME2NOTEBOOK1, name='notebook1',
              parent=self.panel1, pos=wx.Point(0, 152), size=wx.Size(1368, 576),
              style=0)
        self.notebook1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.notebook1.SetForegroundColour(wx.Colour(255, 255, 255))

        self.panel2 = wx.Panel(id=wxID_FRAME2PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1360,
              538), style=wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(0, 255, 255))

        self.panel3 = wx.Panel(id=wxID_FRAME2PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1360,
              538), style=wx.TAB_TRAVERSAL)
        self.panel3.SetBackgroundColour(wx.Colour(29, 29, 29))

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='  Inggris', name='staticText2', parent=self.panel3,
              pos=wx.Point(16, 64), size=wx.Size(87, 25), style=0)
        self.staticText2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='Indonesia', name='staticText3', parent=self.panel3,
              pos=wx.Point(24, 176), size=wx.Size(104, 25), style=0)
        self.staticText3.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.txt_igg = wx.TextCtrl(id=wxID_FRAME2TXT_IGG, name='txt_igg',
              parent=self.panel3, pos=wx.Point(168, 64), size=wx.Size(368, 32),
              style=0, value='')
        self.txt_igg.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Arial'))
        self.txt_igg.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_iggTextEnter,
              id=wxID_FRAME2TXT_IGG)

        self.txt_ind = wx.TextCtrl(id=wxID_FRAME2TXT_IND, name='txt_ind',
              parent=self.panel3, pos=wx.Point(168, 168), size=wx.Size(368, 37),
              style=0, value='')
        self.txt_ind.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Arial'))

        self.tmbSimpan = wx.Button(id=wxID_FRAME2TMBSIMPAN, label='Simpan',
              name='tmbSimpan', parent=self.panel3, pos=wx.Point(176, 272),
              size=wx.Size(96, 40), style=0)
        self.tmbSimpan.Bind(wx.EVT_BUTTON, self.OnTmbSimpanButton,
              id=wxID_FRAME2TMBSIMPAN)

        self.tmbBersih = wx.Button(id=wxID_FRAME2TMBBERSIH, label='Bersih',
              name='tmbBersih', parent=self.panel3, pos=wx.Point(312, 272),
              size=wx.Size(91, 40), style=0)
        self.tmbBersih.Bind(wx.EVT_BUTTON, self.OnTmbBersihButton,
              id=wxID_FRAME2TMBBERSIH)

        self.tmbHapus = wx.Button(id=wxID_FRAME2TMBHAPUS, label='Hapus',
              name='tmbHapus', parent=self.panel3, pos=wx.Point(448, 272),
              size=wx.Size(91, 40), style=0)
        self.tmbHapus.Bind(wx.EVT_BUTTON, self.OnTmbHapusButton,
              id=wxID_FRAME2TMBHAPUS)

        self.lc = wx.ListCtrl(id=wxID_FRAME2LC, name='lc', parent=self.panel3,
              pos=wx.Point(664, 16), size=wx.Size(600, 400),
              style=wx.LC_REPORT)
        self.lc.SetFont(wx.Font(16, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              'MS Sans Serif'))
        self._init_coll_lc_Columns(self.lc)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLcListItemSelected,
              id=wxID_FRAME2LC)

        self.rInggris = wx.RadioButton(id=wxID_FRAME2RINGGRIS,
              label='Inggris - Indonesia', name='rInggris', parent=self.panel2,
              pos=wx.Point(208, 40), size=wx.Size(192, 24), style=0)
        self.rInggris.SetValue(True)
        self.rInggris.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.BOLD, True,
              'Modern No. 20'))

        self.radioButton1 = wx.RadioButton(id=wxID_FRAME2RADIOBUTTON1,
              label='Indonesia - Inggris', name='radioButton1',
              parent=self.panel2, pos=wx.Point(896, 40), size=wx.Size(248, 24),
              style=0)
        self.radioButton1.SetValue(False)
        self.radioButton1.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.BOLD,
              True, 'Modern No. 20'))

        self.staticText4 = wx.StaticText(id=wxID_FRAME2STATICTEXT4,
              label='Masukan Kata Yang Ingin Diterjemahkan', name='staticText4',
              parent=self.panel2, pos=wx.Point(472, 144), size=wx.Size(342, 25),
              style=0)
        self.staticText4.SetFont(wx.Font(16, wx.SWISS, wx.ITALIC, wx.BOLD,
              False, 'Arial Narrow'))

        self.txt_kata = wx.TextCtrl(id=wxID_FRAME2TXT_KATA, name='txt_kata',
              parent=self.panel2, pos=wx.Point(440, 216), size=wx.Size(408, 34),
              style=0, value='')
        self.txt_kata.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Arial'))

        self.txt_terjemahan = wx.TextCtrl(id=wxID_FRAME2TXT_TERJEMAHAN,
              name='txt_terjemahan', parent=self.panel2, pos=wx.Point(440, 360),
              size=wx.Size(408, 34), style=0, value='')
        self.txt_terjemahan.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Arial'))

        self.staticText5 = wx.StaticText(id=wxID_FRAME2STATICTEXT5,
              label='Terjemahan', name='staticText5', parent=self.panel2,
              pos=wx.Point(576, 328), size=wx.Size(115, 26), style=0)
        self.staticText5.SetFont(wx.Font(16, wx.SWISS, wx.ITALIC, wx.BOLD,
              False, 'Bradley Hand ITC'))

        self.tmbTerjemahkan = wx.Button(id=wxID_FRAME2TMBTERJEMAHKAN,
              label='Terjemahkan', name='tmbTerjemahkan', parent=self.panel2,
              pos=wx.Point(552, 416), size=wx.Size(168, 36), style=0)
        self.tmbTerjemahkan.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Segoe Script'))
        self.tmbTerjemahkan.Bind(wx.EVT_BUTTON, self.OnTmbTerjemahkanButton,
              id=wxID_FRAME2TMBTERJEMAHKAN)

        self.btn_bersih2 = wx.Button(id=wxID_FRAME2BTN_BERSIH2, label='Bersih',
              name='btn_bersih2', parent=self.panel2, pos=wx.Point(592, 464),
              size=wx.Size(80, 36), style=0)
        self.btn_bersih2.Bind(wx.EVT_BUTTON, self.OnBtn_bersih2Button,
              id=wxID_FRAME2BTN_BERSIH2)

        self.toolBar1 = wx.ToolBar(id=wxID_FRAME2TOOLBAR1, name='toolBar1',
              parent=self.panel1, pos=wx.Point(0, 0), size=wx.Size(1280, 52),
              style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.toolBar1.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME2STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(8, 130),
              size=wx.Size(1264, 2), style=0)
        self.staticLine1.SetBackgroundColour(wx.Colour(237, 230, 251))

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_FRAME2DATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self.panel1, pos=wx.Point(1128, 8),
              size=wx.Size(128, 24), style=wx.DP_SHOWCENTURY)

        self._init_coll_notebook1_Pages(self.notebook1)
        self._init_coll_toolBar1_Tools(self.toolBar1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Isi_List()
        
    def Isi_List(self):
        self.lc.DeleteAllItems()
        sql = "select * from kata order by Inggris"
        
        kursor.execute(sql)
        hasil = kursor.fetchall()
        baris = self.lc.GetItemCount()
        
        for i in hasil:
            self.lc.InsertStringItem(baris,"%s"%i[0])
            self.lc.SetStringItem(baris,1,"%s"%i[1])
            
            baris =baris + 1

    def OnTmbSimpanButton(self, event):
        if self.txt_igg.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text Inggris masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
            self.Bersih()
        elif self.txt_ind.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text Indonesia masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
            self.Bersih()
        else:
            sql = "select * from kata where Inggris ='%s'"\
            %(self.txt_igg.GetValue())
        
            kursor.execute(sql)
        
            hasil = kursor.fetchall()
            if kursor.rowcount > 0:
                sql1 = "update kata set Indonesia = '%s' where Inggris ='%s'"\
                %(self.txt_ind.GetValue(),self.txt_igg.GetValue())
            
                kursor.execute(sql1)
            
                conn.commit()
            else:
                sql1 = "Insert into kata (Inggris,Indonesia) values ('%s','%s')\
                "%(self.txt_igg.GetValue(),self.txt_ind.GetValue())
            
                kursor.execute(sql1)
            
                conn.commit()
        
            self.Bersih()
            self.Isi_List()
            self.pesan = wx.MessageDialog(self,"Berhasi Menyimpan","Info",wx.OK)
            self.pesan.ShowModal()
        
    def Bersih(self):
        self.txt_igg.SetValue("")
        self.txt_ind.SetValue("")
        self.txt_igg.SetFocus()

    def OnTmbBersihButton(self, event):
        self.Bersih()

    def OnTmbHapusButton(self, event):
        sql1 = "delete from kata where Inggris ='%s'\
        "%(self.txt_igg.GetValue())
        
        kursor.execute(sql1)
        
        conn.commit()
        
        self.Bersih()
        self.Isi_List()
        self.pesan = wx.MessageDialog(self,"Berhasil MengHapus","Info",wx.OK)
        self.pesan.ShowModal()

    def OnLcListItemSelected(self, event):
        self.a = event.m_itemIndex
        
        md1 = self.lc.GetItem(self.a,0).GetText()
        self.txt_igg.SetValue(md1)
        
        ing1 = self.lc.GetItem(self.a,1).GetText()
        self.txt_ind.SetValue(ing1)

    def OnTxt_iggTextEnter(self, event):
        sql = "select * from kata where madura ='%s'\
        "%(self.txt_madura.GetValue())
        
        kursor.execute(sql)
        
        if kursor.rowcount > 0:
            hasil = kursor.fetchall()
            
            for i in hasil:
                self.txt_ind.SetValue(i[1])
        else:
            
            self.pesan = wx.MessageDialog(self, "Terjemahan kata"+self.txt_ind.GetValue()\
            +"tidak ada","Informasi",wx.OK)
            
            self.pesan.Show.Modal()
    
    def bersih2(self):
        self.txt_kata.SetValue("")
        self.txt_terjemahan.SetValue("")
        self.txt_kata.SetFocus()

    
    def OnTmbTerjemahkanButton(self, event):
        if self.rInggris.Value == True:
            
            sql = "select * from kata where Inggris ='%s'\
            "%(self.txt_kata.GetValue())
            
            kursor.execute(sql)
            
            if kursor.rowcount > 0:
                hasil = kursor.fetchall()
                
                for i in hasil:
                    self.txt_terjemahan.SetValue(i[1])
                    
            else:
                self.pesan = wx.MessageDialog(self, "terjemahan kata"\
                +" "+self.txt_kata.GetValue()+" "+ "tidak ada","Informasi",wx.OK)
                    
                self.pesan.ShowModal()
                self.bersih2()
                
        else:
                
            sql = "select * from kata where indonesia ='%s'\
                "%(self.txt_kata.GetValue())
            kursor.execute(sql)
                
            if kursor.rowcount > 0:
                    
                hasil = kursor.fetchall()
                    
                for i in hasil:
                        
                    self.txt_terjemahan.SetValue(i[0])
            else:
                    self.pesan = wx.MessageDialog(self, "terjemahkan kata"\
                    +" "+self.txt_kata.GetValue()+" "+ "tidak ada","Informasi",wx.OK)
                    
                    self.pesan.ShowModal()
                    self.bersih2()

    def OnBtn_bersih2Button(self, event):
        self.bersih2()

    def OnToolBar1Tools0Tool(self, event):
        self.main = MainKamus.create(None)
        self.main.Show()
        self.Close()
