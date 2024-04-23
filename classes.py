import tkcalendar as Calendar

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)
        self.kulonlegesseg = []
        self.picture = None
        self.rating = None
        self.rating_num = None

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)
        self.kulonlegesseg = []
        self.picture = None
        self.rating = None
        self.rating_num = None

class Szalloda:
    def __init__(self,nev):
        self.nev = nev
        self.szobak = []
        self.x_cor = None
        self.y_cor = None



class Foglalas:
    def __init__(self, idopont, szalloda, szobaszam):
        self.idopont = idopont
        self.szalloda = szalloda
        self.szobaszam = szobaszam


#From StackOverflow
class MyCalendar(Calendar.Calendar):
    def __init__(self, master=None, **kw):
        self._disabled_dates = []
        Calendar.Calendar.__init__(self, master, **kw)

    def disable_date(self, date):
        self._disabled_dates.append(date)
        mi, mj = self._get_day_coords(date)
        if mi is not None:  # date is displayed
            self._calendar[mi][mj].state(['disabled'])

    def _display_calendar(self):
        Calendar.Calendar._display_calendar(self)
        for date in self._disabled_dates:
            mi, mj = self._get_day_coords(date)
            if mi is not None:  # date is displayed
                self._calendar[mi][mj].state(['disabled'])