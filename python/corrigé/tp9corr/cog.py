import sqlite3

class cog:
    def __init__(self):
        self.conn=sqlite3.connect('cog.db')
        self.conn.text_factory = bytes

    def region_name(self, region_number):
        c=self.conn.execute('select NCCENR from regions where REGION=:reg', {'reg':region_number})
        l = c.fetchall()
        if l:
            return l[0][0].decode('latin-1')
        else:
            raise ValueError(f'No such region: {region_number}')

    def region_number(self, region_ncc):
        c=self.conn.execute('select REGION from regions where NCC=:n', {'n':region_ncc})
        l = c.fetchall()
        if l:
            return l[0][0]
        else:
            raise ValueError(f'No such region: {region_ncc}')

    def department_name(self, department_code):
        c=self.conn.execute('select NCCENR from departements where DEP=:dep', {'dep':department_code})
        l = c.fetchall()
        if l:
            return l[0][0].decode('latin-1')
        else:
            raise ValueError(f'No such department: {department_code}')

    def department_set(self, region_ncc):
        c=self.conn.execute('select departements.NCCENR from departements inner join regions on departements.REGION=regions.REGION where regions.NCC=:n', {'n':region_ncc})
        return set(d[0].decode('latin-1') for d in c)
        