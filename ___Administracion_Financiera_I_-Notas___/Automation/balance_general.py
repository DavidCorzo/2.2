import xlsxwriter 

class balance_general:
    def __init__(self,cuentas):
        self.cuentas                = cuentas
        self.master = {
            "Activos circulantes":[],
            "Activos no circulantes":[],
            "Pasivos circulantes":[],
            "Pasivos no circulantes":[],
            "Capital contable":[]
        }

    def sort(self):
        for i in self.cuentas: 
            if (i.get_category() == [1,0,0]):
                # es activo
                if (i.get_is_circulante()):
                    self.master["Activos circulantes"].append(i)
                else:
                    self.master["Activos no circulantes"].append(i)
            elif (i.get_category() == [0,1,0]):
                if (i.get_is_circulante()):
                    self.master["Pasivos circulantes"].append(i)
                else:
                    self.master["Pasivos no circulantes"].append(i)
            elif (i.get_category() == [0,0,1]):
                self.master["Capital contable"].append(i)
            else: print(i.get_name())
    
    def write_balance(self):
        # initialize workbook object
        workbook = xlsxwriter.Workbook('tarea.xlsx') 
        worksheet = workbook.add_worksheet() 
        
        bold = workbook.add_format({'bold': True,'underline':True})

        # for loop to print on excel sheet
        row, col = 1,1
        for k,v in self.master.items():
            worksheet.write(row,col,k.title(),bold)
            row += 1
            begining = row + 1
            for i in v: 
                worksheet.write(row,col,i.get_name().title())
                worksheet.write(row,col+1,i.get_cant1())
                worksheet.write(row,col+2,None)
                worksheet.write(row,col+3,i.get_cant2())
                row += 1
            end = row 
            row += 1
            worksheet.write_formula(f"C{row}",f'=SUM(C{begining}:C{end})')
            worksheet.write_formula(f"E{row}",f'=SUM(E{begining}:E{end})')
            worksheet.write(row-1,col,f"Total {k}",bold)
            row += 1
        workbook.close()

    

