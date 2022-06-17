#Boa:Frame:Frame1

import wx, MySQLdb, framenotebook, Tentangprogram, Bantuan, KamusJepang, Login
import wx.lib.analogclock

conn=MySQLdb.connect(host="localhost", user="root", passwd="", db="kamus")

cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1ANALOGCLOCK1, wxID_FRAME1CARI_INGG, wxID_FRAME1LC, 
 wxID_FRAME1LC_INDO, wxID_FRAME1LC_INGG, wxID_FRAME1NOTEBOOK1, 
 wxID_FRAME1NOTEBOOK2, wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, 
 wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, wxID_FRAME1PANEL5, wxID_FRAME1PANEL6, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICBOX3, 
 wxID_FRAME1STATICBOX4, wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1TXTPENGERTIAN_INDO, wxID_FRAME1TXTPENGERTIAN_INGG, 
 wxID_FRAME1TXTSAMPLE_INDO, wxID_FRAME1TXTSAMPLE_INGG, 
 wxID_FRAME1TXT_CARIINDO, wxID_FRAME1TXT_ID, wxID_FRAME1TXT_ID_IG, 
 wxID_FRAME1TXT_ID_INGG, wxID_FRAME1TXT_KOSAKATA, wxID_FRAME1TXT_PENGERTIAN, 
 wxID_FRAME1TXT_SAMPLE, 
] = [wx.NewId() for _init_ctrls in range(34)]

[wxID_FRAME1ABOUTITEMS0, wxID_FRAME1ABOUTITEMS1, wxID_FRAME1ABOUTITEMS3, 
] = [wx.NewId() for _init_coll_About_Items in range(3)]

[wxID_FRAME1PYTHONTRANSLATEINDOINGG, wxID_FRAME1PYTHONTRANSLATEITEMS1, 
] = [wx.NewId() for _init_coll_PythonTranslate_Items in range(2)]

