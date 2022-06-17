#Boa:Frame:Frame1

import MySQLdb
import wx #MainKamus, framenotebook, KamusJepang, Tentangprogram, Bantuan
import wx.lib.analogclock
import wx.lib.masked.timectrl
import wx.lib.masked.textctrl

conn=MySQLdb.connect(host="localhost", user="root", passwd="")
cur = conn.cursor()


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1ANALOGCLOCK1, wxID_FRAME1BITMAPBUTTON16, 
 wxID_FRAME1BTN_1, wxID_FRAME1BTN_2, wxID_FRAME1BTN_3, wxID_FRAME1BTN_4, 
 wxID_FRAME1BTN_HAPUSIG, wxID_FRAME1BTN_HAPUSIND, wxID_FRAME1BTN_HAPUSPY, 
 wxID_FRAME1BTN_HOME, wxID_FRAME1BTN_KIRIM, wxID_FRAME1BTN_REFLES, 
 wxID_FRAME1BTN_TAMBAHIG, wxID_FRAME1BTN_TAMBAHIND, wxID_FRAME1BTN_TAMBAHPY, 
 wxID_FRAME1BTN_UPDATEIG, wxID_FRAME1BTN_UPDATEIND, wxID_FRAME1BTN_UPDATEPY, 
 wxID_FRAME1LC_IG, wxID_FRAME1LC_IND, wxID_FRAME1LC_KS, wxID_FRAME1LC_PY, 
 wxID_FRAME1LC_TANYA, wxID_FRAME1NOTEBOOK1, wxID_FRAME1NOTEBOOK2, 
 wxID_FRAME1NOTEBOOK3, wxID_FRAME1NOTEBOOK4, wxID_FRAME1PANEL1, 
 wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, wxID_FRAME1PANEL5, 
 wxID_FRAME1PANEL6, wxID_FRAME1PANEL7, wxID_FRAME1PANEL8, wxID_FRAME1PANEL9, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICLINE1, 
 wxID_FRAME1STATICLINE10, wxID_FRAME1STATICLINE2, wxID_FRAME1STATICLINE3, 
 wxID_FRAME1STATICLINE4, wxID_FRAME1STATICLINE5, wxID_FRAME1STATICLINE6, 
 wxID_FRAME1STATICLINE7, wxID_FRAME1STATICLINE8, wxID_FRAME1STATICLINE9, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1TXT_BALAS, wxID_FRAME1TXT_ID, 
 wxID_FRAME1TXT_ID_IG, wxID_FRAME1TXT_ID_IND, wxID_FRAME1TXT_KOSAKATAIG, 
 wxID_FRAME1TXT_KOSAKATAIND, wxID_FRAME1TXT_KOSAKATAPY, 
 wxID_FRAME1TXT_NAMA_KS, wxID_FRAME1TXT_PENGERTIANIG, 
 wxID_FRAME1TXT_PENGERTIANIND, wxID_FRAME1TXT_PENGERTIANPY, 
 wxID_FRAME1TXT_SAMPLEIG, wxID_FRAME1TXT_SAMPLEIND, wxID_FRAME1TXT_SAMPLEPY, 
 wxID_FRAME1TXT_SARAN_KS, 
] = [wx.NewId() for _init_ctrls in range(68)]