[wxID_FRAME1ADMINISTRATORITEMS0] = [wx.NewId() for _init_coll_Administrator_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_PythonTranslate_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1PYTHONTRANSLATEINDOINGG,
              kind=wx.ITEM_NORMAL, text='Translate Indonesia - Inggris')
        parent.Append(help='', id=wxID_FRAME1PYTHONTRANSLATEITEMS1,
              kind=wx.ITEM_NORMAL, text='Translate Indonesia - Jepang')
        self.Bind(wx.EVT_MENU, self.OnPythonTranslateIndoinggMenu,
              id=wxID_FRAME1PYTHONTRANSLATEINDOINGG)
        self.Bind(wx.EVT_MENU, self.OnPythonTranslateItems1Menu,
              id=wxID_FRAME1PYTHONTRANSLATEITEMS1)

    def _init_coll_Administrator_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1ADMINISTRATORITEMS0,
              kind=wx.ITEM_NORMAL, text='Masuk')
        self.Bind(wx.EVT_MENU, self.OnAdministratorItems0Menu,
              id=wxID_FRAME1ADMINISTRATORITEMS0)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.PythonTranslate, title='Python Translate')
        parent.Append(menu=self.Administrator, title='Administrator')
        parent.Append(menu=self.About, title='Tentang')

    def _init_coll_About_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1ABOUTITEMS0, kind=wx.ITEM_NORMAL,
              text='Tentang Program')
        parent.Append(help='', id=wxID_FRAME1ABOUTITEMS1, kind=wx.ITEM_NORMAL,
              text='Bantuan')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_FRAME1ABOUTITEMS3, kind=wx.ITEM_NORMAL,
              text='Keluar')
        self.Bind(wx.EVT_MENU, self.OnAboutItems3Menu,
              id=wxID_FRAME1ABOUTITEMS3)
        self.Bind(wx.EVT_MENU, self.OnAboutItems0Menu,
              id=wxID_FRAME1ABOUTITEMS0)
        self.Bind(wx.EVT_MENU, self.OnAboutItems1Menu,
              id=wxID_FRAME1ABOUTITEMS1)

    def _init_coll_notebook2_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel5, select=True,
              text='Pengertian')
        parent.AddPage(imageId=-1, page=self.panel6, select=False,
              text='Sample')

    def _init_coll_lc_ingg_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Kosakata', width=500)

    def _init_coll_lc_indo_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Kosakata', width=500)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text='Kamus Python')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Kamus B.Indonesia')
        parent.AddPage(imageId=-1, page=self.panel4, select=False,
              text='Kamus B.Inggris')

    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='KosaKata', width=400)

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.PythonTranslate = wx.Menu(title='')

        self.Administrator = wx.Menu(title='')

        self.About = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_PythonTranslate_Items(self.PythonTranslate)
        self._init_coll_Administrator_Items(self.Administrator)
        self._init_coll_About_Items(self.About)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1296, 776),
              style=wx.DEFAULT_FRAME_STYLE, title='Kamus')
        self._init_utils()
        self.SetClientSize(wx.Size(1280, 738))
        self.SetMenuBar(self.menuBar1)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1280, 738),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(119, 136, 131))

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(168, 64),
              size=wx.Size(920, 2), style=wx.SUNKEN_BORDER)
        self.staticLine1.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.staticLine1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self.panel1, pos=wx.Point(0, 72), size=wx.Size(1360, 640),
              style=0)
        self.notebook1.SetBackgroundColour(wx.Colour(255, 128, 192))
        self.notebook1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Segoe Script'))

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1352,
              600), style=wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(171, 50, 20))

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1352,
              600), style=wx.TAB_TRAVERSAL)
        self.panel3.SetBackgroundColour(wx.Colour(0, 128, 192))
        self.panel3.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              'Broadway'))

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1352,
              600), style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Kamus Sederhana', name='staticText1', parent=self.panel1,
              pos=wx.Point(456, 8), size=wx.Size(385, 48), style=0)
        self.staticText1.SetFont(wx.Font(28, wx.SWISS, wx.ITALIC, wx.BOLD,
              False, 'Snap ITC'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='KosaKata', name='staticText2', parent=self.panel2,
              pos=wx.Point(16, 32), size=wx.Size(98, 25), style=0)
        self.staticText2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Rockwell'))
        self.staticText2.SetBackgroundColour(wx.Colour(153, 32, 11))

        self.txt_kosakata = wx.TextCtrl(id=wxID_FRAME1TXT_KOSAKATA,
              name='txt_kosakata', parent=self.panel2, pos=wx.Point(144, 24),
              size=wx.Size(880, 40), style=0, value='')
        self.txt_kosakata.SetToolTipString('Cari kosakata')
        self.txt_kosakata.Bind(wx.EVT_TEXT, self.OnTxt_kosakataText,
              id=wxID_FRAME1TXT_KOSAKATA)

        self.notebook2 = wx.Notebook(id=wxID_FRAME1NOTEBOOK2, name='notebook2',
              parent=self.panel2, pos=wx.Point(0, 80), size=wx.Size(1336, 528),
              style=0)
        self.notebook2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Bell MT'))

        self.panel5 = wx.Panel(id=wxID_FRAME1PANEL5, name='panel5',
              parent=self.notebook2, pos=wx.Point(0, 0), size=wx.Size(1328,
              498), style=wx.TAB_TRAVERSAL)

        self.panel6 = wx.Panel(id=wxID_FRAME1PANEL6, name='panel6',
              parent=self.notebook2, pos=wx.Point(0, 0), size=wx.Size(1328,
              498), style=wx.TAB_TRAVERSAL)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Cari', name='staticText3', parent=self.panel3,
              pos=wx.Point(16, 24), size=wx.Size(59, 26), style=0)
        self.staticText3.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Algerian'))

        self.txt_cariindo = wx.TextCtrl(id=wxID_FRAME1TXT_CARIINDO,
              name='txt_cariindo', parent=self.panel3, pos=wx.Point(88, 16),
              size=wx.Size(672, 40), style=0, value='')
        self.txt_cariindo.SetToolTipString('Cari Kosakata')
        self.txt_cariindo.Bind(wx.EVT_TEXT, self.OnTxt_cariindoText,
              id=wxID_FRAME1TXT_CARIINDO)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1, label='Sample',
              name='staticBox1', parent=self.panel3, pos=wx.Point(8, 320),
              size=wx.Size(840, 256), style=0)
        self.staticBox1.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC, wx.BOLD, False,
              'Calisto MT'))

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label='Pengertian', name='staticBox2', parent=self.panel3,
              pos=wx.Point(8, 88), size=wx.Size(840, 224), style=0)
        self.staticBox2.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC, wx.BOLD, False,
              'Calisto MT'))

        self.txtpengertian_indo = wx.TextCtrl(id=wxID_FRAME1TXTPENGERTIAN_INDO,
              name='txtpengertian_indo', parent=self.panel3, pos=wx.Point(16,
              112), size=wx.Size(816, 192), style=wx.TE_MULTILINE, value='')
        self.txtpengertian_indo.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Arial'))

        self.txtsample_indo = wx.TextCtrl(id=wxID_FRAME1TXTSAMPLE_INDO,
              name='txtsample_indo', parent=self.panel3, pos=wx.Point(16, 344),
              size=wx.Size(816, 224), style=wx.TE_MULTILINE, value='')
        self.txtsample_indo.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Arial'))

        self.lc_indo = wx.ListCtrl(id=wxID_FRAME1LC_INDO, name='lc_indo',
              parent=self.panel3, pos=wx.Point(872, 8), size=wx.Size(392, 584),
              style=wx.LC_REPORT)
        self.lc_indo.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              'Calibri'))
        self._init_coll_lc_indo_Columns(self.lc_indo)
        self.lc_indo.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_indoListItemSelected, id=wxID_FRAME1LC_INDO)

        self.lc = wx.ListCtrl(id=wxID_FRAME1LC, name='lc', parent=self.panel5,
              pos=wx.Point(928, 8), size=wx.Size(312, 488), style=wx.LC_REPORT)
        self._init_coll_lc_Columns(self.lc)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_pythonListItemSelected, id=wxID_FRAME1LC)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='Search', name='staticText4', parent=self.panel4,
              pos=wx.Point(24, 24), size=wx.Size(85, 19), style=0)
        self.staticText4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Engravers MT'))

        self.cari_ingg = wx.TextCtrl(id=wxID_FRAME1CARI_INGG, name='cari_ingg',
              parent=self.panel4, pos=wx.Point(128, 16), size=wx.Size(632, 35),
              style=0, value='')
        self.cari_ingg.SetToolTipString('Seacrh Kosakata')
        self.cari_ingg.Bind(wx.EVT_TEXT, self.OnCari_inggText,
              id=wxID_FRAME1CARI_INGG)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label='Pengertian', name='staticBox3', parent=self.panel4,
              pos=wx.Point(8, 88), size=wx.Size(800, 224), style=0)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4, label='Sample',
              name='staticBox4', parent=self.panel4, pos=wx.Point(8, 320),
              size=wx.Size(800, 256), style=0)

        self.lc_ingg = wx.ListCtrl(id=wxID_FRAME1LC_INGG, name='lc_ingg',
              parent=self.panel4, pos=wx.Point(840, 8), size=wx.Size(424, 584),
              style=wx.LC_REPORT)
        self._init_coll_lc_ingg_Columns(self.lc_ingg)
        self.lc_ingg.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_inggListItemSelected, id=wxID_FRAME1LC_INGG)

        self.txtpengertian_ingg = wx.TextCtrl(id=wxID_FRAME1TXTPENGERTIAN_INGG,
              name='txtpengertian_ingg', parent=self.panel4, pos=wx.Point(16,
              112), size=wx.Size(776, 192), style=wx.TE_MULTILINE, value='')
        self.txtpengertian_ingg.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Arial'))

        self.txtsample_ingg = wx.TextCtrl(id=wxID_FRAME1TXTSAMPLE_INGG,
              name='txtsample_ingg', parent=self.panel4, pos=wx.Point(16, 344),
              size=wx.Size(776, 224), style=wx.TE_MULTILINE, value='')
        self.txtsample_ingg.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Arial'))

        self.txt_pengertian = wx.TextCtrl(id=wxID_FRAME1TXT_PENGERTIAN,
              name='txt_pengertian', parent=self.panel5, pos=wx.Point(8, 8),
              size=wx.Size(912, 488), style=wx.TE_MULTILINE, value='')
        self.txt_pengertian.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Bell MT'))

        self.txt_sample = wx.TextCtrl(id=wxID_FRAME1TXT_SAMPLE,
              name='txt_sample', parent=self.panel6, pos=wx.Point(0, 0),
              size=wx.Size(1320, 496), style=wx.TE_MULTILINE, value='')

        self.analogClock1 = wx.lib.analogclock.analogclock.AnalogClock(id=wxID_FRAME1ANALOGCLOCK1,
              name='analogClock1', parent=self.panel1, pos=wx.Point(1080, 0),
              size=wx.Size(264, 72), style=0)
        self.analogClock1.SetBackgroundColour(wx.Colour(119, 136, 131))

        self.txt_id = wx.TextCtrl(id=wxID_FRAME1TXT_ID, name='txt_id',
              parent=self.panel2, pos=wx.Point(1096, -40), size=wx.Size(100,
              35), style=0, value='')

        self.txt_id_ig = wx.TextCtrl(id=wxID_FRAME1TXT_ID_IG, name='txt_id_ig',
              parent=self.panel3, pos=wx.Point(1104, -40), size=wx.Size(100,
              27), style=0, value='')

        self.txt_id_ingg = wx.TextCtrl(id=wxID_FRAME1TXT_ID_INGG,
              name='txt_id_ingg', parent=self.panel4, pos=wx.Point(1064, -48),
              size=wx.Size(100, 35), style=0, value='')

        self._init_coll_notebook1_Pages(self.notebook1)
        self._init_coll_notebook2_Pages(self.notebook2)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.tampil()
        self.tampil_indo()
        self.tampil_ingg()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#----------------------------Codind main kamus python------------------------------#

    def OnPythonTranslateIndoinggMenu(self, event):
        self.main = framenotebook.create(None)
        self.main.Show()

        self.Close()
    
    def bersih_py(self):
        self.txt_pengertian.SetValue("")
        self.txt_sample.SetValue("")
    
    def tampil(self):
        self.lc.DeleteAllItems()
        sql = "select * from kms_python ORDER BY kosakata"
        cur.execute(sql)
        hasil = cur.fetchall()
        k = self.lc.GetItemCount()
        for i in hasil :
            self.lc.InsertStringItem(k,"%s"%i[1])
       
    def isi_objek(self):
        sql = "select * from kms_python where kosakata = '%s'"%(self.txt_id.GetValue())
        cur.execute(sql)
        
        hasil = cur.fetchone()
        
        self.txt_pengertian.SetValue(hasil[2])           
        
        self.txt_sample.SetValue(hasil[3])
        
            
    def OnTxt_kosakataText(self, event):
        self.lc.DeleteAllItems()
        cari = self.txt_kosakata.GetValue()
        cur.execute( "select * from kms_python where kosakata LIKE '%%%s%%'"%(cari))
        
        hasil = cur.fetchall()
        k = self.lc.GetItemCount()
        for i in hasil:
            self.lc.InsertStringItem(k,"%s"%i[1])
            k= k + 1
        self.bersih_py()
            
    def OnLc_pythonListItemSelected(self, event):
        a = event.m_itemIndex
        # mengambil no index baris yang di pilih
        b = self.lc.GetItem(a,0).GetText()                    
        #no index baris di konversikan ke text /string
        self.txt_id.SetValue(b)
        self.isi_objek()
        


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#--------------------------Codind main kamus indonesia-----------------------------#

    def bersih_indo(self):
        self.txtpengertian_indo.SetValue("")
        self.txtsample_indo.SetValue("")

    def tampil_indo(self):
        self.lc_indo.DeleteAllItems()
        sql1 = "select * from kms_indo ORDER BY kosakata_ind"
        cur.execute(sql1)
        hasil = cur.fetchall()
        j = self.lc_indo.GetItemCount()
        for i in hasil :
            self.lc_indo.InsertStringItem(j,"%s"%i[1])
            
    def objek_indo(self):
        sql1 = "select * from kms_indo where kosakata_ind = '%s'"%(self.txt_id_ig.GetValue())
        cur.execute(sql1)
        
        hasil = cur.fetchone()
        
        self.txtpengertian_indo.SetValue(hasil[2])           
        
        self.txtsample_indo.SetValue(hasil[3])

    def OnTxt_cariindoText(self, event):
        self.lc_indo.DeleteAllItems()
        cari = self.txt_cariindo.GetValue()
        cur.execute( "select * from kms_indo where kosakata_ind LIKE '%%%s%%'"%(cari))
        
        hasil = cur.fetchall()
        j = self.lc_indo.GetItemCount()
        for i in hasil:
            self.lc_indo.InsertStringItem(j,"%s"%i[1])
            j= j + 1
        self.bersih_indo()

    def OnLc_indoListItemSelected(self, event):
        a = event.m_itemIndex
        # mengambil no index baris yang di pilih
        b = self.lc_indo.GetItem(a,0).GetText()                    
        #no index baris di konversikan ke text /string
        self.txt_id_ig.SetValue(b)
        self.objek_indo()



        
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#----------------------------Codind main kamus inggris-----------------------------#

    def bersih_ingg(self):
        self.txtpengertian_ingg.SetValue("")
        self.txtsample_ingg.SetValue("")
    
    def tampil_ingg(self):
        self.lc_ingg.DeleteAllItems()
        sql2 = "select * from kms_ingg ORDER BY kosakata_ingg"
        cur.execute(sql2)
        hasil = cur.fetchall()
        d = self.lc_ingg.GetItemCount()
        for i in hasil :
            self.lc_ingg.InsertStringItem(d,"%s"%i[1])
    
    def objek_ingg(self):
        sql2 = "select * from kms_ingg where kosakata_ingg = '%s'"%(self.txt_id_ingg.GetValue())
        cur.execute(sql2)
        
        hasil = cur.fetchone()
        
        self.txtpengertian_ingg.SetValue(hasil[2])           
        
        self.txtsample_ingg.SetValue(hasil[3])
    
    def OnCari_inggText(self, event):
        self.lc_ingg.DeleteAllItems()
        cari = self.cari_ingg.GetValue()
        cur.execute( "select * from kms_ingg where kosakata_ingg LIKE '%%%s%%'"%(cari))
        
        hasil = cur.fetchall()
        d = self.lc_ingg.GetItemCount()
        for i in hasil:
            self.lc_ingg.InsertStringItem(d,"%s"%i[1])
            d= d + 1
            self.bersih_ingg()

    def OnLc_inggListItemSelected(self, event):
        a = event.m_itemIndex
        # mengambil no index baris yang di pilih
        b = self.lc_ingg.GetItem(a,0).GetText()                    
        #no index baris di konversikan ke text /string
        self.txt_id_ingg.SetValue(b)
        self.objek_ingg()
#*******************************************************************#
    def OnAboutItems3Menu(self, event):#keluar
        quit()

    def OnAboutItems0Menu(self, event):#Tentangprogram
        self.main = Tentangprogram.create(None)
        self.main.Show()
        self.Close()

    def OnAboutItems1Menu(self, event):
        self.main = Bantuan.create(None)
        self.main.Show()
        self.Close()

    def OnPythonTranslateItems1Menu(self, event):
        self.main = KamusJepang.create(None)
        self.main.Show()
        self.Close()

    def OnAdministratorItems0Menu(self, event):
        self.main = Login.create(None)
        self.main.Show()
        self.Close()