class Frame1(wx.Frame):
    def _init_coll_lc_py_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Kosataka', width=400)

    def _init_coll_notebook2_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel6, select=True,
              text='Pengertian')
        parent.AddPage(imageId=-1, page=self.panel7, select=False,
              text='Sample')

    def _init_coll_lc_ks_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Nama',
              width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Kritik Dan Saran', width=500)

    def _init_coll_lc_tanya_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Pertanyaan', width=600)

    def _init_coll_lc_ig_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Kosakata', width=400)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text='Admin Kamus Python')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Admin Kamus indonesia')
        parent.AddPage(imageId=-1, page=self.panel4, select=False,
              text='Admin Kamus inggris')
        parent.AddPage(imageId=-1, page=self.panel5, select=False,
              text='Admin Tentang / Bantuan')

    def _init_coll_lc_ind_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Kosakata', width=400)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1296, 776),
              style=wx.DEFAULT_FRAME_STYLE, title='Admin')
        self.SetClientSize(wx.Size(1280, 738))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1280, 738),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Administrator', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 0), size=wx.Size(507, 71), style=0)
        self.staticText1.SetFont(wx.Font(48, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Algerian'))

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self.panel1, pos=wx.Point(0, 72), size=wx.Size(1272, 648),
              style=0)
        self.notebook1.SetFont(wx.Font(10, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, 'Terminal'))
        self.notebook1.SetBackgroundColour(wx.Colour(75, 75, 75))

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1264,
              622), style=wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1264,
              622), style=wx.TAB_TRAVERSAL)
        self.panel3.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1264,
              622), style=wx.TAB_TRAVERSAL)
        self.panel4.SetBackgroundColour(wx.Colour(15, 15, 15))

        self.panel5 = wx.Panel(id=wxID_FRAME1PANEL5, name='panel5',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(1264,
              622), style=wx.TAB_TRAVERSAL)
        self.panel5.SetBackgroundColour(wx.Colour(64, 128, 128))

        self.notebook2 = wx.Notebook(id=wxID_FRAME1NOTEBOOK2, name='notebook2',
              parent=self.panel2, pos=wx.Point(80, 48), size=wx.Size(1120, 528),
              style=wx.RAISED_BORDER | wx.NB_LEFT)
        self.notebook2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.panel6 = wx.Panel(id=wxID_FRAME1PANEL6, name='panel6',
              parent=self.notebook2, pos=wx.Point(0, 0), size=wx.Size(1090,
              520), style=wx.TAB_TRAVERSAL)
        self.panel6.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.panel7 = wx.Panel(id=wxID_FRAME1PANEL7, name='panel7',
              parent=self.notebook2, pos=wx.Point(0, 0), size=wx.Size(1090,
              520), style=wx.TAB_TRAVERSAL)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel2, pos=wx.Point(56, 24),
              size=wx.Size(1168, 2), style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_FRAME1STATICLINE2,
              name='staticLine2', parent=self.panel2, pos=wx.Point(1224, 24),
              size=wx.Size(1, 576), style=0)

        self.staticLine3 = wx.StaticLine(id=wxID_FRAME1STATICLINE3,
              name='staticLine3', parent=self.panel2, pos=wx.Point(56, 24),
              size=wx.Size(1, 576), style=0)

        self.staticLine4 = wx.StaticLine(id=wxID_FRAME1STATICLINE4,
              name='staticLine4', parent=self.panel2, pos=wx.Point(56, 600),
              size=wx.Size(1168, 2), style=0)

        self.analogClock1 = wx.lib.analogclock.analogclock.AnalogClock(id=wxID_FRAME1ANALOGCLOCK1,
              name='analogClock1', parent=self.panel1, pos=wx.Point(1064, 0),
              size=wx.Size(208, 80), style=0)

        self.txt_kosakatapy = wx.TextCtrl(id=wxID_FRAME1TXT_KOSAKATAPY,
              name='txt_kosakatapy', parent=self.panel6, pos=wx.Point(8, 24),
              size=wx.Size(504, 40), style=0, value='')
        self.txt_kosakatapy.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Copperplate Gothic Bold'))
        self.txt_kosakatapy.SetToolTipString('Cari Kosakata')
        self.txt_kosakatapy.SetEditable(True)
        self.txt_kosakatapy.SetHelpText('fuyuyf]\\')
        self.txt_kosakatapy.Bind(wx.EVT_TEXT, self.OnTxt_kosakatapyText,
              id=wxID_FRAME1TXT_KOSAKATAPY)

        self.txt_pengertianpy = wx.TextCtrl(id=wxID_FRAME1TXT_PENGERTIANPY,
              name='txt_pengertianpy', parent=self.panel6, pos=wx.Point(8, 128),
              size=wx.Size(776, 384), style=wx.TE_MULTILINE, value='')
        self.txt_pengertianpy.SetEditable(True)

        self.lc_py = wx.ListCtrl(id=wxID_FRAME1LC_PY, name='lc_py',
              parent=self.panel6, pos=wx.Point(808, 16), size=wx.Size(264, 496),
              style=wx.LC_REPORT)
        self._init_coll_lc_py_Columns(self.lc_py)
        self.lc_py.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLc_pyListItemSelected,
              id=wxID_FRAME1LC_PY)

        self.staticLine5 = wx.StaticLine(id=wxID_FRAME1STATICLINE5,
              name='staticLine5', parent=self.panel6, pos=wx.Point(8, 96),
              size=wx.Size(776, 2), style=0)

        self.staticLine6 = wx.StaticLine(id=wxID_FRAME1STATICLINE6,
              name='staticLine6', parent=self.panel6, pos=wx.Point(795, 16),
              size=wx.Size(1, 496), style=0)

        self.btn_tambahpy = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon tambah.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1BTN_TAMBAHPY,
              name='btn_tambahpy', parent=self.panel6, pos=wx.Point(616, 32),
              size=wx.Size(88, 48), style=wx.BU_AUTODRAW)
        self.btn_tambahpy.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_tambahpy.Bind(wx.EVT_BUTTON, self.OnBtn_tambahpyButton,
              id=wxID_FRAME1BTN_TAMBAHPY)

        self.btn_updatepy = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon refles.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BTN_UPDATEPY,
              name='btn_updatepy', parent=self.panel6, pos=wx.Point(528, 32),
              size=wx.Size(88, 48), style=wx.BU_AUTODRAW)
        self.btn_updatepy.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_updatepy.Bind(wx.EVT_BUTTON, self.OnBtn_updatepyButton,
              id=wxID_FRAME1BTN_UPDATEPY)

        self.btn_hapuspy = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon hapus.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BTN_HAPUSPY,
              name='btn_hapuspy', parent=self.panel6, pos=wx.Point(704, 32),
              size=wx.Size(80, 48), style=wx.BU_AUTODRAW)
        self.btn_hapuspy.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_hapuspy.Bind(wx.EVT_BUTTON, self.OnBtn_hapuspyButton,
              id=wxID_FRAME1BTN_HAPUSPY)

        self.txt_samplepy = wx.TextCtrl(id=wxID_FRAME1TXT_SAMPLEPY,
              name='txt_samplepy', parent=self.panel7, pos=wx.Point(16, 8),
              size=wx.Size(1056, 496), style=wx.TE_MULTILINE, value='')

        self.notebook3 = wx.Notebook(id=wxID_FRAME1NOTEBOOK3, name='notebook3',
              parent=self.panel3, pos=wx.Point(48, 32), size=wx.Size(1160, 568),
              style=0)

        self.panel8 = wx.Panel(id=wxID_FRAME1PANEL8, name='panel8',
              parent=self.notebook3, pos=wx.Point(8, 8), size=wx.Size(1144,
              552), style=wx.TAB_TRAVERSAL)
        self.panel8.SetBackgroundColour(wx.Colour(255, 157, 157))

        self.txt_pengertianind = wx.TextCtrl(id=wxID_FRAME1TXT_PENGERTIANIND,
              name='txt_pengertianind', parent=self.panel8, pos=wx.Point(8, 48),
              size=wx.Size(816, 248), style=wx.TE_MULTILINE, value='')

        self.txt_sampleind = wx.TextCtrl(id=wxID_FRAME1TXT_SAMPLEIND,
              name='txt_sampleind', parent=self.panel8, pos=wx.Point(8, 304),
              size=wx.Size(816, 240), style=wx.TE_MULTILINE, value='')

        self.lc_ind = wx.ListCtrl(id=wxID_FRAME1LC_IND, name='lc_ind',
              parent=self.panel8, pos=wx.Point(840, 72), size=wx.Size(296, 472),
              style=wx.LC_REPORT)
        self._init_coll_lc_ind_Columns(self.lc_ind)
        self.lc_ind.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_indListItemSelected, id=wxID_FRAME1LC_IND)

        self.staticLine8 = wx.StaticLine(id=wxID_FRAME1STATICLINE8,
              name='staticLine8', parent=self.panel8, pos=wx.Point(832, 64),
              size=wx.Size(1, 472), style=0)

        self.btn_tambahind = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon tambah.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1BTN_TAMBAHIND,
              name='btn_tambahind', parent=self.panel8, pos=wx.Point(856, 8),
              size=wx.Size(72, 48), style=wx.BU_AUTODRAW)
        self.btn_tambahind.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_tambahind.Bind(wx.EVT_BUTTON, self.OnBtn_tambahindButton,
              id=wxID_FRAME1BTN_TAMBAHIND)

        self.btn_hapusind = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon hapus.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BTN_HAPUSIND,
              name='btn_hapusind', parent=self.panel8, pos=wx.Point(952, 8),
              size=wx.Size(72, 48), style=wx.BU_AUTODRAW)
        self.btn_hapusind.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_hapusind.Bind(wx.EVT_BUTTON, self.OnBtn_hapusindButton,
              id=wxID_FRAME1BTN_HAPUSIND)

        self.btn_updateind = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon refles.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BTN_UPDATEIND,
              name='btn_updateind', parent=self.panel8, pos=wx.Point(1048, 8),
              size=wx.Size(72, 48), style=wx.BU_AUTODRAW)
        self.btn_updateind.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_updateind.Bind(wx.EVT_BUTTON, self.OnBtn_updateindButton,
              id=wxID_FRAME1BTN_UPDATEIND)

        self.notebook4 = wx.Notebook(id=wxID_FRAME1NOTEBOOK4, name='notebook4',
              parent=self.panel4, pos=wx.Point(80, 8), size=wx.Size(1096, 608),
              style=wx.RAISED_BORDER)

        self.panel9 = wx.Panel(id=wxID_FRAME1PANEL9, name='panel9',
              parent=self.notebook4, pos=wx.Point(8, 8), size=wx.Size(1072,
              584), style=wx.TAB_TRAVERSAL)
        self.panel9.SetBackgroundColour(wx.Colour(13, 13, 255))

        self.txt_pengertianig = wx.TextCtrl(id=wxID_FRAME1TXT_PENGERTIANIG,
              name='txt_pengertianig', parent=self.panel9, pos=wx.Point(8, 48),
              size=wx.Size(760, 264), style=wx.TE_MULTILINE, value='')

        self.txt_sampleig = wx.TextCtrl(id=wxID_FRAME1TXT_SAMPLEIG,
              name='txt_sampleig', parent=self.panel9, pos=wx.Point(8, 320),
              size=wx.Size(760, 256), style=wx.TE_MULTILINE, value='')

        self.lc_ig = wx.ListCtrl(id=wxID_FRAME1LC_IG, name='lc_ig',
              parent=self.panel9, pos=wx.Point(784, 72), size=wx.Size(280, 504),
              style=wx.LC_REPORT)
        self._init_coll_lc_ig_Columns(self.lc_ig)
        self.lc_ig.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLc_igListItemSelected,
              id=wxID_FRAME1LC_IG)

        self.staticLine9 = wx.StaticLine(id=wxID_FRAME1STATICLINE9,
              name='staticLine9', parent=self.panel9, pos=wx.Point(776, 64),
              size=wx.Size(288, 2), style=0)

        self.staticLine10 = wx.StaticLine(id=wxID_FRAME1STATICLINE10,
              name='staticLine10', parent=self.panel9, pos=wx.Point(776, 64),
              size=wx.Size(1, 512), style=0)

        self.btn_tambahig = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon tambah.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1BTN_TAMBAHIG,
              name='btn_tambahig', parent=self.panel9, pos=wx.Point(792, 8),
              size=wx.Size(72, 48), style=wx.BU_AUTODRAW)
        self.btn_tambahig.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_tambahig.Bind(wx.EVT_BUTTON, self.OnBtn_tambahigButton,
              id=wxID_FRAME1BTN_TAMBAHIG)

        self.btn_hapusig = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon hapus.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BTN_HAPUSIG,
              name='btn_hapusig', parent=self.panel9, pos=wx.Point(888, 8),
              size=wx.Size(72, 48), style=wx.BU_AUTODRAW)
        self.btn_hapusig.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_hapusig.Bind(wx.EVT_BUTTON, self.OnBtn_hapusigButton,
              id=wxID_FRAME1BTN_HAPUSIG)

        self.btn_updateig = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon refles.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BTN_UPDATEIG,
              name='btn_updateig', parent=self.panel9, pos=wx.Point(984, 8),
              size=wx.Size(72, 48), style=wx.BU_AUTODRAW)
        self.btn_updateig.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_updateig.Bind(wx.EVT_BUTTON, self.OnBtn_updateigButton,
              id=wxID_FRAME1BTN_UPDATEIG)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='Kritik Dan Saran', name='staticBox1', parent=self.panel5,
              pos=wx.Point(16, 16), size=wx.Size(600, 592), style=0)
        self.staticBox1.SetBackgroundColour(wx.Colour(64, 128, 128))

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label='Pertanyaan User', name='staticBox2', parent=self.panel5,
              pos=wx.Point(672, 16), size=wx.Size(576, 592), style=0)

        self.txt_nama_ks = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA_KS,
              name='txt_nama_ks', parent=self.panel5, pos=wx.Point(160, 72),
              size=wx.Size(256, 24), style=0, value='')

        self.lc_ks = wx.ListCtrl(id=wxID_FRAME1LC_KS, name='lc_ks',
              parent=self.panel5, pos=wx.Point(24, 344), size=wx.Size(584, 256),
              style=wx.LC_REPORT)
        self._init_coll_lc_ks_Columns(self.lc_ks)
        self.lc_ks.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLc_ksListItemSelected,
              id=wxID_FRAME1LC_KS)

        self.txt_saran_ks = wx.TextCtrl(id=wxID_FRAME1TXT_SARAN_KS,
              name='txt_saran_ks', parent=self.panel5, pos=wx.Point(24, 144),
              size=wx.Size(576, 176), style=wx.TE_MULTILINE, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Nama', name='staticText2', parent=self.panel5,
              pos=wx.Point(272, 48), size=wx.Size(32, 12), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Kritik Dan Saran', name='staticText3', parent=self.panel5,
              pos=wx.Point(224, 128), size=wx.Size(144, 12), style=0)

        self.txt_balas = wx.TextCtrl(id=wxID_FRAME1TXT_BALAS, name='txt_balas',
              parent=self.panel5, pos=wx.Point(680, 80), size=wx.Size(560, 160),
              style=wx.TE_MULTILINE, value='')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='Balas', name='staticText5', parent=self.panel5,
              pos=wx.Point(928, 48), size=wx.Size(65, 16), style=0)
        self.staticText5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, True,
              'Terminal'))

        self.btn_kirim = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon kirim.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BTN_KIRIM, name='btn_kirim',
              parent=self.panel5, pos=wx.Point(1120, 248), size=wx.Size(88, 48),
              style=wx.BU_AUTODRAW)
        self.btn_kirim.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_kirim.Bind(wx.EVT_BUTTON, self.OnBtn_kirimButton,
              id=wxID_FRAME1BTN_KIRIM)

        self.bitmapButton16 = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/icon bersih.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BITMAPBUTTON16,
              name='bitmapButton16', parent=self.panel5, pos=wx.Point(704, 248),
              size=wx.Size(104, 48), style=wx.BU_AUTODRAW)
        self.bitmapButton16.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticLine7 = wx.StaticLine(id=wxID_FRAME1STATICLINE7,
              name='staticLine7', parent=self.panel8, pos=wx.Point(832, 64),
              size=wx.Size(304, 2), style=0)

        self.txt_kosakataind = wx.TextCtrl(id=wxID_FRAME1TXT_KOSAKATAIND,
              name='txt_kosakataind', parent=self.panel8, pos=wx.Point(8, 8),
              size=wx.Size(800, 32), style=0, value='')
        self.txt_kosakataind.SetToolTipString('Cari & Tambah Kosakata')
        self.txt_kosakataind.Bind(wx.EVT_TEXT, self.OnTxt_kosakataindText,
              id=wxID_FRAME1TXT_KOSAKATAIND)

        self.txt_kosakataig = wx.TextCtrl(id=wxID_FRAME1TXT_KOSAKATAIG,
              name='txt_kosakataig', parent=self.panel9, pos=wx.Point(8, 8),
              size=wx.Size(744, 32), style=0, value='')
        self.txt_kosakataig.SetToolTipString('Cari & Tambah Kosakata')
        self.txt_kosakataig.Bind(wx.EVT_TEXT, self.OnTxt_kosakataigText,
              id=wxID_FRAME1TXT_KOSAKATAIG)

        self.txt_id = wx.TextCtrl(id=wxID_FRAME1TXT_ID, name='txt_id',
              parent=self.panel2, pos=wx.Point(1080, -32), size=wx.Size(100,
              20), style=0, value='')

        self.txt_id_ind = wx.TextCtrl(id=wxID_FRAME1TXT_ID_IND,
              name='txt_id_ind', parent=self.panel8, pos=wx.Point(1032, -32),
              size=wx.Size(100, 20), style=0, value='')

        self.txt_id_ig = wx.TextCtrl(id=wxID_FRAME1TXT_ID_IG, name='txt_id_ig',
              parent=self.panel9, pos=wx.Point(960, -32), size=wx.Size(100, 20),
              style=0, value='')

        self.lc_tanya = wx.ListCtrl(id=wxID_FRAME1LC_TANYA, name='lc_tanya',
              parent=self.panel5, pos=wx.Point(680, 304), size=wx.Size(560,
              296), style=wx.LC_REPORT)
        self._init_coll_lc_tanya_Columns(self.lc_tanya)

        self.btn_refles = wx.Button(id=wxID_FRAME1BTN_REFLES, label='Refles',
              name='btn_refles', parent=self.panel5, pos=wx.Point(616, 264),
              size=wx.Size(56, 32), style=0)
        self.btn_refles.SetFont(wx.Font(9, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, 'Arial Narrow'))
        self.btn_refles.Bind(wx.EVT_BUTTON, self.OnBtn_reflesButton,
              id=wxID_FRAME1BTN_REFLES)

        self.btn_home = wx.BitmapButton(bitmap=wx.Bitmap(u'gambar/home5.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1BTN_HOME, name='btn_home',
              parent=self.panel1, pos=wx.Point(536, 0), size=wx.Size(72, 72),
              style=wx.BU_AUTODRAW)
        self.btn_home.SetToolTipString('Buka MainKamus')
        self.btn_home.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.btn_home.Bind(wx.EVT_BUTTON, self.OnBtn_homeButton,
              id=wxID_FRAME1BTN_HOME)

        self.btn_1 = wx.Button(id=wxID_FRAME1BTN_1, label='??', name='btn_1',
              parent=self.panel5, pos=wx.Point(616, 88), size=wx.Size(56, 23),
              style=0)
        self.btn_1.SetToolTipString('+-+-+-+-+-+-+-+-')
        self.btn_1.Bind(wx.EVT_BUTTON, self.OnBtn_1Button, id=wxID_FRAME1BTN_1)

        self.btn_2 = wx.Button(id=wxID_FRAME1BTN_2, label='!!', name='btn_2',
              parent=self.panel5, pos=wx.Point(616, 152), size=wx.Size(56, 24),
              style=0)
        self.btn_2.SetToolTipString('#############')
        self.btn_2.Bind(wx.EVT_BUTTON, self.OnBtn_2Button, id=wxID_FRAME1BTN_2)

        self.btn_3 = wx.Button(id=wxID_FRAME1BTN_3, label='@T@', name='btn_3',
              parent=self.panel5, pos=wx.Point(616, 344), size=wx.Size(56, 23),
              style=0)
        self.btn_3.SetToolTipString('{{}}')
        self.btn_3.Bind(wx.EVT_BUTTON, self.OnBtn_3Button, id=wxID_FRAME1BTN_3)

        self.btn_4 = wx.Button(id=wxID_FRAME1BTN_4, label='^B^', name='btn_4',
              parent=self.panel5, pos=wx.Point(616, 408), size=wx.Size(56, 23),
              style=0)
        self.btn_4.SetToolTipString('""')
        self.btn_4.Bind(wx.EVT_BUTTON, self.OnBtn_4Button, id=wxID_FRAME1BTN_4)

        self._init_coll_notebook1_Pages(self.notebook1)
        self._init_coll_notebook2_Pages(self.notebook2)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.tampil_py()
        self.tampil_indo()
        self.tampil_inggris()
        self.tampil_ks()
        self.tampil_bantuan()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#*****************************Coding Kamus Python*************************************#

    
    def tampil_py(self):
        self.lc_py.DeleteAllItems()
        sql = "select * from kms_python ORDER BY kosakata"
        cur.execute(sql)
        hasil = cur.fetchall()
        j = self.lc_py.GetItemCount()
        for i in hasil:
            self.lc_py.InsertStringItem(j,"%s"%i[1])
    
    def objeck_pdans(self):
        sql = "select * from kms_python where kosakata = '%s'"%(self.txt_id.GetValue())
        cur.execute(sql)
        
        hasil = cur.fetchone()
        
        self.txt_pengertianpy.SetValue(hasil[2])           
        
        self.txt_samplepy.SetValue(hasil[3])
        
    def bersih(self):
        self.txt_kosakatapy.SetValue("")
        self.txt_pengertianpy.SetValue("")
        self.txt_samplepy.SetValue("")
        self.txt_id.SetValue("")
        self.txt_kosakatapy.SetFocus()

    def OnBtn_tambahpyButton(self, event):
        if self.txt_kosakatapy.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text kosakata masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        elif self.txt_pengertianpy.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text pengertian masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        
        elif self.txt_samplepy.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text sample masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        
        else:
            sql = "insert into kms_python values ('%s','%s','%s','%s')"\
            %(self.txt_id.GetValue(),self.txt_kosakatapy.GetValue(),self.txt_pengertianpy.GetValue(),\
            self.txt_samplepy.GetValue())
            cur.execute(sql)
            conn.commit()
            self.pesan=wx.MessageDialog(self,"Berhasil Menambahkan kata ke database","Succes",wx.OK)
            self.pesan.ShowModal()
            self.bersih()
            self.tampil_py()
        
    
    def OnBtn_hapuspyButton(self, event):
        if self.txt_id.GetValue()=="":
            self.pesan=wx.MessageDialog(self,"Silahkan pilih dahulu Yang Akan Dihapus","Informasi",wx.OK)
            self.pesan.ShowModal()
        else:
            sql = "select * from kms_python where kosakata = '%s'" %(self.txt_id.GetValue())
            cur.execute(sql)
            hasil=cur.fetchone()
            if cur.rowcount > 0:
                tanya = wx.MessageDialog(self,"Yakin Ingin Menghapus",style=wx.YES_NO)
                if tanya.ShowModal()==wx.ID_YES:
                    sql = "delete from kms_python where kosakata = '%s'"%(self.txt_id.GetValue())
                    cur.execute(sql)
                    conn.commit()
                    self.tampil_py()
                    self.bersih()
                    self.pesan=wx.MessageDialog(self,"Data Berhasil Dihapus","Info",wx.OK)
                    self.pesan.ShowModal()
            else:
                self.pesan=wx.MessageDialog(self,"Data Yang Mau Dihapus Tidak Ada Di DATABASE","Informasi",wx.OK)
                self.pesan.ShowModal()

    def OnBtn_updatepyButton(self, event):
        self.tampil_py()
        self.bersih()

    def OnLc_pyListItemSelected(self, event):
        a = event.m_itemIndex
        b = self.lc_py.GetItem(a,0).GetText()
        self.txt_id.SetValue(b)
        self.objeck_pdans()

    def bersih_py(self):
        self.txt_pengertianpy.SetValue("")
        self.txt_samplepy.SetValue("")

    def OnTxt_kosakatapyText(self, event):
        self.lc_py.DeleteAllItems()
        cari = self.txt_kosakatapy.GetValue()
        cur.execute( "select * from kms_python where kosakata LIKE '%%%s%%'"%(cari))
        
        hasil = cur.fetchall()
        k = self.lc_py.GetItemCount()
        for i in hasil:
            self.lc_py.InsertStringItem(k,"%s"%i[1])
            k= k + 1
        self.bersih_py()
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#***********************************Coding Kamus Indo*************************************#
     
    def tampil_indo(self):
        self.lc_ind.DeleteAllItems()
        sql = "select * from kms_indo ORDER BY kosakata_ind"
        cur.execute(sql)
        hasil = cur.fetchall()
        j = self.lc_ind.GetItemCount()
        for i in hasil:
            self.lc_ind.InsertStringItem(j,"%s"%i[1])
    
    def bersih_indo(self):
        self.txt_kosakataind.SetValue("")
        self.txt_pengertianind.SetValue("")
        self.txt_sampleind.SetValue("")
        self.txt_id_ind.SetValue("")
        self.txt_kosakataind.SetFocus()
    
    
    def objeckind_pdans(self):
        sql = "select * from kms_indo where kosakata_ind = '%s'"%(self.txt_id_ind.GetValue())
        cur.execute(sql)
        
        hasil = cur.fetchone()
        
        self.txt_pengertianind.SetValue(hasil[2])           
        
        self.txt_sampleind.SetValue(hasil[3])
    
    def OnBtn_tambahindButton(self, event):
        if self.txt_kosakataind.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text kosakata masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        elif self.txt_pengertianind.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text pengertian masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        
        elif self.txt_sampleind.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text sample masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        
        else:
            sql = "insert into kms_indo values ('%s','%s','%s','%s')"\
            %(self.txt_id_ind.GetValue(),self.txt_kosakataind.GetValue(),self.txt_pengertianind.GetValue(),\
            self.txt_sampleind.GetValue())
            cur.execute(sql)
            conn.commit()
            self.pesan=wx.MessageDialog(self,"Berhasil Menambahkan kata ke database","Succes",wx.OK)
            self.pesan.ShowModal()
            self.bersih_indo()
            self.tampil_indo()

    def OnBtn_hapusindButton(self, event):
        if self.txt_id_ind.GetValue()=="":
            self.pesan=wx.MessageDialog(self,"Silahkan pilih dahulu Yang Akan Dihapus","Informasi",wx.OK)
            self.pesan.ShowModal()
        else:
            sql = "select * from kms_indo where kosakata_ind = '%s'" %(self.txt_id_ind.GetValue())
            cur.execute(sql)
            hasil=cur.fetchone()
            if cur.rowcount > 0:
                tanya = wx.MessageDialog(self,"Yakin Ingin Menghapus",style=wx.YES_NO)
                if tanya.ShowModal()==wx.ID_YES:
                    sql = "delete from kms_indo where kosakata_ind = '%s'"%(self.txt_id_ind.GetValue())
                    cur.execute(sql)
                    conn.commit()
                    self.tampil_indo()
                    self.bersih_indo()
                    self.pesan=wx.MessageDialog(self,"Data Berhasil Dihapus","Info",wx.OK)
                    self.pesan.ShowModal()
            else:
                self.pesan=wx.MessageDialog(self,"Data Yang Mau Dihapus Tidak Ada Di DATABASE","Informasi",wx.OK)
                self.pesan.ShowModal()


    def OnBtn_updateindButton(self, event):
        self.tampil_indo()
        self.bersih_indo()

    def OnLc_indListItemSelected(self, event):
        a = event.m_itemIndex
        b = self.lc_ind.GetItem(a,0).GetText()
        self.txt_id_ind.SetValue(b)
        self.objeckind_pdans()
        
    def bersih_ind2(self):
        self.txt_pengertianind.SetValue("")
        self.txt_sampleind.SetValue("")

    def OnTxt_kosakataindText(self, event):
        self.lc_ind.DeleteAllItems()
        cari = self.txt_kosakataind.GetValue()
        cur.execute( "select * from kms_indo where kosakata_ind LIKE '%%%s%%'"%(cari))
        
        hasil = cur.fetchall()
        k = self.lc_ind.GetItemCount()
        for i in hasil:
            self.lc_ind.InsertStringItem(k,"%s"%i[1])
            k= k + 1
        self.bersih_ind2()
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#*********************************Coding Kamus Inggris************************************#
    
    def tampil_inggris(self):
        self.lc_ig.DeleteAllItems()
        sql = "select * from kms_ingg ORDER BY kosakata_ingg"
        cur.execute(sql)
        hasil = cur.fetchall()
        j = self.lc_ig.GetItemCount()
        for i in hasil:
            self.lc_ig.InsertStringItem(j,"%s"%i[1])
    
    def bersih_inggris(self):
        self.txt_kosakataig.SetValue("")
        self.txt_pengertianig.SetValue("")
        self.txt_sampleig.SetValue("")
        self.txt_id_ig.SetValue("")
        self.txt_kosakataig.SetFocus()
    
    
    def objeckig_pdans(self):
        sql = "select * from kms_ingg where kosakata_ingg = '%s'"%(self.txt_id_ig.GetValue())
        cur.execute(sql)
        
        hasil = cur.fetchone()
        
        self.txt_pengertianig.SetValue(hasil[2])           
        
        self.txt_sampleig.SetValue(hasil[3])


    def OnBtn_tambahigButton(self, event):
        if self.txt_kosakataig.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text kosakata masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        elif self.txt_pengertianig.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text pengertian masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        
        elif self.txt_sampleig.GetValue() == "":
            self.pesan=wx.MessageDialog(self,"Text sample masih kosong","Info",wx.OK)
            self.pesan.ShowModal()
        
        else:
            sql = "insert into kms_ingg values ('%s','%s','%s','%s')"\
            %(self.txt_id_ig.GetValue(),self.txt_kosakataig.GetValue(),self.txt_pengertianig.GetValue(),\
            self.txt_sampleig.GetValue())
            cur.execute(sql)
            conn.commit()
            self.pesan=wx.MessageDialog(self,"Berhasil Menambahkan kata ke database","Succes",wx.OK)
            self.pesan.ShowModal()
            self.bersih_inggris()
            self.tampil_inggris()

    def OnBtn_hapusigButton(self, event):
        if self.txt_id_ig.GetValue()=="":
            self.pesan=wx.MessageDialog(self,"Silahkan pilih dahulu Yang Akan Dihapus","Informasi",wx.OK)
            self.pesan.ShowModal()
        else:
            sql = "select * from kms_ingg where kosakata_ingg = '%s'" %(self.txt_id_ig.GetValue())
            cur.execute(sql)
            hasil=cur.fetchone()
            if cur.rowcount > 0:
                tanya = wx.MessageDialog(self,"Yakin Ingin Menghapus",style=wx.YES_NO)
                if tanya.ShowModal()==wx.ID_YES:
                    sql = "delete from kms_ingg where kosakata_ingg = '%s'"%(self.txt_id_ig.GetValue())
                    cur.execute(sql)
                    conn.commit()
                    self.tampil_inggris()
                    self.bersih_inggris()
                    self.pesan=wx.MessageDialog(self,"Data Berhasil Dihapus","Info",wx.OK)
                    self.pesan.ShowModal()
            else:
                self.pesan=wx.MessageDialog(self,"Data Yang Mau Dihapus Tidak Ada Di DATABASE","Informasi",wx.OK)
                self.pesan.ShowModal()

    def OnBtn_updateigButton(self, event):
        self.tampil_inggris()
        self.bersih_inggris()

    def OnLc_igListItemSelected(self, event):
        a = event.m_itemIndex
        b = self.lc_ig.GetItem(a,0).GetText()
        self.txt_id_ig.SetValue(b)
        self.objeckig_pdans()
        
    def bersih_inggris2(self):
        self.txt_pengertianig.SetValue("")
        self.txt_sampleig.SetValue("")

    def OnTxt_kosakataigText(self, event):
        self.lc_ig.DeleteAllItems()
        cari = self.txt_kosakataig.GetValue()
        cur.execute( "select * from kms_ingg where kosakata_ingg LIKE '%%%s%%'"%(cari))
        
        hasil = cur.fetchall()
        k = self.lc_ig.GetItemCount()
        for i in hasil:
            self.lc_ig.InsertStringItem(k,"%s"%i[1])
            k= k + 1
        self.bersih_inggris2()
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#******************************Coding Menu Saran Dan Bantuan******************************#
    
    def tampil_ks(self):
        sql = "select * from tentangprogram"
        cur.execute(sql)
        hasil=cur.fetchall()
        k = self.lc_ks.GetItemCount()
        for i in hasil:
            self.lc_ks.InsertStringItem(k,"%s"%i[0])
            self.lc_ks.SetStringItem(k,1,"%s"%i[1])
            
            k = k+1

    def OnLc_ksListItemSelected(self, event):
        no_baris = event.m_itemIndex
        
        nama = self.lc_ks.GetItem(no_baris,0).GetText()
        ks = self.lc_ks.GetItem(no_baris,1).GetText()
        
        self.txt_nama_ks.SetValue(nama)
        self.txt_saran_ks.SetValue(ks)

    def tampil_bantuan(self):
        sql = "select * from pertanyaan"
        cur.execute(sql)
        hasil=cur.fetchall()
        k = self.lc_tanya.GetItemCount()
        for i in hasil:
            self.lc_tanya.InsertStringItem(k,"%s"%i[0])
            
            k = k+1

    def OnBtn_kirimButton(self, event):
        if self.txt_balas.GetValue()== "":
            self.pesan = wx.MessageDialog(self,"Anda Belum Memberi Balasan","Informasi",wx.OK)
            self.pesan.ShowModal()
        
        else:
            sql = "insert into balasan values \
            ('%s')"%(self.txt_balas.GetValue())
            cur.execute(sql)
            conn.commit()
            self.pesan = wx.MessageDialog(self,"Balasan Anda Sudah Terkirim ","Informasi",wx.OK)
            self.pesan.ShowModal()
            self.txt_balas.SetValue("")
            self.txt_balas.SetFocus()

    def OnBtn_reflesButton(self, event):
        self.txt_nama_ks.SetValue("")
        self.txt_saran_ks.SetValue("")
        self.txt_balas.SetValue("")
        self.txt_balas.SetFocus()

    def OnBtn_homeButton(self, event):
        self.main = MainKamus.create(None)
        self.main.Show()

    def OnBtn_1Button(self, event):
        self.main = framenotebook.create(None)
        self.main.Show()
        
    def OnBtn_2Button(self, event):
        self.main = KamusJepang.create(None)
        self.main.Show()
        

    def OnBtn_3Button(self, event):
        self.main = Tentangprogram.create(None)
        self.main.Show()
        

    def OnBtn_4Button(self, event):
        self.main = Bantuan.create(None)
        self.main.Show()
        

    

